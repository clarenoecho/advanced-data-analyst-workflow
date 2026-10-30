"""Tes untuk tools/setup_awal.py, tools/atur_github.py, dan tools/bangun_paket.py.
Memakai salinan repo di folder sementara dan remote bare sungguhan (tanpa jaringan).
"""
import contextlib
import importlib.util
import io
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def muat(nama):
    spec = importlib.util.spec_from_file_location(nama, ROOT / "tools" / f"{nama}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SA = muat("setup_awal")
AG = muat("atur_github")
P = muat("progress")


def git(cwd, *args):
    r = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise AssertionError(f"git {' '.join(args)}: {r.stderr}")
    return r.stdout.strip()


def salin_repo(tujuan: Path):
    shutil.copytree(ROOT, tujuan, ignore=shutil.ignore_patterns(".git", "__pycache__", "paket_project"))


class TestAturGithub(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.work = self.tmp / "work"
        salin_repo(self.work)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def jalan(self, *args):
        with contextlib.redirect_stdout(io.StringIO()):
            return AG.main(["--root", str(self.work), *args])

    def test_penanda_ada_di_dokumen_penting(self):
        for f in ("system/04_protokol_mentor.md", "docs/panduan_chatgpt_project.md", "PANDUAN.md"):
            self.assertIn(AG.PENANDA, (ROOT / f).read_text(encoding="utf-8"), f)

    def test_mengganti_semua_penanda(self):
        self.assertEqual(self.jalan("tasya-data"), 0)
        for p in AG.sasaran(self.work):
            self.assertNotIn(AG.PENANDA, p.read_text(encoding="utf-8"), p)
        teks = (self.work / "system" / "04_protokol_mentor.md").read_text(encoding="utf-8")
        self.assertIn("raw.githubusercontent.com/tasya-data/advanced-data-analyst-workflow/main/state/dashboard.md", teks)

    def test_dry_tidak_mengubah(self):
        sebelum = (self.work / "system" / "04_protokol_mentor.md").read_text(encoding="utf-8")
        self.assertEqual(self.jalan("tasya-data", "--dry"), 0)
        self.assertEqual(sebelum, (self.work / "system" / "04_protokol_mentor.md").read_text(encoding="utf-8"))

    def test_username_tidak_sah_ditolak(self):
        for bad in ("-tasya", "tasya data", "tasya/x", "a" * 40, "tasya--data"):
            self.assertEqual(self.jalan("--", bad), 1, bad)


class TestBangunPaket(unittest.TestCase):
    def test_paket_berisi_empat_file_tanpa_front_matter_ganda(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            salin_repo(tmp / "work")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(muat("bangun_paket").main(["--root", str(tmp / "work")]), 0)
            berkas = sorted(p.name for p in (tmp / "work" / "paket_project").iterdir())
            self.assertEqual(berkas, ["02_roadmap.md", "09_kurikulum.md", "aturan_mentor.md"])
            self.assertLessEqual(len(berkas), 3, "harus muat di kuota unggah ChatGPT Free (3 file per hari)")
            aturan = (tmp / "work" / "paket_project" / "aturan_mentor.md").read_text(encoding="utf-8")
            self.assertIn("Dapur Data", aturan)
            self.assertIn("[BAGIAN 7 dari 7] KEBIJAKAN REFERENSI BELAJAR", aturan)
            self.assertIn("RUBRIK VALIDASI", aturan)
            self.assertIn("Mode hemat ChatGPT Free", aturan)
            self.assertIn("Instruksi inti", aturan)
            self.assertNotIn("\n---\ndokumen:", aturan)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class TestSalinDashboard(unittest.TestCase):
    def test_teks_berisi_dashboard_tanpa_komentar(self):
        SD = muat("salin_dashboard")
        teks = SD.teks_dashboard(ROOT)
        self.assertTrue(teks.startswith("cek progres"))
        self.assertIn("DAPUR DATA", teks)
        self.assertNotIn("<!--", teks)

    def test_tanpa_dashboard_gagal_dengan_pesan(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(muat("salin_dashboard").main(["--root", str(tmp)]), 1)
            self.assertIn("tidak ditemukan", out.getvalue())
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class TestSetupAwal(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.work = self.tmp / "work"
        self.remote = self.tmp / "remote.git"
        salin_repo(self.work)
        git(self.tmp, "init", "--bare", "-b", "main", str(self.remote))
        # konfigurasi git global palsu supaya tes tidak menyentuh milik pengguna
        self.env_lama = {k: os.environ.get(k) for k in ("GIT_CONFIG_GLOBAL", "GIT_CONFIG_NOSYSTEM")}
        os.environ["GIT_CONFIG_GLOBAL"] = str(self.tmp / "gitconfig")
        os.environ["GIT_CONFIG_NOSYSTEM"] = "1"
        (self.tmp / "gitconfig").write_text("[commit]\n\tgpgsign = false\n", encoding="utf-8")
        # origin diarahkan ke remote bare (setup tidak menimpa origin yang sudah ada)
        git(self.work, "init", "-b", "main")
        git(self.work, "remote", "add", "origin", str(self.remote))

    def tearDown(self):
        for k, v in self.env_lama.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(self.tmp, ignore_errors=True)

    def jalan(self, username="tasya-data", jawaban=("Tasya", "tasya@example.com")):
        it = iter(jawaban)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            kode = SA.proses(self.work, username, pasang=False, push=True, tanya_fn=lambda _: next(it))
        return kode, out.getvalue()

    def test_setup_lengkap(self):
        kode, keluar = self.jalan()
        self.assertEqual(kode, 0, keluar)
        self.assertEqual(git(self.remote, "log", "-1", "--format=%s", "main"), "awal: Dapur Data siap dipakai")
        self.assertEqual(git(self.work, "config", "user.name"), "Tasya")
        teks = (self.work / "system" / "04_protokol_mentor.md").read_text(encoding="utf-8")
        self.assertIn("tasya-data/advanced-data-analyst-workflow", teks)
        self.assertTrue((self.work / "paket_project" / "aturan_mentor.md").exists())
        berkas = git(self.remote, "ls-tree", "-r", "--name-only", "main").splitlines()
        self.assertIn("state/state.yaml", berkas)
        self.assertIn("latihan/0_python_dasar/.gitkeep", berkas)
        self.assertFalse(any(b.startswith("paket_project/") for b in berkas))
        self.assertFalse(any("__pycache__" in b for b in berkas))
        self.assertEqual(P.check(P.Repo(self.work))[0], [])

    def test_aman_dijalankan_ulang(self):
        self.jalan()
        kode, keluar = self.jalan(jawaban=())
        self.assertEqual(kode, 0, keluar)
        self.assertIn("sudah terisi", keluar)
        self.assertEqual(git(self.remote, "rev-list", "--count", "main"), "1")

    def test_username_tidak_sah(self):
        with self.assertRaises(SA.Gagal):
            self.jalan(username="bukan username")


if __name__ == "__main__":
    unittest.main()
