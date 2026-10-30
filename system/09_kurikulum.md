---
dokumen: kurikulum
versi: 1.0
tanggal: 2026-10-30
peran: Rincian setiap resep roadmap beserta konsep wajib. Dipakai mentor untuk menyajikan materi, menyusun ujian, dan retrieval review.
otoritas: Di bawah roadmap (system/02_roadmap.md). Roadmap menentukan fase dan urutan; kurikulum merinci isi setiap resep.
---

# Kurikulum Dapur Data: Advanced Data Analyst

## Cara memakai

- Setiap resep punya **id** yang sama persis dengan id di `state/state.yaml`. Kolom `modul` di Evidence Entry diisi id ini.
- **Wajib** adalah daftar konsep yang harus diajarkan (`lanjut`) dan **semuanya** diujikan saat validasi (`ujian`). Ujian yang hanya mencakup sebagian daftar tidak boleh memvalidasi resep.
- **Fokus ujian** memberi arah soal dan challenge sesuai `system/03_rubrik_validasi.md`.
- **Alat** menyebut software yang dipakai di resep itu. **Semua alat di kurikulum ini gratis**, termasuk mentornya (ChatGPT Free). Fitur yang butuh langganan (Copilot, Power BI Service) hanya dipelajari sebagai konsep, dengan alternatif gratis untuk praktiknya.
- Setelah resep Validated, daftar wajibnya menjadi **cakupan retrieval review**.
- Kurikulum hanya berubah dengan persetujuan Tasya, dicatat di `docs/changelog.md`.

---

# 🥚 FASE 0 — PYTHON DASAR

#### `py_setup` — Setup: Python, VS Code & Jupyter
- **Alat:** Python 3.12+ dari python.org, VS Code + ekstensi Python & Jupyter, Git
- **Wajib:** apa itu Python dan kenapa dipakai analis; memasang Python (centang *Add python.exe to PATH*), VS Code, dan ekstensi; terminal dasar (`cd`, `dir`, `python --version`); menjalankan file `.py`; membuat dan menjalankan notebook `.ipynb`; sel kode vs sel markdown; menulis markdown dasar (judul, daftar, tebal); `print()` dan komentar `#`; struktur folder repo ini (`latihan/`, `portfolio/`) dan cara menyimpan file di sana
- **Fokus ujian:** membuat notebook di `latihan/0_python_dasar/` yang berisi sel markdown penjelasan dan sel kode yang berjalan; menjelaskan beda file `.py` dan notebook

#### `py_dasar` — Variabel, Tipe Data & Operator
- **Wajib:** variabel dan aturan penamaan; tipe `int`, `float`, `str`, `bool`, `None`; `type()`; konversi (`int()`, `float()`, `str()`); operator aritmatika (`+ - * / // % **`); operator perbandingan; operator logika (`and`, `or`, `not`); `input()`; f-string dan format angka (`f"{x:,.2f}"`); method string (`upper`, `lower`, `strip`, `split`, `join`, `replace`); indexing dan slicing string
- **Fokus ujian:** program kecil yang menerima input, menghitung, dan menampilkan hasil rapi (misalnya kalkulator total belanja dengan diskon)

#### `py_kontrol` — Percabangan & Perulangan
- **Wajib:** `if/elif/else`; kondisi bersarang; `for` dengan `range()` dan dengan list; `while`; `break`, `continue`; akumulator (menjumlahkan/menghitung dalam loop); `enumerate()`; `zip()`
- **Fokus ujian:** memproses daftar data dengan aturan bercabang (misalnya mengkategorikan nilai transaksi)

#### `py_struktur_data` — List, Tuple, Dictionary & Set
- **Wajib:** list (`append`, `extend`, `insert`, `remove`, `pop`, `sort`/`sorted`, slicing); tuple dan unpacking; dict (`keys`, `values`, `items`, `get`, `update`, iterasi); set (`add`, union, intersection, difference); list comprehension dan dict comprehension; struktur bersarang (list of dict)
- **Fokus ujian:** memilih struktur data yang tepat; mengolah list of dict (misalnya daftar pesanan) menjadi ringkasan

#### `py_fungsi_modul` — Fungsi & Modul
- **Wajib:** `def`, `return`; parameter default dan keyword argument; `*args`, `**kwargs`; scope lokal/global; `lambda`; docstring; `import`, `from ... import`, `as`; membuat modul sendiri; `if __name__ == "__main__":`; standard library `math`, `random`, `datetime`
- **Fokus ujian:** memecah program menjadi fungsi kecil yang bisa dipakai ulang

#### `py_error_file` — Error Handling & File I/O
- **Wajib:** membaca traceback; `try/except/else/finally`; exception umum (`ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`); `raise`; `open()` dengan mode `r/w/a` dan `with`; `encoding="utf-8"`; `pathlib.Path`; modul `csv` (`reader`, `DictReader`, `writer`); modul `json` (`load`, `dump`)
- **Fokus ujian:** membaca file CSV, menangani baris rusak tanpa program berhenti, dan menyimpan hasilnya ke JSON

#### `py_venv_git` — Virtual Environment, pip, Git & GitHub
- **Wajib:** `python -m venv .venv`, aktivasi di Windows, memilih kernel venv di VS Code; `pip install`, `pip list`, `pip freeze`, `requirements.txt`, `pip install -r`; konsep Git (repo, commit, riwayat); `git status`, `add`, `commit`, `push`, `pull`, `log`; `.gitignore`; GitHub (repo, README, melihat riwayat commit); menulis README dasar dengan markdown
- **Fokus ujian:** menyiapkan environment proyek kecil yang bisa diulang di laptop lain, lalu commit dan push ke GitHub

