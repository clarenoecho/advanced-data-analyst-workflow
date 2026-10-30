"""Tes untuk tools/progress.py. Jalankan dari akar repo:
    python -m unittest discover -s tests -v
"""
import contextlib
import datetime as dt
import importlib.util
import io
import re
import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("progress", ROOT / "tools" / "progress.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

D = dt.date

# State uji dibekukan di tests/fixtures/state (kondisi awal: resep pertama aktif),
# supaya tes tidak ikut berubah ketika state.yaml asli maju.
FIXTURE = ROOT / "tests" / "fixtures" / "state"
URUTAN_FASE_0 = ["py_setup", "py_dasar", "py_kontrol", "py_struktur_data", "py_fungsi_modul",
                 "py_error_file", "py_venv_git"]


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(FIXTURE, self.tmp / "state")
        (self.tmp / "latihan").mkdir()
        (self.tmp / "latihan" / "bukti.ipynb").write_text("{}", encoding="utf-8")
        self.repo = P.Repo(self.tmp)
        self.today = D(2026, 11, 1)
        self.n = 0

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def entry(self, dir=None, **kw):
        self.n += 1
        e = {
            "id": f"uji-{self.n}", "modul": "py_setup", "tanggal": D(2026, 11, 1),
            "jenis": "validasi", "skor_persen": 90, "mode_ai": "assisted",
            "level_soal": "L1, L2", "bukti": ["latihan/bukti.ipynb"],
            "pemahaman": "Memakai notebook supaya penjelasan dan kode bersatu; menyimpan di latihan/",
            "keputusan": "validated",
        }
        e.update(kw)
        p = (dir or self.tmp) / f"{e['id']}.yaml"
        p.write_text(yaml.safe_dump(e, allow_unicode=True, sort_keys=False), encoding="utf-8")
        return p

    def apply(self, today=None, **kw):
        return P.apply_entry(self.repo, self.entry(**kw), today or self.today)

    def item(self, item_id):
        data, _ = self.repo.load()
        return P.find(data, item_id)[1]["item"]

    def selesaikan(self, ids):
        for i in ids:
            self.apply(modul=i)


class TestState(Base):
    def test_state_fixture_konsisten(self):
        errors, _ = P.check(self.repo)
        self.assertEqual(errors, [])

    def test_state_hidup_konsisten(self):
        """state/state.yaml yang sebenarnya harus konsisten (inilah yang dijaga di GitHub)."""
        errors, _ = P.check(P.Repo(ROOT))
        self.assertEqual(errors, [])

    def test_roundtrip_tidak_mengubah_data(self):
        data, header = self.repo.load()
        self.repo.save(data, header)
        data2, header2 = self.repo.load()
        self.assertEqual(data, data2)
        self.assertEqual(header, header2)

    def test_dua_resep_aktif_terdeteksi(self):
        data, _ = self.repo.load()
        P.find(data, "py_dasar")[1]["item"]["status"] = "aktif"
        errors, _ = P.check(self.repo, data)
        self.assertTrue(any("lebih dari satu resep aktif" in e for e in errors))

    def test_lompatan_terdeteksi(self):
        data, _ = self.repo.load()
        P.find(data, "sql_join")[1]["item"]["status"] = "validated"
        errors, _ = P.check(self.repo, data)
        self.assertTrue(any("melompati roadmap" in e for e in errors))

    def test_validated_tanpa_evidence_ditolak(self):
        data, _ = self.repo.load()
        it = P.find(data, "py_setup")[1]["item"]
        it["status"] = "validated"
        P.find(data, "py_dasar")[1]["item"]["status"] = "aktif"
        errors, _ = P.check(self.repo, data)
        self.assertTrue(any("wajib punya evidence" in e for e in errors))

    def test_portfolio_terkunci_sebelum_prasyarat(self):
        data, _ = self.repo.load()
        P.find(data, "porto_0")[1]["item"]["status"] = "aktif"
        P.find(data, "py_setup")[1]["item"]["status"] = "belum"
        errors, _ = P.check(self.repo, data)
        self.assertTrue(any("prasyarat" in e for e in errors))

    def test_status_legacy_tidak_sah(self):
        data, _ = self.repo.load()
        P.find(data, "py_setup")[1]["item"]["status"] = "validated_legacy"
        errors, _ = P.check(self.repo, data)
        self.assertTrue(any("status tidak sah" in e for e in errors))


class TestValidasi(Base):
    def test_lulus_memajukan_resep(self):
        self.apply()
        it = self.item("py_setup")
        self.assertEqual(it["status"], "validated")
        self.assertEqual(it["review_berikutnya"], D(2026, 11, 8))
        self.assertEqual(self.item("py_dasar")["status"], "aktif")
        data, _ = self.repo.load()
        self.assertEqual(data["quest_berikutnya"], "py_kontrol")
        self.assertEqual(data["kemenangan_terbaru"], "py_setup")
        errors, warnings = P.check(self.repo)
        self.assertEqual(errors, [])
        self.assertFalse(any("tidak sinkron" in w for w in warnings))

    def test_skor_rendah_status_tidak_berubah(self):
        self.apply(skor_persen=70, keputusan="tetap")
        self.assertEqual(self.item("py_setup")["status"], "aktif")
        self.assertEqual(self.item("py_dasar")["status"], "belum")
        self.assertTrue((self.tmp / "state" / "evidence" / "uji-1.yaml").exists())

    def test_ambang_tepat_80_lulus(self):
        self.apply(skor_persen=80)
        self.assertEqual(self.item("py_setup")["status"], "validated")

    def test_keputusan_tidak_sesuai_ditolak(self):
        with self.assertRaises(P.StateError):
            self.apply(skor_persen=70, keputusan="validated")

    def test_melompati_resep_ditolak(self):
        with self.assertRaises(P.StateError):
            self.apply(modul="py_dasar")

    def test_pemahaman_wajib(self):
        with self.assertRaises(P.StateError):
            self.apply(pemahaman="")

    def test_tanggal_masa_depan_ditolak(self):
        with self.assertRaises(P.StateError):
            self.apply(tanggal=D(2026, 12, 1))

    def test_skor_boolean_ditolak(self):
        with self.assertRaises(P.StateError):
            self.apply(skor_persen=True)

    def test_learned_lalu_validasi(self):
        P.mark_learned(self.repo, "py_setup", self.today)
        self.assertEqual(self.item("py_setup")["status"], "learned")
        self.assertEqual(P.check(self.repo)[0], [])
        self.apply()
        self.assertEqual(self.item("py_setup")["status"], "validated")

    def test_dry_run_tidak_mengubah_file(self):
        before = (self.tmp / "state" / "state.yaml").read_text(encoding="utf-8")
        P.apply_entry(self.repo, self.entry(), self.today, dry=True)
        self.assertEqual(before, (self.tmp / "state" / "state.yaml").read_text(encoding="utf-8"))


class TestFaseDanOpsional(Base):
    def test_opsional_dilewati_dan_portfolio_terbuka(self):
        self.selesaikan(URUTAN_FASE_0)
        self.assertEqual(self.item("py_oop")["status"], "belum")
        self.assertEqual(self.item("porto_0")["status"], "aktif")
        self.assertEqual(P.check(self.repo)[0], [])

    def test_opsional_boleh_divalidasi_tanpa_menggeser_resep_aktif(self):
        self.selesaikan(URUTAN_FASE_0)
        self.apply(modul="py_oop")
        self.assertEqual(self.item("py_oop")["status"], "validated")
        self.assertEqual(self.item("porto_0")["status"], "aktif")
        self.assertEqual(P.check(self.repo)[0], [])

    def test_opsional_belum_terbuka_ditolak(self):
        with self.assertRaises(P.StateError):
            self.apply(modul="py_oop")

    def test_fase_lulus_menaikkan_pangkat_dan_membuka_fase_berikutnya(self):
        data, _ = self.repo.load()
        self.assertEqual(P.pangkat(data), "Trainee Dapur")
        self.selesaikan(URUTAN_FASE_0)
        msgs, _ = self.apply(modul="porto_0")
        self.assertTrue(any("Pangkat baru: Commis Chef" in m for m in msgs))
        self.assertEqual(self.item("numpy_esensial")["status"], "aktif")
        data, _ = self.repo.load()
        self.assertEqual(data["posisi_saat_ini"], {"fase": 1, "modul": "numpy_esensial", "quest": None})
        self.assertEqual(data["quest_berikutnya"], "pd_dasar_io")
        out = P.render_dashboard(data)
        self.assertIn("Commis Chef", out)
        self.assertIn("🏅 LULUS", out)
        self.assertEqual(P.check(self.repo)[0], [])

    def test_modul_berquest_menampilkan_menu_aktif(self):
        self.selesaikan(URUTAN_FASE_0 + ["porto_0", "numpy_esensial"])
        data, _ = self.repo.load()
        self.assertEqual(data["posisi_saat_ini"], {"fase": 1, "modul": "pandas", "quest": "pd_dasar_io"})
        out = P.render_dashboard(data)
        self.assertIn("🍳 MENU AKTIF", out)
        self.assertIn("PANDAS", out)

    def test_entri_untuk_modul_induk_ditolak(self):
        self.selesaikan(URUTAN_FASE_0 + ["porto_0", "numpy_esensial"])
        with self.assertRaises(P.StateError) as cm:
            self.apply(modul="pandas")
        self.assertIn("id resep yang benar-benar diuji", str(cm.exception))
        self.assertIn("pd_dasar_io", str(cm.exception))


class TestRetensi(Base):
    def test_retrieval_jeda_dan_retained(self):
        self.apply()  # py_setup validated 2026-11-01
        with self.assertRaises(P.StateError):
            self.apply(modul="py_setup", jenis="retrieval", mode_ai="independent",
                       tanggal=D(2026, 11, 5), keputusan="retained", today=D(2026, 11, 5))
        self.apply(modul="py_setup", jenis="retrieval", mode_ai="independent", pemahaman=None,
                   tanggal=D(2026, 11, 8), keputusan="retained", today=D(2026, 11, 8))
        it = self.item("py_setup")
        self.assertEqual(it["status"], "retained")
        self.assertEqual(it["review_berikutnya"], D(2026, 12, 1))

    def test_retrieval_wajib_independent(self):
        self.apply()
        with self.assertRaises(P.StateError):
            self.apply(modul="py_setup", jenis="retrieval", mode_ai="assisted",
                       tanggal=D(2026, 11, 8), keputusan="retained", today=D(2026, 11, 8))

    def test_retrieval_untuk_resep_belum_validated_ditolak(self):
        with self.assertRaises(P.StateError):
            self.apply(jenis="retrieval", mode_ai="independent", keputusan="retained")

    def test_retrieval_gagal_menandai_perlu_review(self):
        self.apply()
        self.apply(modul="py_setup", jenis="retrieval", mode_ai="independent",
                   skor_persen=60, keputusan="tetap", tanggal=D(2026, 11, 8), today=D(2026, 11, 8))
        it = self.item("py_setup")
        self.assertEqual(it["status"], "validated")
        self.assertTrue(it["perlu_review"])
        self.assertEqual(it["review_berikutnya"], D(2026, 11, 11))

    def test_mastery_butuh_retained_dan_dua_konteks(self):
        self.apply()
        with self.assertRaises(P.StateError):  # masih validated
            self.apply(modul="py_setup", jenis="mastery", mode_ai="independent",
                       konteks=["a", "b"], keputusan="mastered")
        h8 = D(2026, 11, 8)
        self.apply(modul="py_setup", jenis="retrieval", mode_ai="independent",
                   tanggal=h8, keputusan="retained", today=h8)
        with self.assertRaises(P.StateError):  # konteks kurang
            self.apply(modul="py_setup", jenis="mastery", mode_ai="independent",
                       konteks=["satu"], keputusan="mastered", tanggal=h8, today=h8)
        self.apply(modul="py_setup", jenis="mastery", mode_ai="independent",
                   konteks=["proyek A", "proyek B"], keputusan="mastered", tanggal=h8, today=h8)
        self.assertEqual(self.item("py_setup")["status"], "mastered")


class TestDueDanDashboard(Base):
    def test_due(self):
        self.apply()
        data, _ = self.repo.load()
        self.assertEqual(P.due(data, D(2026, 11, 7)), [])
        jatuh = P.due(data, D(2026, 11, 8))
        self.assertEqual([i["id"] for i, _ in jatuh], ["py_setup"])

    def test_dashboard_memuat_elemen_wajib(self):
        data, _ = self.repo.load()
        out = P.render_dashboard(data)
        for s in ("DAPUR DATA", "Tasya", "PANGKAT", "Trainee Dapur", "FASE 0", "FASE 7",
                  "🔥 SEDANG DIMASAK", "🔒 TERKUNCI", "⏭️ OPSIONAL", "RESEP AKTIF",
                  "RESEP BERIKUTNYA", "POSISI SEKARANG"):
            self.assertIn(s, out)
        self.assertNotIn("LEGACY", out)

    def test_dashboard_dari_cli_tulis(self):
        with contextlib.redirect_stdout(io.StringIO()):
            rc = P.main(["--root", str(self.tmp), "--today", "2026-11-01", "dashboard", "--tulis"])
        self.assertEqual(rc, 0)
        errors, warnings = P.check(self.repo)
        self.assertEqual(errors, [])
        self.assertFalse(any("tidak sinkron" in w for w in warnings))

    def test_dashboard_hidup_sinkron(self):
        _, warnings = P.check(P.Repo(ROOT))
        self.assertFalse(any("dashboard" in w for w in warnings), warnings)


class TestKeamananEntri(Base):
    def test_bukti_harus_ada_di_repo(self):
        with self.assertRaisesRegex(P.StateError, "bukti tidak ditemukan"):
            self.apply(bukti=["latihan/tidak_ada.ipynb"])

    def test_bukti_url_diterima(self):
        self.apply(bukti=["https://github.com/contoh/repo/blob/main/x.ipynb"])
        self.assertEqual(self.item("py_setup")["status"], "validated")

    def test_bukti_di_luar_repo_ditolak(self):
        for b in ("../rahasia.txt", "/etc/passwd", "C:/Windows/win.ini"):
            with self.assertRaises(P.StateError, msg=b):
                self.apply(bukti=[b])

    def test_bukti_boleh_garis_miring_windows(self):
        self.apply(bukti=["latihan\\bukti.ipynb"])
        self.assertEqual(self.item("py_setup")["status"], "validated")

    def test_id_berbahaya_ditolak(self):
        for bad in ("../../x", "a.b", "a/b", "ab", "x" * 81, ""):
            p = self.entry(id="aman-1")
            data = yaml.safe_load(p.read_text(encoding="utf-8"))
            data["id"] = bad
            p.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
            with self.assertRaises(P.StateError, msg=repr(bad)):
                P.apply_entry(self.repo, p, self.today)
        self.assertFalse((self.tmp / "state" / "evidence").exists()
                         and any((self.tmp / "state" / "evidence").iterdir()))

    def test_id_ganda_ditolak(self):
        self.apply(id="sekali-saja")
        with self.assertRaisesRegex(P.StateError, "sudah pernah dipakai"):
            self.apply(id="sekali-saja", modul="py_dasar")

    def test_entri_bukan_pemetaan_ditolak(self):
        p = self.tmp / "daftar.yaml"
        p.write_text("- a\n- b\n", encoding="utf-8")
        with self.assertRaises(P.StateError):
            P.apply_entry(self.repo, p, self.today)

    def test_yaml_rusak_ditolak(self):
        p = self.tmp / "rusak.yaml"
        p.write_text("id: [belum ditutup\n  modul: x: y", encoding="utf-8")
        with self.assertRaises(P.StateError):
            P.apply_entry(self.repo, p, self.today)

    def test_entri_terlalu_besar_ditolak(self):
        p = self.tmp / "besar.yaml"
        p.write_text("x: " + "a" * (P.BATAS_ENTRI_BYTE + 10), encoding="utf-8")
        with self.assertRaisesRegex(P.StateError, "ukuran"):
            P.apply_entry(self.repo, p, self.today)


class TestInbox(Base):
    def setUp(self):
        super().setUp()
        self.inbox = self.tmp / "state" / "inbox"
        self.inbox.mkdir()
        (self.inbox / "README.md").write_text("abaikan", encoding="utf-8")

    def jalan(self, *extra):
        with contextlib.redirect_stdout(io.StringIO()):
            return P.main(["--root", str(self.tmp), "--today", "2026-11-01", "inbox", *extra])

    def test_inbox_kosong_aman(self):
        self.assertEqual(self.jalan(), 0)

    def test_entri_valid_diterapkan(self):
        self.entry(dir=self.inbox)
        self.assertEqual(self.jalan(), 0)
        self.assertEqual(self.item("py_setup")["status"], "validated")
        self.assertFalse((self.inbox / "uji-1.yaml").exists())
        self.assertTrue((self.inbox / "README.md").exists())
        self.assertEqual(P.check(self.repo)[0], [])

    def test_entri_ditolak_dipindah_dengan_alasan(self):
        self.entry(dir=self.inbox, skor_persen=70, keputusan="validated")
        self.assertEqual(self.jalan(), 1)
        self.assertEqual(self.item("py_setup")["status"], "aktif")
        alasan = (self.inbox / "ditolak" / "uji-1.yaml.alasan.txt").read_text(encoding="utf-8")
        self.assertIn("hasil perhitungan", alasan)

    def test_urutan_nama_berkas_dihormati(self):
        self.entry(dir=self.inbox, id="b-dasar", modul="py_dasar")
        self.entry(dir=self.inbox, id="a-setup")
        self.assertEqual(self.jalan(), 0)
        self.assertEqual(self.item("py_dasar")["status"], "validated")


class TestKurikulum(unittest.TestCase):
    """Setiap resep di state.yaml harus punya rincian di system/09_kurikulum.md, dan sebaliknya."""

    def test_id_state_dan_kurikulum_sama(self):
        data, _ = P.Repo(ROOT).load()
        state_ids = [r["item"]["id"] for r in P.leaves(data)]
        teks = (ROOT / "system" / "09_kurikulum.md").read_text(encoding="utf-8")
        kur_ids = re.findall(r"^#### `([a-z0-9_]+)`", teks, re.M)
        self.assertEqual(len(kur_ids), len(set(kur_ids)), "id ganda di kurikulum")
        self.assertEqual(sorted(set(state_ids) - set(kur_ids)), [], "resep di state tanpa rincian kurikulum")
        self.assertEqual(sorted(set(kur_ids) - set(state_ids)), [], "id di kurikulum yang tidak ada di state")
        self.assertEqual(kur_ids, state_ids, "urutan kurikulum harus sama dengan urutan state")

    def test_fixture_dan_state_hidup_punya_struktur_sama(self):
        hidup, _ = P.Repo(ROOT).load()
        beku = yaml.safe_load((FIXTURE / "state.yaml").read_text(encoding="utf-8"))
        self.assertEqual([r["item"]["id"] for r in P.leaves(hidup)],
                         [r["item"]["id"] for r in P.leaves(beku)],
                         "fixture tes harus diperbarui bila roadmap berubah")


if __name__ == "__main__":
    unittest.main()
