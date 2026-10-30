---
dokumen: roadmap
versi: 1.0
tanggal: 2026-10-30
peran: Sumber kebenaran materi dan urutan belajar. Rincian isi tiap resep ada di system/09_kurikulum.md.
---

# 🍳 Roadmap Dapur Data: Advanced Data Analyst

> **Target:** menjadi **Advanced Data Analyst**, yaitu analis yang mampu bergerak dari pertanyaan bisnis sampai rekomendasi: mengambil data dengan SQL, merapikannya dengan Python, menilainya dengan statistik, menyajikannya lewat dashboard, dan memakai AI dengan kritis.

## Dasar penyusunan

Roadmap ini disusun dari riset pada 2026-10-30:

- **Permintaan lowongan.** SQL muncul di sekitar 53–60% lowongan Data Analyst, Python 31–41%, Power BI 29–43%, Tableau 2–26%, dan Excel di sekitar separuh sampai 81% lowongan (riset 365 Data Science atas 855 lowongan AS dan AccioJob atas 328 lowongan).
- **Lowongan analis senior** meminta SQL tingkat lanjut (window function, optimasi, BigQuery), dbt dan star schema, A/B testing, analisis funnel, cohort, dan retensi, serta kemampuan menerjemahkan data menjadi rekomendasi bisnis.
- **Google Advanced Data Analytics Certificate**: EDA, statistik, regresi linier dan logistik, dasar machine learning, capstone.
- **Ujian Microsoft PL-300 (Power BI Data Analyst, April 2026)**: menyiapkan data, data modeling dan DAX, visualisasi dan storytelling, mengelola dan mengamankan konten.
- **Tren AI**: AI mampu menulis query dan dashboard tetapi sering keliru dengan yakin, sehingga analis dinilai dari kemampuan merumuskan masalah, menilai secara statistik, dan memverifikasi hasil AI.

Sumber lengkapnya ada di `docs/sumber_riset.md`.

## Prinsip urutan

1. **Fondasi dulu.** Python dan Pandas (Fase 0–1) menjadi alat kerja untuk semua fase berikutnya.
2. **SQL sebelum wrangling lanjut.** Di dunia kerja data diambil dari database lebih dulu.
3. **Statistik sebelum business analytics.** Funnel, cohort, dan A/B test hanya bermakna bila Tasya bisa menilai apakah perbedaan itu nyata.
4. **BI setelah analisis.** Dashboard menyajikan analisis yang benar, bukan menggantikannya.
5. **AI di akhir, bukan di awal.** AI dipakai paling efektif oleh orang yang bisa memeriksa hasilnya.
6. Machine learning **tidak** menjadi fase sendiri. Regresi masuk Fase 4, sedangkan clustering dan forecasting masuk Fase 5 sebagai alat analis.
7. **Semuanya gratis.** Mentor berjalan di ChatGPT Free, dan setiap alat praktik punya versi gratis: Python dan library-nya, SQLite, PostgreSQL, BigQuery Sandbox, dbt Core, Excel untuk web, Power BI Desktop, dan Gemini API tingkat gratis. Fitur berbayar hanya dipelajari sebagai konsep.

## Pangkat

Setiap fase yang lulus menaikkan pangkat di dashboard:

| Fase selesai | Pangkat |
|---|---|
| belum ada | Trainee Dapur |
| 0 | Commis Chef |
| 0–1 | Demi Chef de Partie |
| 0–2 | Chef de Partie |
| 0–3 | Senior Chef de Partie |
| 0–4 | Sous Chef |
| 0–5 | Executive Sous Chef |
| 0–6 | Chef de Cuisine |
| 0–7 | Head Chef (Advanced Data Analyst) |

---

# 🥚 FASE 0 — PYTHON DASAR

**Tujuan:** menulis program Python kecil dengan percaya diri, bekerja di Jupyter, dan menyimpan pekerjaan di GitHub.

- Setup: Python, VS Code, Jupyter
- Variabel, tipe data, operator
- Percabangan dan perulangan
- List, tuple, dictionary, set
- Fungsi dan modul
- Error handling dan file I/O
- Virtual environment, pip, Git & GitHub
- OOP dasar *(opsional)*
- 🎁 **Mini Project: Buku Resep Digital (CLI)**

# 🥕 FASE 1 — PANDAS & VISUALISASI DASAR

**Tujuan:** memuat, membersihkan, meringkas, dan memvisualisasikan dataset tabular, lalu menuliskan temuan dalam laporan EDA.