#### `py_oop` — OOP Dasar *(opsional)*
- **Wajib:** `class`, `__init__`, `self`; atribut dan method; atribut kelas vs instance; `__str__`; inheritance dan `super()`
- **Fokus ujian:** memodelkan objek sederhana (misalnya `Resep` dengan daftar bahan dan method menghitung porsi)

#### `porto_0` — Mini Project: Buku Resep Digital (CLI)
- **Wajib:** program menu di terminal untuk menambah, mencari, menampilkan, dan menghapus resep; data disimpan ke file JSON; minimal 4 fungsi terpisah; error handling untuk input salah; ringkasan sederhana (misalnya jumlah resep per kategori); repo/folder `portfolio/0_buku_resep_digital/` dengan README berisi cara pakai, contoh tampilan, dan dua keputusan desain beserta alasannya
- **Fokus ujian:** program berjalan tanpa crash pada input salah; README jelas; refleksi keputusan dan keterbatasan

---

# 🥕 FASE 1 — PANDAS & VISUALISASI DASAR

#### `numpy_esensial` — NumPy Esensial
- **Alat:** NumPy, Jupyter
- **Wajib:** kenapa array lebih cepat dari list; `np.array`, `arange`, `linspace`, `zeros`, `ones`; `shape`, `ndim`, `dtype`; indexing, slicing, boolean indexing; operasi vektor dan broadcasting; agregasi dengan `axis` (`sum`, `mean`, `median`, `std`, `min`, `max`, `argmax`); `np.where`; `np.random.default_rng` dengan seed
- **Fokus ujian:** menjawab pertanyaan dari array 2D (misalnya penjualan per toko per bulan) memakai `axis` dan boolean indexing

#### `pd_dasar_io` — Series, DataFrame & Membaca Data
- **Alat:** pandas
- **Wajib:** `Series` dan `DataFrame`; membuat DataFrame dari dict; `read_csv` (parameter `sep`, `encoding`, `parse_dates`), `read_excel`, `read_json`; `to_csv`, `to_excel`; `head`, `tail`, `info`, `describe`, `shape`, `dtypes`, `columns`, `index`; `value_counts`, `nunique`
- **Fokus ujian:** memuat dataset publik dan menuliskan 5 fakta pertama tentang isinya

#### `pd_seleksi_filter` — Seleksi & Filtering
- **Wajib:** `df["kol"]`, `df[["a","b"]]`; `loc` dan `iloc`; filter dengan perbandingan; kondisi ganda `&`, `|`, `~`; `isin`, `between`, `str.contains`; `query`; `sort_values`, `nlargest`/`nsmallest`; membuat kolom baru dan `np.where`
- **Fokus ujian:** menjawab pertanyaan bisnis sederhana dengan filter dan sort (misalnya "10 pesanan terbesar dari kota X bulan lalu")

#### `pd_cleaning` — Data Cleaning Dasar
- **Wajib:** `isna().sum()`, `dropna`, `fillna` (nilai tetap, mean/median, `ffill`); `duplicated`, `drop_duplicates`; `astype`; `pd.to_datetime`, `pd.to_numeric(errors="coerce")`; `rename`, `drop`; merapikan teks (`str.strip`, `str.lower`, `str.replace`); `apply` dan `map`; mencatat keputusan cleaning
- **Fokus ujian:** membersihkan dataset kotor dan menjelaskan alasan setiap keputusan (hapus vs isi)

#### `pd_groupby_agg` — GroupBy & Agregasi
- **Wajib:** `groupby` satu dan beberapa kolom; `agg` dengan beberapa fungsi dan named aggregation; `size` vs `count`; `transform`; `reset_index`; `pivot_table`; `crosstab`; `pd.cut` untuk binning
- **Fokus ujian:** meringkas data transaksi per kategori/waktu dan menarik insight

#### `pd_gabung_reshape` — Merge, Concat & Reshape
- **Wajib:** `merge` (`inner`, `left`, `right`, `outer`; `on`, `left_on`/`right_on`; `indicator=True`); memeriksa duplikasi baris setelah merge; `concat`; `melt` (wide → long); `pivot` (long → wide); `set_index`/`reset_index`
- **Fokus ujian:** menggabungkan tabel pesanan, pelanggan, dan produk lalu menjawab pertanyaan lintas tabel

#### `mpl_dasar` — Matplotlib: Grafik Dasar
- **Alat:** Matplotlib
- **Wajib:** `plt.plot`, `bar`/`barh`, `hist`, `scatter`, `boxplot`; judul, label sumbu, legend; memilih grafik sesuai pertanyaan (tren, perbandingan, distribusi, hubungan); plotting langsung dari Pandas (`df.plot`)
- **Fokus ujian:** memilih jenis grafik yang tepat untuk 4 pertanyaan berbeda dan menjelaskan alasannya

#### `mpl_figure_axes` — Matplotlib: Figure, Axes & Styling
- **Wajib:** `fig, ax = plt.subplots()`; beberapa subplot (`nrows`, `ncols`, `figsize`); `ax.set_title`, `set_xlabel`, `set_ylim`; format tick angka/tanggal; anotasi (`ax.annotate`, `ax.text`); warna dan menonjolkan satu seri; `tight_layout`; `savefig` (`dpi`, `bbox_inches`)
- **Fokus ujian:** membuat satu figure multi-panel yang rapi dan menyimpannya sebagai PNG

#### `sns_distribusi_kategori` — Seaborn: Distribusi & Kategori
- **Alat:** seaborn
- **Wajib:** `histplot`, `kdeplot`, `boxplot`, `violinplot`; `countplot`, `barplot` (estimator dan error bar), `stripplot`; parameter `hue`, `order`; membandingkan distribusi antar kelompok
- **Fokus ujian:** membandingkan distribusi nilai antar kelompok dan menjelaskan apa yang terlihat

