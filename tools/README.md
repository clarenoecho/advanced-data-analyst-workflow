# tools/

| Script | Fungsi |
|---|---|
| `progress.py` | Penjaga aturan progres. Satu-satunya yang mengubah `state/state.yaml` |
| `simpan.py` | Satu perintah simpan progres (dipanggil oleh `Simpan Progres.bat`) |
| `setup_awal.py` | Setup pertama kali (dipanggil oleh `Setup Awal.bat`) |
| `atur_github.py` | Mengisi username GitHub ke dokumen (sudah dijalankan oleh Setup Awal) |
| `bangun_paket.py` | Membuat folder `paket_project/` berisi 3 file aturan untuk ChatGPT Project (muat di batas ChatGPT Free) |
| `salin_dashboard.py` | Menyalin dashboard ke clipboard untuk ditempel ke chat (dipanggil oleh `Salin Dashboard.bat`) |

## progress.py

| Perintah | Fungsi |
|---|---|
| `python tools\progress.py check` | Periksa konsistensi state (satu resep aktif, tanpa lompatan, bukti ada, dashboard sinkron) |
| `python tools\progress.py dashboard [--tulis]` | Tampilkan dashboard; `--tulis` menyimpannya ke `state/dashboard.md` |
| `python tools\progress.py due` | Daftar review yang jatuh tempo |
| `python tools\progress.py learned <id>` | Tandai resep aktif sudah dipelajari, belum diuji |
| `python tools\progress.py apply <entri.yaml> [--dry]` | Terapkan Evidence Entry; `--dry` hanya simulasi |
| `python tools\progress.py inbox [--dry]` | Terapkan semua entri di `state/inbox/` (dijalankan workflow GitHub) |

Opsi global: `--root <folder repo>` dan `--today YYYY-MM-DD`. Aturannya di `system/03_rubrik_validasi.md`.

## simpan.py

| Perintah | Fungsi |
|---|---|
| `python tools\simpan.py` | Baca entri dari clipboard, `git pull`, simulasi rubrik, terapkan, `check`, satu commit (bukti + state), push, bangun ulang `paket_project/` |
| `... --dry` | Hanya periksa dan simulasi |
| `... --berkas <file.yaml>` | Baca entri dari berkas, bukan clipboard |
| `... --tanpa-push` | Commit lokal saja (saat tanpa internet) |
| `... --tanpa-git` | Terapkan ke file saja |
| `... --tanpa-paket` | Jangan membangun ulang `paket_project/` |

Aturan keselamatan: entri ditolak berarti tidak ada file yang berubah; bila `check` gagal setelah diterapkan, semua perubahan dikembalikan; hanya file state dan file di `bukti:` yang masuk ke commit.

## Tes

`python -m unittest discover -s tests -v`. Tes memakai state beku di `tests/fixtures/state/`; bila roadmap berubah, perbarui fixture itu juga (tes akan mengingatkan).
