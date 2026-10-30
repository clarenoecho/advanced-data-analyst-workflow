# Changelog

Setiap perubahan konstitusi, roadmap, kurikulum, rubrik, atau format dashboard dicatat di sini.

## 2026-10-30 — v1.1: Kompatibel dengan ChatGPT Free

- `PANDUAN.md` di akar repo: panduan lengkap untuk Tasya (setup, ChatGPT Project, belajar harian, simpan progres, membaca dashboard, tips Free, solusi masalah, kamus istilah).

- Paket ChatGPT Project dikurangi menjadi 3 file (rubrik digabung ke `aturan_mentor.md`) supaya muat di kuota unggah Free (sekitar 3 file per hari, 5 file per Project). Instruksi inti ditaruh di awal `aturan_mentor.md` sebagai cadangan kolom Instructions.
- Bagian baru "Mode hemat ChatGPT Free" di protokol mentor: kode dan output ditempel sebagai teks, chat baru setiap resep, jawaban panjang dipecah dengan command `teruskan`, ujian dinilai per soal secara tertulis.
- Alat baru `Salin Dashboard.bat` untuk menempelkan progres bila mentor gagal membuka GitHub.
- Semua alat kurikulum dipastikan gratis: Excel untuk web (Power Query cadangan di Power BI Desktop), AI visual Power BI Desktop (Copilot hanya konsep), Gemini API tingkat gratis untuk Fase 7 (hanya data publik/contoh).

## 2026-10-30 — v1.0: Dapur Data dibuat

- Sistem dibuat untuk Tasya, mengadaptasi mesin progres berbasis bukti dari sistem belajar "Learn AI Workflow".
- Roadmap 8 fase (0–7) Advanced Data Analyst disusun dari riset lowongan dan sertifikasi (lihat `docs/sumber_riset.md`).
- Empat status (Learned, Validated, Retained, Mastered); tidak ada status legacy karena semua dimulai dari nol.
- Tema dapur: resep, mencicip, pangkat brigade dapur dari Trainee Dapur sampai Head Chef.
- Command baru `ujian` dan `bingung`; command `prepare commit` dan `commit progres` diganti satu langkah Simpan Progres.
- Resep opsional boleh divalidasi tanpa menggeser resep aktif.
- Setup pertama kali dengan satu klik (`Setup Awal.bat`).
