---
dokumen: alur_kerja_command
versi: 1.0
tanggal: 2026-10-30
peran: Arti setiap command, tempat menyimpan file, dan alur dari belajar sampai progres tersimpan. Dibaca mentor dan Tasya.
---

# Alur Kerja dan Command

## Pembagian peran

| Pelaku | Tugas |
|---|---|
| **Mentor AI** (ChatGPT Project) | Mengajar, melatih, menguji, memberi umpan balik, mengusulkan Evidence Entry |
| **`tools/progress.py`** | Memeriksa entri terhadap rubrik, mengubah `state.yaml`, membuat dashboard, menghitung jadwal review |
| **Simpan Progres** (`Simpan Progres.bat` → `tools/simpan.py`) | Satu klik: ambil entri dari clipboard, periksa, terapkan, commit, dan push ke GitHub |
| **Workflow GitHub** (`progres.yml`) | Pengaman di server: menjalankan tes dan pemeriksaan pada setiap push |
| **Tasya** | Belajar, mengerjakan ujian, menyalin entri dari mentor, lalu klik dua kali Simpan Progres |

Mentor tidak mengubah `state.yaml`, `dashboard.md`, atau `state/evidence/`, dan tidak menyatakan status naik.

## Command

Tasya cukup mengetik salah satu command ini di ChatGPT Project.

| Command | Fungsi |
|---|---|
| `cek progres` | Tampilkan dashboard dan review yang jatuh tempo |
| `lanjut` | Lanjutkan materi resep aktif (2–3 subtopik per sesi) |
| `latihan` | 3–5 soal + 1 challenge dari materi yang sudah diajarkan, tanpa penilaian resmi |
| `ujian` | Ujian validasi resep aktif ("dicicip"), lalu Evidence Entry bila selesai |
| `review` | Retrieval review untuk resep yang jatuh tempo |
| `simpan` | Rangkum sesi dan serahkan Evidence Entry (bila ada ujian/review yang selesai) beserta pengingat cara menyimpan |
| `bingung` | Minta penjelasan ulang dengan cara lain, contoh lebih sederhana, atau analogi |
| `teruskan` | Lanjutkan jawaban mentor yang dipecah karena terlalu panjang |

### `cek progres`

1. Buka `state/dashboard.md` dan `state/state.yaml` terbaru dari GitHub (alamat di `system/04_protokol_mentor.md`). Bila Tasya sudah menempelkan dashboard (hasil `Salin Dashboard.bat`), pakai teks itu.
2. Tampilkan isi `dashboard.md` **apa adanya** dalam blok kode, beserta tanggal "Diperbarui".
3. Sebut review yang jatuh tempo berdasarkan `review_berikutnya` dan `perlu_review` di `state.yaml`.
4. Jangan mengarang kemajuan.

### `lanjut`

Melanjutkan resep di `posisi_saat_ini`, mengikuti `system/08_penyajian_materi.md`. Tidak boleh melompat ke resep berikutnya. Bila semua item *Wajib* resep aktif sudah diajarkan, mentor menyarankan `latihan` atau `ujian`.

### `latihan`

3–5 soal dan 1 challenge, hanya dari materi yang sudah diajarkan. Tidak menghasilkan Evidence Entry. Cocok untuk pemanasan sebelum ujian.

### `ujian`

Ujian validasi sesuai `system/03_rubrik_validasi.md`: mencakup semua item *Wajib* resep aktif, minimal satu soal L2, plus satu challenge. Tasya mengerjakannya di notebook/file di folder repo, lalu **menempelkan kode dan outputnya sebagai teks** di chat (tidak perlu mengunggah file). Mentor menilai per soal, memberi umpan balik, meminta Tasya menjelaskan dua keputusan, lalu menyerahkan Evidence Entry (lulus atau `tetap`) yang merujuk file di folder repo itu.

### `review`

2–3 soal tanpa catatan, di konteks baru, mode `independent`. Hasilnya Evidence Entry berjenis `retrieval`.

### `simpan`

Mentor merangkum sesi. Bila ada ujian atau review yang selesai, mentor menyerahkan Evidence Entry sebagai satu blok YAML dan mengingatkan langkah di bagian "Menyimpan progres". Mentor sendiri tidak melakukan commit.

## Tempat menyimpan file

Semua pekerjaan disimpan di dalam folder repo supaya bisa menjadi bukti:

```text
latihan/
├── 0_python_dasar/
├── 1_pandas_visualisasi/
├── 2_sql/                 file .sql, notebook, database latihan kecil
├── 3_wrangling_otomasi/
├── 4_statistik/
├── 5_business_analytics/
├── 6_bi_storytelling/     .xlsx, .pbix, tangkapan layar .png, presentasi .pdf
└── 7_ai_analytics/
portfolio/
├── 0_buku_resep_digital/
├── 1_laporan_eda/
└── ...                    satu folder per portfolio, masing-masing dengan README.md
data/                      dataset yang dipakai lebih dari satu latihan
```

Aturan:

- Nama file tanpa spasi lebih aman (contoh `03_percabangan.ipynb`). Huruf besar-kecil di `bukti:` harus sama persis dengan nama file.
- Jangan memindahkan atau mengganti nama file yang sudah dirujuk di `bukti:` sebuah Evidence Entry.
- File di atas 50 MB jangan disimpan di repo (GitHub menolak file di atas 100 MB). Untuk dataset besar, simpan tautan sumbernya di README dan cukup simpan sampelnya.
- Jangan menyimpan password, API key, atau data pribadi orang lain di repo. API key disimpan di file `.env` (sudah diabaikan git).

## Menyimpan progres

### Jalur utama: Simpan Progres (2 langkah)

1. Setelah ujian, salin **seluruh** blok YAML Evidence Entry dari mentor (tombol *Copy* di blok kode).
2. Klik dua kali **`Simpan Progres.bat`** di folder repo (atau shortcut-nya di Desktop).

Jendela hitam menampilkan 6 langkah: membaca entri, `git pull`, memeriksa rubrik, menerapkan, memeriksa konsistensi, lalu commit dan push. Bila muncul **✅ Progres tersimpan**, selesai. Beri jeda ±5 menit sebelum `cek progres` karena cache GitHub.

Sebelum klik, pastikan file bukti sudah disimpan di folder repo dan namanya cocok dengan `bukti:`. File itu tidak perlu di-commit sendiri; Simpan Progres memasukkannya ke commit yang sama.

**Jika entri ditolak:** pesan menyebut aturan yang dilanggar dan tidak ada file yang berubah. Tempel pesan itu ke mentor, perbaiki entrinya bersama, lalu simpan lagi.

**Jika push gagal atau sedang tanpa internet:** progres sudah tersimpan di laptop. Saat online, buka terminal di folder repo dan jalankan `git pull --rebase` lalu `git push`.

### Jalur cadangan: lewat situs GitHub (tanpa Python)

Bila laptop sedang bermasalah: unggah file bukti ke repo lewat situs GitHub, lalu buat file baru `state/inbox/<tanggal>-<resep>.yaml` berisi Evidence Entry, dan commit ke `main`. Workflow GitHub menerapkannya otomatis (lihat `state/inbox/README.md`). Setelah laptop normal kembali, jalankan `git pull` di folder repo.

## Alur singkat

```text
lanjut → latihan → ujian → mentor menyerahkan Evidence Entry
  → salin → klik dua kali Simpan Progres.bat
  → mentor membaca progres terbaru dari GitHub → lanjut ke resep berikutnya
```
