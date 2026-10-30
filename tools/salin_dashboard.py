#!/usr/bin/env python3
"""Salin isi state/dashboard.md ke clipboard, untuk ditempel ke chat mentor.

Dipakai bila mentor (terutama di ChatGPT Free) tidak bisa membuka GitHub.
Klik dua kali "Salin Dashboard.bat", lalu tempel (Ctrl+V) di chat dengan pesan "cek progres".
Tidak memakai kuota unggah file karena yang dikirim berupa teks.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def teks_dashboard(root: Path) -> str:
    p = root / "state" / "dashboard.md"
    if not p.is_file():
        raise FileNotFoundError("state/dashboard.md tidak ditemukan. Jalankan: python tools\\progress.py dashboard --tulis")
    isi = p.read_text(encoding="utf-8")
    # buang komentar HTML di baris pertama; sisanya dikirim apa adanya
    baris = [b for b in isi.splitlines() if not b.startswith("<!--")]
    return "cek progres (dashboard ditempel karena GitHub tidak bisa dibuka):\n\n" + "\n".join(baris).strip() + "\n"


def ke_clipboard(teks: str) -> bool:
    if not sys.platform.startswith("win"):
        return False
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write(teks)
        nama = f.name
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command",
                            f"Get-Content -Raw -Encoding UTF8 -LiteralPath '{nama}' | Set-Clipboard"],
                           capture_output=True)
        return r.returncode == 0
    except OSError:
        return False
    finally:
        Path(nama).unlink(missing_ok=True)


def main(argv=None) -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="Salin dashboard ke clipboard")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    a = ap.parse_args(argv)
    try:
        teks = teks_dashboard(Path(a.root))
    except FileNotFoundError as x:
        print(f"❌ {x}")
        return 1
    if ke_clipboard(teks):
        print("✅ Dashboard disalin. Buka chat mentor lalu tekan Ctrl+V dan Enter.")
    else:
        print("Clipboard tidak tersedia; salin teks di bawah ini secara manual:\n")
        print(teks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
