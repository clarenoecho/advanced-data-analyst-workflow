#!/usr/bin/env python3
"""Isi username GitHub pemilik repo ke semua dokumen, cukup sekali setelah repo dibuat.

Mentor AI membaca progres dari alamat GitHub repo ini. Dokumen di system/, docs/, dan
README memakai penanda <USERNAME_GITHUB>; script ini menggantinya dengan username asli.

Pemakaian (dari folder repo):
    python tools\\atur_github.py tasya-contoh
    python tools\\atur_github.py tasya-contoh --dry     tampilkan file yang akan diubah saja
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PENANDA = "<USERNAME_GITHUB>"
FOLDER = ["system", "docs", "state/inbox"]
BERKAS = ["README.md", "PANDUAN.md"]
USERNAME = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$")  # aturan username GitHub


def sasaran(root: Path):
    out = [root / b for b in BERKAS if (root / b).is_file()]
    for f in FOLDER:
        if (root / f).is_dir():
            out += sorted((root / f).rglob("*.md"))
    return out


def main(argv=None) -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="Isi username GitHub ke dokumen sistem")
    ap.add_argument("username")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args(argv)

    if not USERNAME.match(a.username):
        print(f"❌ '{a.username}' bukan username GitHub yang sah (huruf, angka, dan '-' saja).")
        return 1
    root = Path(a.root)
    diubah = []
    for p in sasaran(root):
        teks = p.read_text(encoding="utf-8")
        if PENANDA in teks:
            diubah.append(p.relative_to(root).as_posix())
            if not a.dry:
                p.write_text(teks.replace(PENANDA, a.username), encoding="utf-8", newline="\n")
    if not diubah:
        print("Tidak ada penanda yang perlu diganti (sudah diisi sebelumnya?).")
        return 0
    print(("Akan diubah" if a.dry else "✅ Diisi") + f" ({len(diubah)} file):")
    for d in diubah:
        print("  -", d)
    if not a.dry:
        print("\nLangkah berikutnya: commit dan push, lalu bangun ulang paket: python tools\\bangun_paket.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
