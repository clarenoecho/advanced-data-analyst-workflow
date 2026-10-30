#!/usr/bin/env python3
"""setup_awal.py - menyiapkan repo Dapur Data di laptop untuk pertama kali.

Cukup dijalankan SEKALI (klik dua kali "Setup Awal.bat"). Yang dikerjakan:
    1. Memeriksa Python dan Git
    2. Memasang paket yang dibutuhkan tools (PyYAML) dan kernel Jupyter
    3. Menanyakan username GitHub, lalu mengisinya ke semua dokumen (tools/atur_github.py)
    4. Menyiapkan identitas Git (nama dan email) bila belum ada
    5. Membuat repo Git lokal, commit pertama, lalu push ke GitHub
    6. Membangun paket aturan untuk ChatGPT Project (folder paket_project/)

Sebelumnya, buat repo KOSONG bernama advanced-data-analyst-workflow di GitHub
(Public, tanpa README). Lihat docs/panduan_mulai.md.

Aman dijalankan ulang: langkah yang sudah selesai dilewati.
"""
from __future__ import annotations

import argparse
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

NAMA_REPO = "advanced-data-analyst-workflow"
HERE = Path(__file__).resolve().parent


def muat(nama):
    spec = importlib.util.spec_from_file_location(nama, HERE / f"{nama}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Gagal(Exception):
    pass


def jalan(cmd, cwd, cek=True):
    try:
        r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace")
    except OSError:
        raise Gagal(f"Perintah tidak ditemukan: {cmd[0]}")
    if cek and r.returncode != 0:
        raise Gagal(f"{' '.join(cmd)} gagal:\n{(r.stderr or r.stdout).strip()}")
    return r


def git(root, *args, cek=True):
    return jalan(["git", *args], root, cek=cek)


def tanya(teks, tanya_fn=input):
    while True:
        jawab = tanya_fn(teks).strip()
        if jawab:
            return jawab


def proses(root: Path, username: str | None, *, pasang=True, push=True, tanya_fn=input) -> int:
    root = Path(root).resolve()
    ag = muat("atur_github")

    # 1. Python dan Git
    if sys.version_info < (3, 9):
        raise Gagal("Butuh Python 3.9 atau lebih baru.")
    if shutil.which("git") is None:
        raise Gagal("Git belum terpasang. Pasang dari https://git-scm.com/download/win lalu jalankan lagi.")
    print(f"1/6 Python {sys.version.split()[0]} dan {git(root, '--version').stdout.strip()} siap")

    # 2. paket
    if pasang:
        jalan([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt", "ipykernel"], root)
        print("2/6 PyYAML dan kernel Jupyter terpasang")
    else:
        print("2/6 Pemasangan paket dilewati")

    # 3. username GitHub
    if not username:
        username = tanya("    Username GitHub kamu (contoh: tasya-data): ", tanya_fn)
    if not ag.USERNAME.match(username):
        raise Gagal(f"'{username}' bukan username GitHub yang sah.")
    terisi = [p for p in ag.sasaran(root) if ag.PENANDA in p.read_text(encoding="utf-8")]
    if terisi:
        for p in terisi:
            p.write_text(p.read_text(encoding="utf-8").replace(ag.PENANDA, username), encoding="utf-8", newline="\n")
        print(f"3/6 Username '{username}' diisi ke {len(terisi)} dokumen")
    else:
        print("3/6 Username sudah terisi sebelumnya")

    # 4. identitas Git
    if not git(root, "config", "user.name", cek=False).stdout.strip():
        nama = tanya("    Nama untuk riwayat Git (contoh: Tasya): ", tanya_fn)
        git(root, "config", "--global", "user.name", nama)
    if not git(root, "config", "user.email", cek=False).stdout.strip():
        email = tanya("    Email akun GitHub kamu: ", tanya_fn)
        git(root, "config", "--global", "user.email", email)
    print("4/6 Identitas Git siap")

    # 5. repo lokal, commit pertama, push
    if not (root / ".git").exists():
        git(root, "init", "-b", "main")
    git(root, "add", "-A")
    if git(root, "diff", "--cached", "--quiet", cek=False).returncode != 0:
        git(root, "commit", "-m", "awal: Dapur Data siap dipakai")
    url = f"https://github.com/{username}/{NAMA_REPO}.git"
    if git(root, "remote", "get-url", "origin", cek=False).returncode != 0:
        git(root, "remote", "add", "origin", url)
    if push:
        print("5/6 Mengirim ke GitHub... (bila muncul jendela login GitHub, masuk dengan akunmu)")
        try:
            git(root, "push", "-u", "origin", "main")
        except Gagal as x:
            raise Gagal(f"{x}\n\nPastikan repo KOSONG '{NAMA_REPO}' sudah dibuat di akun GitHub '{username}' "
                        "dan kamu sudah login, lalu jalankan Setup Awal lagi.")
        print(f"    Terkirim: https://github.com/{username}/{NAMA_REPO}")
    else:
        print("5/6 Commit lokal dibuat (push dilewati)")

    # 6. paket ChatGPT Project
    muat("bangun_paket").main(["--root", str(root)])
    print("6/6 Paket aturan untuk ChatGPT Project ada di folder paket_project/")
    print("\n✅ Setup selesai. Langkah berikutnya: siapkan ChatGPT Project (docs/panduan_chatgpt_project.md).")
    return 0


def main(argv=None) -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="Setup awal repo Dapur Data")
    ap.add_argument("--username", default=None)
    ap.add_argument("--root", default=str(HERE.parent))
    ap.add_argument("--tanpa-pasang", action="store_true")
    ap.add_argument("--tanpa-push", action="store_true")
    a = ap.parse_args(argv)
    try:
        return proses(Path(a.root), a.username, pasang=not a.tanpa_pasang, push=not a.tanpa_push)
    except Gagal as x:
        print(f"\n❌ {x}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