#### `sns_relasi_matrix` — Seaborn: Relasi, Heatmap & Pairplot
- **Wajib:** `scatterplot` dan `lineplot` dengan `hue`/`size`; `relplot` dan faceting (`col`, `row`); `regplot`; `heatmap` dari matriks korelasi (`annot`, `cmap`, `fmt`); `pairplot`; tema dan palet (`set_theme`, `palette`)
- **Fokus ujian:** menjelajahi hubungan antarvariabel dan menyatakan insight beserta keterbatasannya (korelasi ≠ sebab)

#### `porto_1` — Portfolio #1: Laporan EDA
- **Wajib:** dataset publik (misalnya Kaggle atau data.go.id) dengan minimal 1.000 baris; 3–5 pertanyaan analisis yang ditulis di awal; pemeriksaan kualitas data dan cleaning yang terdokumentasi; minimal 6 visualisasi yang menjawab pertanyaan; ringkasan insight dan rekomendasi; notebook rapi dengan markdown; `portfolio/1_laporan_eda/README.md` (tujuan, data, temuan utama, keterbatasan)
- **Fokus ujian:** setiap grafik menjawab pertanyaan; insight didukung data; keterbatasan disebut jujur

---

# 🔪 FASE 2 — ADVANCED SQL & DATA MODELING

