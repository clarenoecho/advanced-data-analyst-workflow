# 🍳 Dapur Data: Advanced Data Analyst

> Sistem belajar mandiri **Tasya** untuk menjadi **Advanced Data Analyst**: dari Python dasar sampai SQL lanjut, statistik, business analytics, Power BI, dan AI, dengan bukti di setiap langkah.
>
> 💸 **100% gratis**: mentor berjalan di ChatGPT Free, dan semua alat praktik punya versi gratis.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📍 Progres saat ini

Lihat dashboard yang dibuat otomatis dari state: [`state/dashboard.md`](state/dashboard.md).

## 📖 Tentang

Repo ini adalah **sumber kebenaran** sebuah sistem belajar yang dijalankan bersama mentor AI (ChatGPT Project). Mentor mengajar dan menguji; progres dicatat di file, bukan di ingatan AI, dan hanya berubah lewat bukti yang lolos pemeriksaan script.

Temanya **dapur**: setiap fase adalah satu bagian dapur, setiap materi adalah satu **resep**, ujian adalah **mencicip**, dan setiap fase yang lulus menaikkan **pangkat**, dari Trainee Dapur sampai **Head Chef**.

## ⚙️ Cara kerja

```text
Belajar & ujian bersama mentor AI
        ↓
Mentor menyerahkan Evidence Entry (bukti, satu blok YAML)
        ↓
Salin → klik dua kali "Simpan Progres.bat"
        ↓
tools/progress.py memeriksa terhadap rubrik → state.yaml + dashboard diperbarui → push ke GitHub
        ↓
Mentor membaca progres terbaru langsung dari GitHub
```

## 🗺️ Roadmap: 8 fase

| Fase | Isi | Portfolio |
|---|---|---|
| 🥚 0 | Python Dasar | Buku Resep Digital (CLI) |
| 🥕 1 | Pandas & Visualisasi Dasar | Laporan EDA |
| 🔪 2 | Advanced SQL & Data Modeling | Studi Kasus SQL |
| 🍲 3 | Data Wrangling & Otomasi | Pipeline Data End-to-End |
| ⚖️ 4 | Statistik untuk Analis | Analisis A/B Test |
| 🛒 5 | Business & Product Analytics | Studi Kasus E-commerce |
| 🍽️ 6 | BI & Data Storytelling | Dashboard Power BI |
| ✨ 7 | AI-Augmented Analytics | Capstone End-to-End |

Rinciannya di [`system/02_roadmap.md`](system/02_roadmap.md) dan [`system/09_kurikulum.md`](system/09_kurikulum.md).

## 🏅 Status resep

🥄 Siap Dicicip (Learned) → 🍽️ Tersaji (Validated) → 📖 Resep Hafal (Retained) → ⭐ Signature Dish (Mastered). Syaratnya di [`system/03_rubrik_validasi.md`](system/03_rubrik_validasi.md).

## 🚀 Mulai

> 📘 **Tasya, mulai dari [`PANDUAN.md`](PANDUAN.md)**: panduan lengkap dari nol sampai belajar sehari-hari.

1. Ikuti [`docs/panduan_mulai.md`](docs/panduan_mulai.md): pasang Python, Git, dan VS Code, lalu klik dua kali **`Setup Awal.bat`**.
2. Siapkan mentor di ChatGPT: [`docs/panduan_chatgpt_project.md`](docs/panduan_chatgpt_project.md).
3. Di ChatGPT Project, ketik `cek progres`, lalu `lanjut`.

## 📂 Struktur

```text
advanced-data-analyst-workflow/
├── PANDUAN.md           panduan lengkap untuk Tasya
├── Setup Awal.bat       dijalankan sekali di awal
├── Simpan Progres.bat   dijalankan setiap selesai ujian
├── Salin Dashboard.bat  salin progres ke clipboard bila mentor tidak bisa membuka GitHub
├── system/              aturan sistem (diunggah ke ChatGPT Project)
├── state/               state.yaml · dashboard.md · evidence/
├── latihan/             notebook dan file latihan per fase
├── portfolio/           proyek portfolio, satu folder per proyek
├── data/                dataset bersama
├── tools/               progress.py, simpan.py, dan script pendukung
├── tests/               tes otomatis
└── docs/                panduan, sumber riset, changelog
```

## 🛠️ Perintah (untuk yang suka terminal)

```powershell
python tools\simpan.py                # sama dengan klik dua kali Simpan Progres.bat
python tools\progress.py check        # periksa konsistensi state
python tools\progress.py dashboard    # tampilkan dashboard
python tools\progress.py due          # review yang jatuh tempo
python -m unittest discover -s tests  # jalankan tes
```

## 📜 Lisensi

MIT. Lihat [`LICENSE`](LICENSE).