- NumPy esensial
- Pandas: membaca data, seleksi dan filter, cleaning dasar, groupby, merge dan reshape
- Matplotlib: grafik dasar, figure dan axes
- Seaborn: distribusi, kategori, relasi, heatmap, pairplot
- 🎁 **Portfolio #1: Laporan EDA** dataset publik

# 🔪 FASE 2 — ADVANCED SQL & DATA MODELING

**Tujuan:** menjawab pertanyaan bisnis langsung dari database dengan SQL yang benar, rapi, dan efisien, serta memahami bagaimana data dimodelkan.

- Fondasi SQL: SELECT, filter, agregasi, CASE WHEN, JOIN, subquery, CTE
- SQL lanjut: window function (ranking, running total, LAG/LEAD), fungsi tanggal dan teks, NULL, optimasi query
- Platform: PostgreSQL (dan koneksi dari Python), BigQuery Sandbox
- Data modeling: model relasional, normalisasi, ERD, star schema
- 🎁 **Portfolio #2: Studi Kasus SQL**

# 🍲 FASE 3 — DATA WRANGLING & OTOMASI

**Tujuan:** mengubah data mentah yang berantakan menjadi tabel siap analisis secara otomatis dan bisa diulang.

- Pandas lanjut: method chaining, datetime dan time series, teks dan kategori, performa dan Parquet
- Data quality: profiling, aturan validasi, outlier, duplikat, standardisasi
- ETL: mengambil data dari API, pipeline ETL dengan Python, dasar dbt
- Otomasi: script dan penjadwalan, laporan Excel otomatis
- 🎁 **Portfolio #3: Pipeline Data End-to-End**

# ⚖️ FASE 4 — STATISTIK UNTUK ANALIS

**Tujuan:** membedakan sinyal dari kebetulan, merancang dan menganalisis eksperimen, dan menjelaskan hubungan antarvariabel.

- Statistik deskriptif, probabilitas dan distribusi, sampling dan confidence interval
- Uji hipotesis: konsep dan p-value, t-test, chi-square, ANOVA
- A/B testing: desain eksperimen, sample size, analisis, jebakan umum
- Regresi linier dan logistik
- Korelasi vs kausalitas
- 🎁 **Portfolio #4: Analisis A/B Test**

# 🛒 FASE 5 — BUSINESS & PRODUCT ANALYTICS

**Tujuan:** menerjemahkan pertanyaan bisnis menjadi metrik dan analisis, lalu menghasilkan rekomendasi yang bisa dijalankan.

- Merumuskan masalah bisnis, metrik dan KPI
- Analisis funnel, cohort, retensi, churn
- Segmentasi: RFM dan K-Means
- CLV dan unit economics
- Forecasting dasar
- 🎁 **Portfolio #5: Studi Kasus E-commerce**

# 🍽️ FASE 6 — BI & DATA STORYTELLING

**Tujuan:** membangun dashboard yang dipakai orang, dan menyampaikan insight yang membuat orang bertindak.

- Excel lanjut: formula lanjut, dynamic array, PivotTable, Power Query
- Power BI: Power Query dan data model, DAX dasar dan CALCULATE, time intelligence, report interaktif, publish dan keamanan
- Storytelling: prinsip desain dashboard, narasi insight dan presentasi
- 🎁 **Portfolio #6: Dashboard Power BI** beserta presentasi insight

Catatan alat: Power BI Desktop gratis dan berjalan di Windows. Power BI Service (publish, refresh, row-level security di cloud) butuh akun kerja atau sekolah; tanpa akun itu, resep `pbi_service` dipelajari konsepnya dan dipraktikkan di Power BI Desktop (lihat kurikulum).

# ✨ FASE 7 — AI-AUGMENTED ANALYTICS & CAPSTONE

**Tujuan:** memakai AI untuk mempercepat kerja analis tanpa kehilangan ketelitian.

- Prompting untuk SQL dan analisis
- Memverifikasi hasil AI
- AI di Excel dan Power BI
- Analisis teks dengan LLM API
- Otomasi narasi insight
- Privasi, etika, dan tata kelola data
- 🎂 **Capstone: Analisis End-to-End**, dari pertanyaan bisnis, SQL, wrangling, statistik, dashboard, sampai rekomendasi

---

## Aturan perubahan

Roadmap ini hanya berubah dengan persetujuan Tasya. Usulan perubahan dari mentor dilaporkan singkat di akhir sesi (lihat `system/08_penyajian_materi.md`), lalu dicatat di `docs/changelog.md` bila disetujui. Setiap perubahan roadmap juga harus diikuti `state/state.yaml` dan `system/09_kurikulum.md`; tes otomatis memeriksa keduanya tetap selaras.