#### `sql_select_filter` — SELECT, WHERE & ORDER BY
- **Alat:** SQLite (lewat Python `sqlite3` + Pandas `read_sql`, atau DB Browser for SQLite)
- **Wajib:** apa itu database relasional, tabel, baris, kolom, primary key; `SELECT`, alias `AS`, `DISTINCT`; `WHERE` dengan `=`, `<>`, `>`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`; `AND`/`OR` dan tanda kurung; `ORDER BY` (`ASC`/`DESC`, beberapa kolom); `LIMIT`; menjalankan query dari Python ke DataFrame
- **Fokus ujian:** menerjemahkan pertanyaan bisnis menjadi query filter yang benar

#### `sql_agregasi` — GROUP BY, HAVING & CASE WHEN
- **Wajib:** `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`; `COUNT(*)` vs `COUNT(kolom)` vs `COUNT(DISTINCT)`; `GROUP BY` satu dan beberapa kolom; `HAVING` vs `WHERE`; `CASE WHEN` untuk kategori dan untuk agregasi bersyarat (`SUM(CASE WHEN ...)`); urutan eksekusi logis query
- **Fokus ujian:** membuat ringkasan metrik per segmen, termasuk agregasi bersyarat

#### `sql_join` — JOIN & UNION
- **Wajib:** `INNER JOIN`, `LEFT JOIN` (dan kenapa `RIGHT`/`FULL` jarang dipakai); join beberapa tabel; self join; menemukan data tanpa pasangan (`LEFT JOIN ... WHERE kanan IS NULL`); jebakan baris berlipat (fan-out) dan cara memeriksanya; `UNION` vs `UNION ALL`
- **Fokus ujian:** menjawab pertanyaan lintas 3+ tabel dan memeriksa jumlah baris hasil join

#### `sql_subquery_cte` — Subquery & CTE
- **Wajib:** subquery di `WHERE` (`IN`, `EXISTS`), di `FROM`, dan scalar subquery; correlated subquery; `WITH` (CTE) satu dan beberapa tahap; memecah query panjang menjadi CTE yang terbaca; gaya penulisan SQL yang rapi
- **Fokus ujian:** menulis ulang query bertingkat menjadi CTE dan menjelaskan tiap tahap

#### `sql_window_ranking` — Window Function: Ranking
- **Wajib:** konsep window function vs `GROUP BY`; `OVER()`, `PARTITION BY`, `ORDER BY` di dalam window; `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`; pola top-N per kelompok; deduplikasi dengan `ROW_NUMBER`
- **Fokus ujian:** "3 produk terlaris per kategori" dan deduplikasi data ganda

#### `sql_window_analitik` — Window Function: Running Total, LAG & LEAD
- **Wajib:** `SUM/AVG/COUNT() OVER`; running total; window frame (`ROWS BETWEEN ... PRECEDING AND CURRENT ROW`); moving average; `LAG`, `LEAD`; pertumbuhan periode-ke-periode (MoM, YoY); persentase terhadap total (`x / SUM(x) OVER ()`); `FIRST_VALUE`
- **Fokus ujian:** analisis tren bulanan dengan pertumbuhan dan moving average

#### `sql_tanggal_teks_null` — Fungsi Tanggal, Teks & NULL
- **Wajib:** fungsi tanggal (`DATE_TRUNC`, `EXTRACT`, selisih tanggal, interval; padanannya di SQLite `strftime`); fungsi teks (`LOWER`, `UPPER`, `TRIM`, `SUBSTRING`, `REPLACE`, `||`/`CONCAT`); `CAST`; perilaku `NULL` dalam perbandingan dan agregasi; `COALESCE`, `NULLIF` (mencegah bagi nol)
- **Fokus ujian:** membersihkan dan meringkas data bertanggal yang mengandung NULL

#### `sql_optimasi` — Optimasi Query: Index & EXPLAIN
- **Wajib:** kenapa query bisa lambat; index (kapan membantu, kapan tidak); `EXPLAIN` / `EXPLAIN ANALYZE`; hanya memilih kolom yang perlu (hindari `SELECT *`); filter sedini mungkin; join pada kolom ber-index; mengetes kebenaran hasil sebelum dan sesudah optimasi
- **Fokus ujian:** membandingkan dua versi query untuk pertanyaan yang sama dan menjelaskan mana yang lebih baik

#### `sql_postgresql` — PostgreSQL & Koneksi dari Python
- **Alat:** PostgreSQL + pgAdmin atau DBeaver
- **Wajib:** memasang PostgreSQL di Windows; membuat database dan tabel (`CREATE TABLE`, tipe data umum, `PRIMARY KEY`, `FOREIGN KEY`); impor CSV (`COPY` atau fitur impor); `CREATE VIEW`; koneksi dari Python dengan SQLAlchemy + `pd.read_sql` dan `df.to_sql`; menyimpan kredensial di `.env` (bukan di kode)
- **Fokus ujian:** memuat dataset ke PostgreSQL, membuat view analisis, dan membacanya dari notebook

#### `sql_bigquery` — BigQuery Sandbox
- **Alat:** Google BigQuery Sandbox (gratis, tanpa kartu kredit)
- **Wajib:** project, dataset, tabel; mengaktifkan sandbox dan batasannya; menjelajah public dataset; perbedaan dialek BigQuery yang umum; estimasi data yang diproses dan biaya (kenapa `SELECT *` mahal); konsep partitioned dan clustered table; mengekspor hasil
- **Fokus ujian:** menjawab pertanyaan dari public dataset BigQuery dengan query yang hemat data

#### `dm_relasional_erd` — Model Relasional, Normalisasi & ERD
- **Wajib:** entitas, atribut, relasi; primary key dan foreign key; kardinalitas (1:1, 1:N, N:M) dan tabel penghubung; normalisasi sampai 3NF (intuisi, bukan hafalan definisi); menggambar ERD (misalnya di dbdiagram.io atau draw.io)
- **Fokus ujian:** merancang ERD untuk kasus sederhana (misalnya sistem pesanan katering)

#### `dm_star_schema` — Star Schema: Fact & Dimension
- **Wajib:** OLTP vs OLAP; fact table dan dimension table; grain (satu baris mewakili apa); star vs snowflake schema; date dimension; surrogate key; pengenalan slowly changing dimension (SCD tipe 1 dan 2)
- **Fokus ujian:** mengubah tabel transaksi datar menjadi star schema dan menulis query analisis di atasnya

#### `porto_2` — Portfolio #2: Studi Kasus SQL
- **Wajib:** dataset multi-tabel (misalnya dataset e-commerce publik) dimuat ke PostgreSQL atau BigQuery; 6–8 pertanyaan bisnis yang dijawab SQL, minimal memakai CTE, JOIN, dan window function; file `.sql` terpisah per pertanyaan dengan komentar; ERD/skema; ringkasan temuan dan rekomendasi; `portfolio/2_studi_kasus_sql/README.md`
- **Fokus ujian:** query benar dan terbaca; jumlah baris diperiksa; rekomendasi didukung hasil query

---

# 🍲 FASE 3 — DATA WRANGLING & OTOMASI

#### `wr_method_chaining` — Method Chaining & Fungsi Kustom
- **Wajib:** method chaining dengan tanda kurung; `assign`; `pipe`; `query` dalam rantai; menulis fungsi cleaning yang bisa dipakai ulang; `apply` vs operasi vektor (kapan menghindari `apply`)
- **Fokus ujian:** menulis ulang notebook cleaning yang berantakan menjadi rantai fungsi yang terbaca

#### `wr_datetime` — Datetime & Time Series
- **Wajib:** `to_datetime` dengan `format`; aksesor `.dt` (`year`, `month`, `day_name`, `to_period`); `DatetimeIndex`; `resample` (harian, mingguan, bulanan); `rolling` (moving average); `shift` dan `pct_change`; zona waktu (pengenalan); mengisi tanggal yang hilang
- **Fokus ujian:** membuat ringkasan mingguan/bulanan dengan pertumbuhan dan moving average

#### `wr_teks_kategori` — Teks & Kategori
- **Wajib:** aksesor `.str` (`contains`, `extract`, `split`, `replace` dengan regex); regex dasar (`\d`, `\w`, `+`, `*`, grup); tipe `category` dan urutan kategori; standardisasi label yang beda tulisan; `get_dummies`
- **Fokus ujian:** mengekstrak informasi dari kolom teks berantakan (misalnya nama produk dan ukuran)

#### `wr_performa` — Performa, Memori & Parquet
- **Wajib:** `memory_usage(deep=True)`; memilih `dtype` hemat; membaca sebagian kolom (`usecols`) dan per potongan (`chunksize`); format Parquet (`to_parquet`, `read_parquet`) vs CSV; mengukur waktu (`%timeit`); pengenalan DuckDB untuk query SQL di atas file
- **Fokus ujian:** mempercepat dan menghemat memori pemrosesan dataset besar, dengan ukuran sebelum/sesudah

#### `dq_profiling_validasi` — Profiling & Aturan Validasi
- **Wajib:** dimensi kualitas data (kelengkapan, keunikan, validitas, konsistensi, ketepatan waktu); profiling cepat (`describe(include="all")`, distribusi, nilai unik); menulis aturan validasi sebagai fungsi atau `assert` (rentang nilai, kolom wajib, kunci unik); laporan kualitas data sederhana
- **Fokus ujian:** membuat fungsi pemeriksa kualitas yang menghasilkan daftar pelanggaran

#### `dq_cleaning_lanjut` — Outlier, Duplikat & Standardisasi
- **Wajib:** deteksi outlier (IQR, z-score) dan keputusan menanganinya (hapus, cap, biarkan) berdasarkan konteks bisnis; duplikat sebagian (kunci gabungan); standardisasi format (tanggal, nomor telepon, nama kota); mencatat log perubahan cleaning
- **Fokus ujian:** membersihkan dataset nyata dan mempertahankan keputusan cleaning dengan alasan bisnis

#### `etl_api` — Mengambil Data dari API
- **Alat:** `requests`
- **Wajib:** konsep REST API, endpoint, parameter, status code; `requests.get`, `params`, `headers`; JSON ke DataFrame (`json_normalize`); pagination; rate limit dan `time.sleep`; API key di `.env` (`python-dotenv`); menangani error koneksi
- **Fokus ujian:** mengambil data dari API publik dengan pagination dan menyimpannya rapi

#### `etl_pipeline` — Pipeline ETL dengan Python
- **Wajib:** konsep Extract–Transform–Load (dan ELT); memisahkan fungsi `extract`, `transform`, `load`; konfigurasi di file terpisah; menulis ke PostgreSQL/Parquet; idempotensi (aman dijalankan ulang); logging dengan modul `logging`; struktur folder proyek pipeline
- **Fokus ujian:** pipeline yang bisa dijalankan ulang dari data mentah ke tabel siap analisis

#### `etl_dbt` — Dasar dbt
- **Alat:** dbt Core dengan adapter DuckDB atau PostgreSQL
- **Wajib:** peran dbt (transformasi di dalam database); project dan model (`.sql`); `ref()` dan `source()`; lapisan staging → intermediate → mart; materialisasi `view` dan `table`; tes bawaan (`unique`, `not_null`, `accepted_values`, `relationships`); `dbt run`, `dbt test`, `dbt docs`
- **Fokus ujian:** membangun model staging dan mart kecil beserta tesnya

#### `oto_script_jadwal` — Script & Penjadwalan
- **Wajib:** mengubah notebook menjadi script `.py`; argumen command line (`argparse`); path relatif yang aman; menjadwalkan script dengan Windows Task Scheduler; mencatat log hasil tiap jalan; pengenalan GitHub Actions terjadwal (`schedule`)
- **Fokus ujian:** script yang berjalan otomatis sesuai jadwal dan meninggalkan log

#### `oto_laporan_excel` — Laporan Excel Otomatis
- **Alat:** pandas + openpyxl
- **Wajib:** `ExcelWriter` dengan beberapa sheet; format angka, lebar kolom, header tebal, freeze panes; conditional formatting dasar dengan openpyxl; menyisipkan grafik gambar; nama file berisi tanggal; laporan HTML sederhana sebagai alternatif
- **Fokus ujian:** menghasilkan laporan Excel rapi untuk pembaca non-teknis dengan satu perintah

#### `porto_3` — Portfolio #3: Pipeline Data End-to-End
- **Wajib:** sumber data nyata (API atau file berkala); pipeline extract → validasi kualitas → transform → load (PostgreSQL/DuckDB/Parquet); minimal satu model dbt atau lapisan transformasi terstruktur; laporan Excel/HTML otomatis; bisa dijalankan dengan satu perintah; diagram alur; `portfolio/3_pipeline_data/README.md` berisi cara menjalankan dan keterbatasan
- **Fokus ujian:** pipeline berjalan ulang tanpa error; pemeriksaan kualitas bermakna; dokumentasi cukup untuk orang lain

---

# ⚖️ FASE 4 — STATISTIK UNTUK ANALIS

#### `stat_deskriptif` — Statistik Deskriptif
- **Alat:** pandas, SciPy, seaborn
- **Wajib:** jenis data (nominal, ordinal, interval, rasio); mean, median, modus dan kapan memilih masing-masing; range, varians, standar deviasi, IQR; persentil dan kuartil; skewness dan efek outlier pada rata-rata; koefisien variasi; menyajikan ringkasan yang tidak menyesatkan
- **Fokus ujian:** memilih ukuran pusat dan sebaran yang tepat untuk data miring (misalnya pendapatan atau nilai pesanan)

#### `stat_probabilitas` — Probabilitas & Distribusi
- **Wajib:** probabilitas dasar, aturan penjumlahan dan perkalian; probabilitas bersyarat dan intuisi Bayes; distribusi normal (aturan 68-95-99.7, z-score); binomial; Poisson (pengenalan); simulasi dengan NumPy untuk memeriksa intuisi
- **Fokus ujian:** menghitung dan mensimulasikan peluang dalam konteks bisnis (misalnya peluang konversi)

#### `stat_inferensi` — Sampling & Confidence Interval
- **Wajib:** populasi vs sampel; bias sampling; distribusi sampling dan Central Limit Theorem (dengan simulasi); standard error; confidence interval untuk rata-rata dan proporsi; interpretasi CI yang benar; bootstrap sederhana
- **Fokus ujian:** menghitung dan menafsirkan CI dari data sampel, termasuk dengan bootstrap

#### `uh_konsep` — Konsep Uji Hipotesis & p-value
- **Wajib:** H0 dan H1; uji satu dan dua sisi; tingkat signifikansi α; p-value dan salah kaprahnya; error tipe I dan II; power; signifikansi statistik vs signifikansi praktis; effect size (Cohen's d, selisih proporsi)
- **Fokus ujian:** menafsirkan hasil uji dengan benar dan menjelaskannya ke orang non-teknis

#### `uh_uji_umum` — T-test, Chi-square & ANOVA
- **Alat:** SciPy (`scipy.stats`)
- **Wajib:** memilih uji yang tepat (diagram keputusan); one-sample, independent (Welch), dan paired t-test; uji proporsi dua sampel; chi-square test of independence; one-way ANOVA (pengenalan) dan uji lanjutan; asumsi tiap uji dan alternatif non-parametrik (Mann-Whitney U); multiple testing (koreksi Bonferroni, pengenalan)
- **Fokus ujian:** memilih, menjalankan, dan menafsirkan uji yang tepat untuk tiga pertanyaan berbeda

#### `ab_desain` — Desain Eksperimen & Sample Size
- **Wajib:** kenapa eksperimen terkontrol; unit randomisasi; metrik utama, metrik sekunder, dan guardrail metric; minimum detectable effect (MDE); menghitung sample size dan durasi (statsmodels `power`); pre-registration hipotesis; kapan A/B test tidak cocok
- **Fokus ujian:** menulis rencana A/B test lengkap untuk perubahan fitur, termasuk sample size

#### `ab_analisis` — Analisis & Jebakan A/B Test
- **Wajib:** analisis konversi (uji proporsi + CI selisih); analisis metrik kontinu (t-test, bootstrap); sample ratio mismatch (SRM) check; bahaya mengintip hasil lebih awal (peeking); novelty effect; segmentasi pasca-eksperimen dan risikonya; menulis rekomendasi: rilis, jangan rilis, atau uji ulang
- **Fokus ujian:** menganalisis data eksperimen dan memberi rekomendasi dengan tingkat keyakinan yang jujur

#### `reg_linier` — Regresi Linier
- **Alat:** statsmodels, scikit-learn
- **Wajib:** regresi sederhana dan berganda; interpretasi koefisien ("ceteris paribus"); R² dan adjusted R²; p-value koefisien; variabel dummy; asumsi (linearitas, residual, multikolinearitas, VIF) dan cara memeriksanya; train/test split dan RMSE/MAE untuk prediksi
- **Fokus ujian:** menjelaskan faktor yang memengaruhi suatu angka bisnis (misalnya penjualan) beserta keterbatasan modelnya

#### `reg_logistik` — Regresi Logistik
- **Wajib:** kapan memakai regresi logistik; probabilitas, odds, log-odds; interpretasi koefisien sebagai odds ratio; confusion matrix, precision, recall, F1; ROC-AUC (pengenalan); memilih threshold sesuai biaya bisnis
- **Fokus ujian:** memodelkan peluang churn atau pembelian dan memilih threshold dengan alasan bisnis

#### `kausalitas` — Korelasi vs Kausalitas
- **Wajib:** korelasi Pearson dan Spearman; korelasi semu (spurious); confounder; Simpson's paradox (dengan contoh data); reverse causality; selection bias; kenapa eksperimen kuat untuk klaim sebab-akibat; pengenalan difference-in-differences secara konseptual
- **Fokus ujian:** mengkritik klaim sebab-akibat yang salah dan mengusulkan cara mengujinya

#### `porto_4` — Portfolio #4: Analisis A/B Test
- **Wajib:** dataset eksperimen publik (atau simulasi yang realistis dan dijelaskan); rencana eksperimen (hipotesis, metrik, MDE, sample size); pemeriksaan SRM dan kualitas data; uji statistik yang sesuai beserta CI dan effect size; analisis segmen dengan peringatan; rekomendasi keputusan; `portfolio/4_analisis_ab_test/README.md` dengan ringkasan eksekutif satu paragraf
- **Fokus ujian:** metode tepat; interpretasi jujur; rekomendasi bisa dipertanggungjawabkan

---

# 🛒 FASE 5 — BUSINESS & PRODUCT ANALYTICS

#### `ba_framing` — Merumuskan Masalah Bisnis
- **Wajib:** dari permintaan samar ke pertanyaan yang bisa dijawab; mengidentifikasi keputusan dan pemangku kepentingan; hypothesis tree / issue tree; kerangka MECE; menyusun rencana analisis (pertanyaan, data, metode, output); menanyakan "kalau hasilnya X, apa yang akan dilakukan?"
- **Fokus ujian:** mengubah permintaan samar ("penjualan turun, kenapa?") menjadi rencana analisis terstruktur

#### `ba_metrik_kpi` — Metrik & KPI
- **Wajib:** metrik vs KPI; north star metric dan input metric; leading vs lagging indicator; guardrail metric; definisi metrik yang presisi (pembilang, penyebut, periode, filter); metrik e-commerce umum (GMV, AOV, conversion rate, repeat rate); metrik rasio yang menyesatkan; pohon metrik (metric tree)
- **Fokus ujian:** merancang pohon metrik untuk sebuah bisnis dan mendefinisikan 5 metrik secara presisi

#### `ba_funnel` — Analisis Funnel
- **Wajib:** tahapan funnel dari data event; conversion rate per tahap dan keseluruhan; drop-off; funnel berbasis sesi vs pengguna; batas waktu konversi; membandingkan funnel antar segmen; menghitung funnel dengan SQL dan Pandas
- **Fokus ujian:** menemukan tahap dengan drop-off terbesar dan mengusulkan hipotesis perbaikan

#### `ba_cohort_retensi` — Cohort, Retensi & Churn
- **Wajib:** konsep cohort (berdasarkan bulan pertama); tabel retensi cohort dan heatmap-nya; retensi klasik vs rolling; definisi churn untuk bisnis berlangganan vs transaksional; churn rate; kurva retensi; membaca pola cohort
- **Fokus ujian:** membangun tabel cohort retensi dan menafsirkan perubahan antar cohort

#### `ba_segmentasi` — Segmentasi: RFM & K-Means
- **Alat:** pandas, scikit-learn
- **Wajib:** kenapa segmentasi; RFM (Recency, Frequency, Monetary): perhitungan, skoring kuantil, label segmen; K-Means: scaling (`StandardScaler`), memilih k (elbow, silhouette), menafsirkan centroid; profil segmen; aksi bisnis per segmen
- **Fokus ujian:** membuat segmentasi pelanggan dan rekomendasi aksi untuk tiap segmen

#### `ba_clv` — CLV & Unit Economics
- **Wajib:** customer lifetime value (formula historis sederhana: AOV × frekuensi × masa hidup × margin); CAC dan rasio LTV:CAC; payback period; ARPU; contribution margin; analisis sensitivitas sederhana
- **Fokus ujian:** menghitung CLV per segmen dan menilai apakah kanal akuisisi menguntungkan

#### `ba_forecasting` — Forecasting Dasar
- **Alat:** pandas, statsmodels
- **Wajib:** komponen time series (tren, musiman, noise); dekomposisi (`seasonal_decompose`); baseline naif dan seasonal naive; moving average; exponential smoothing (Holt-Winters, statsmodels `ExponentialSmoothing`); train/test berdasarkan waktu; MAE dan MAPE; menyajikan prediksi dengan rentang ketidakpastian
- **Fokus ujian:** memprediksi penjualan beberapa periode ke depan dan membandingkannya dengan baseline

#### `porto_5` — Portfolio #5: Studi Kasus E-commerce
- **Wajib:** dataset e-commerce publik multi-tabel; rumusan masalah bisnis dan pohon metrik; analisis funnel atau konversi; cohort retensi; segmentasi RFM; CLV per segmen; 3 rekomendasi yang diprioritaskan beserta dampak yang diharapkan; `portfolio/5_studi_kasus_ecommerce/README.md` dengan ringkasan eksekutif
- **Fokus ujian:** analisis terhubung ke keputusan; rekomendasi spesifik dan terukur

---

# 🍽️ FASE 6 — BI & DATA STORYTELLING

#### `xl_formula` — Formula Lanjut & Dynamic Array
- **Alat:** Excel untuk web (gratis dengan akun Microsoft di office.com); Excel desktop bila tersedia
- **Wajib:** referensi relatif/absolut (`$`); `IF`, `IFS`, `AND`/`OR`; `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`; `XLOOKUP` (dan mengenali `VLOOKUP`); `INDEX`+`MATCH`; dynamic array `FILTER`, `UNIQUE`, `SORT`; `LET`; fungsi teks dan tanggal; Excel Table dan structured reference; data validation
- **Fokus ujian:** membangun lembar analisis yang otomatis ter-update saat data ditambah

#### `xl_pivot_powerquery` — PivotTable & Power Query
- **Alat:** Excel untuk web untuk PivotTable. Fitur Power Query di Excel untuk web terbatas; bila menu yang dibutuhkan tidak ada, praktikkan bagian Power Query di Power BI Desktop (gratis), yang memakai mesin dan editor Power Query yang sama
- **Wajib:** PivotTable (rows, columns, values, filter), grouping tanggal, slicer, PivotChart; Power Query: impor dari CSV/folder, tipe data, hapus/pisah/gabung kolom, unpivot, merge dan append query, refresh; conditional formatting
- **Fokus ujian:** menyusun laporan pivot dari data mentah yang dibersihkan dengan Power Query dan bisa di-refresh

#### `pbi_powerquery_model` — Power Query & Data Model
- **Alat:** Power BI Desktop (gratis, Windows)
- **Wajib:** Get Data dari CSV/Excel/PostgreSQL; Import vs DirectQuery (konsep); profil kolom (*Column quality/distribution*); transformasi di Power Query (tipe, split, unpivot, merge, append, group by); fact dan dimension table; relasi, kardinalitas, arah filter; tabel tanggal (date table) dan menandainya; star schema di Power BI
- **Fokus ujian:** membangun model bintang yang benar dari beberapa sumber data

#### `pbi_dax_dasar` — DAX Dasar & CALCULATE
- **Wajib:** measure vs calculated column; `SUM`, `AVERAGE`, `COUNTROWS`, `DISTINCTCOUNT`, `DIVIDE`; row context vs filter context; `CALCULATE` dengan filter; `FILTER`, `ALL`, `ALLEXCEPT`, `REMOVEFILTERS`; persentase terhadap total; variabel `VAR ... RETURN`; format measure
- **Fokus ujian:** membuat measure KPI dan persentase kontribusi yang benar di berbagai slicer

#### `pbi_dax_waktu` — DAX Time Intelligence & Iterator
- **Wajib:** syarat date table; `TOTALYTD`/`DATESYTD`; `SAMEPERIODLASTYEAR`, `DATEADD`; pertumbuhan MoM dan YoY; running total; iterator `SUMX`, `AVERAGEX`; `RANKX`; semi-additive measure (pengenalan, misalnya saldo akhir)
- **Fokus ujian:** membangun measure perbandingan periode dan ranking yang tetap benar saat difilter

#### `pbi_report` — Report Interaktif
- **Wajib:** memilih visual (card, bar, line, matrix, map); slicer dan filter pane; interaksi antar visual; drillthrough dan drill down; bookmark dan tombol navigasi; tooltip kustom; conditional formatting; tema; tata letak untuk layar dan mobile; aksesibilitas dasar (alt text, kontras)
- **Fokus ujian:** report multi-halaman yang bisa dijelajahi pengguna tanpa penjelasan lisan

#### `pbi_service` — Publish, Refresh & Keamanan
- **Wajib:** komponen Power BI Service (workspace, semantic model, report, dashboard, app); cara publish dan berbagi; scheduled refresh dan kapan gateway diperlukan; row-level security (RLS): membuat role di Desktop dan mengujinya dengan *View as*; sensitivity label (konsep); Copilot di Power BI (konsep dan batasannya)
- **Catatan:** Power BI Service butuh akun kerja atau sekolah. Tanpa akun itu, praktik dilakukan di Power BI Desktop (RLS dengan *View as*), dan bagian Service dipelajari lewat dokumentasi serta demo resmi. Bukti cukup berupa file `.pbix` dan tangkapan layar.
- **Fokus ujian:** menerapkan RLS yang benar dan menjelaskan alur publish–refresh–berbagi

#### `st_desain_dashboard` — Prinsip Desain Dashboard
- **Wajib:** kenali pembaca dan keputusannya; hierarki informasi (KPI di atas, detail di bawah); memilih grafik yang tepat; mengurangi clutter (rasio data-ink); warna dengan tujuan dan ramah buta warna; konsistensi; menonjolkan yang penting; kesalahan umum (pie chart berlebihan, sumbu terpotong, terlalu banyak visual)
- **Fokus ujian:** mengkritik dan mendesain ulang dashboard yang buruk dengan alasan setiap perubahan

#### `st_narasi_presentasi` — Narasi Insight & Presentasi
- **Wajib:** struktur cerita data (konteks → masalah → temuan → rekomendasi); SCQA / piramida Minto (jawaban dulu); judul slide berupa kesimpulan; ringkasan eksekutif; menyesuaikan pesan dengan audiens (teknis vs manajemen); menyampaikan ketidakpastian; menangani pertanyaan sulit
- **Fokus ujian:** presentasi 5 slide dari sebuah analisis dengan ringkasan eksekutif yang berdiri sendiri

#### `porto_6` — Portfolio #6: Dashboard Power BI
- **Wajib:** dataset bisnis multi-tabel; model star schema dengan date table; minimal 8 measure DAX termasuk time intelligence; report minimal 3 halaman dengan navigasi, drillthrough, dan tooltip; RLS sederhana; presentasi insight (PDF, 5–8 slide); `portfolio/6_dashboard_powerbi/README.md` berisi tangkapan layar, model data, daftar measure, dan cara memakai
- **Fokus ujian:** angka benar saat difilter; desain jelas; cerita insight meyakinkan

---

# ✨ FASE 7 — AI-AUGMENTED ANALYTICS & CAPSTONE

#### `ai_prompting` — Prompting untuk SQL & Analisis
- **Alat:** ChatGPT Free (atau chatbot AI gratis lain)
- **Wajib:** cara kerja LLM secara singkat (memprediksi teks, bisa berhalusinasi); memberi konteks: skema tabel, contoh baris, definisi metrik; meminta query SQL/Pandas dengan asumsi eksplisit; prompting bertahap (rencana dulu, lalu kode); meminta penjelasan dan alternatif; menyimpan prompt yang berhasil sebagai template
- **Fokus ujian:** menghasilkan query yang benar dengan bantuan AI untuk pertanyaan bisnis, beserta prompt dan revisinya

#### `ai_verifikasi` — Memverifikasi Hasil AI
- **Wajib:** jenis kesalahan AI yang umum (join salah, filter hilang, definisi metrik keliru, angka dikarang); teknik verifikasi: cek jumlah baris, rekonsiliasi total, uji pada data kecil yang hasilnya diketahui, membandingkan dua metode; membaca kode AI baris per baris; mendokumentasikan verifikasi
- **Fokus ujian:** menemukan dan memperbaiki kesalahan tersembunyi pada analisis buatan AI

#### `ai_bi_copilot` — AI di Excel & Power BI
- **Alat:** Power BI Desktop (gratis). Copilot di Excel dan Power BI butuh lisensi berbayar, jadi dipelajari sebagai konsep saja
- **Wajib:** AI visual di Power BI Desktop (Key Influencers, Decomposition Tree, Q&A) beserta cara menafsirkannya; anomaly detection dan forecast bawaan di line chart; Copilot di Excel dan Power BI: kemampuan, syarat lisensi, dan risikonya (konsep); kapan fitur AI membantu dan kapan menyesatkan
- **Fokus ujian:** memakai AI visual untuk menemukan pemicu sebuah metrik, lalu memverifikasi temuannya secara manual

#### `ai_llm_teks` — Analisis Teks dengan LLM API
- **Alat:** Python + Gemini API tingkat gratis (kunci API dari Google AI Studio, tanpa kartu kredit). Di tingkat gratis, data yang dikirim boleh dipakai Google untuk meningkatkan produknya, jadi **hanya kirim data publik atau data contoh, jangan data pribadi**
- **Wajib:** memanggil LLM API dari Python (library resmi `google-genai`); API key di `.env`; batas kuota tingkat gratis (permintaan per menit dan per hari; cek angkanya di AI Studio karena bisa berubah) serta cara menanganinya (jeda, retry, batch kecil); prompt untuk klasifikasi (sentimen, topik), ekstraksi, dan ringkasan; structured output (JSON) dan validasinya; memproses banyak baris secara batch; biaya token dan estimasinya; mengevaluasi akurasi pada sampel berlabel manual
- **Fokus ujian:** mengklasifikasikan ulasan pelanggan dengan LLM dan mengukur akurasinya terhadap label manual

#### `ai_otomasi_insight` — Otomasi Narasi Insight
- **Alat:** Python + Gemini API tingkat gratis (sama dengan `ai_llm_teks`)
- **Wajib:** menghasilkan ringkasan narasi dari tabel metrik dengan LLM; memberi angka yang sudah dihitung (bukan meminta LLM menghitung); template laporan; langkah review manusia sebelum dikirim; mendeteksi narasi yang tidak didukung data
- **Fokus ujian:** pipeline kecil: metrik dihitung kode → narasi dibuat LLM → dicek manusia

#### `ai_etika_privasi` — Privasi, Etika & Tata Kelola Data
- **Wajib:** data pribadi (PII) dan kenapa tidak boleh dikirim sembarangan ke layanan AI; anonimisasi dan pseudonimisasi; prinsip UU Pelindungan Data Pribadi Indonesia (UU PDP) secara umum; bias dalam data dan model; transparansi metode; dokumentasi sumber dan keputusan; kebijakan pemakaian AI di tempat kerja
- **Fokus ujian:** menilai sebuah rencana analisis berbasis AI dari sisi privasi dan etika, lalu memperbaikinya

#### `capstone` — Capstone: Analisis End-to-End
- **Wajib:** satu masalah bisnis nyata atau realistis yang dipilih Tasya; rencana analisis; data diambil dengan SQL; wrangling dan validasi kualitas; analisis statistik yang sesuai (uji, regresi, atau eksperimen); analisis bisnis (metrik, segmen, atau cohort); dashboard Power BI; minimal satu bagian yang memakai AI beserta bukti verifikasinya; presentasi 8–10 slide dengan ringkasan eksekutif; README profesional di `portfolio/7_capstone/`
- **Fokus ujian:** alur utuh dari pertanyaan sampai rekomendasi; metode tepat; verifikasi AI terdokumentasi; komunikasi jelas
