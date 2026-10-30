# state/inbox/

Jalur **cadangan** untuk menyimpan progres tanpa Python (misalnya saat laptop bermasalah). Jalur utama tetap `Simpan Progres.bat`.

## Cara kerja

1. Pastikan file bukti sudah ada di repo GitHub (unggah lewat situs GitHub bila perlu).
2. Di situs GitHub, buka folder `state/inbox/` → **Add file** → **Create new file**.
3. Nama file: `<tanggal>-<resep>.yaml`, misalnya `2026-11-05-py-dasar.yaml`. Isi dengan Evidence Entry dari mentor, lalu **Commit changes** ke `main`.
4. Workflow GitHub (`.github/workflows/progres.yml`) memeriksa entri terhadap rubrik:
   - **Diterima**: `state.yaml` dan `dashboard.md` diperbarui otomatis, salinan entri disimpan di `state/evidence/`.
   - **Ditolak**: file dipindah ke `state/inbox/ditolak/` beserta `<nama>.alasan.txt`, dan tanda di tab **Actions** berwarna merah.
5. Setelah laptop normal kembali, jalankan `git pull` di folder repo sebelum bekerja lagi.

## Aturan

- Satu entri per file, `.yaml` atau `.yml`. Entri diproses berurutan menurut nama file.
- Jangan mengedit `state/state.yaml` atau `state/dashboard.md` langsung.
