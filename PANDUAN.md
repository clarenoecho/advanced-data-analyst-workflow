# 🍳 Panduan Dapur Data untuk Tasya

Halo Tasya! 👋 Panduan ini menemanimu dari nol sampai bisa belajar setiap hari dengan sistem **Dapur Data: Advanced Data Analyst**. Baca berurutan sekali saja. Setelah itu, cukup buka bagian **4. Belajar sehari-hari** setiap kali mau belajar.

> 💸 Semua yang dipakai di sini **gratis**: ChatGPT Free, GitHub, Python, VS Code, Power BI Desktop, dan alat lainnya.

## Daftar isi

1. [Kenalan dulu: sistem ini apa?](#1-kenalan-dulu-sistem-ini-apa)
2. [Persiapan laptop (sekali saja)](#2-persiapan-laptop-sekali-saja)
3. [Menyiapkan mentor di ChatGPT (sekali saja)](#3-menyiapkan-mentor-di-chatgpt-sekali-saja)
4. [Belajar sehari-hari](#4-belajar-sehari-hari)
5. [Menyimpan progres](#5-menyimpan-progres)
6. [Membaca dashboard](#6-membaca-dashboard)
7. [Tips hemat ChatGPT Free](#7-tips-hemat-chatgpt-free)
8. [Kalau ada masalah](#8-kalau-ada-masalah)
9. [Kamus istilah](#9-kamus-istilah)

---

## 1. Kenalan dulu: sistem ini apa?

Dapur Data adalah **sistem belajar mandiri** untuk menjadi **Advanced Data Analyst**, yaitu analis data yang bisa mengambil data dengan SQL, mengolahnya dengan Python, menilainya dengan statistik, menyajikannya lewat dashboard, dan memakai AI dengan cermat.

Ada tiga bagian yang bekerja sama:

| Bagian | Perannya | Ibaratnya |
|---|---|---|
| **Mentor AI** di ChatGPT | Mengajar, memberi latihan, menguji | Head Chef yang membimbingmu |
| **Folder repo** di laptop | Tempat semua latihan dan catatan progres | Dapurmu |
| **GitHub** | Salinan online folder repo; mentor membaca progresmu dari sini | Buku catatan dapur yang bisa dibaca Head Chef dari mana saja |

### Temanya dapur 🍳

- Materi dibagi menjadi **8 fase** (0–7), seperti bagian-bagian dapur.
- Setiap materi adalah satu **resep**.
- Ujian disebut **dicicip**: mentor mencicipi hasil masakanmu.
- Setiap fase yang lulus menaikkan **pangkatmu**, dari **Trainee Dapur** sampai **Head Chef**.

### 8 fase yang akan kamu lalui

| Fase | Belajar apa | Proyek akhir fase |
|---|---|---|
| 🥚 0 | Python Dasar | Buku Resep Digital (program sederhana) |
| 🥕 1 | Pandas & Visualisasi | Laporan EDA (eksplorasi data) |
| 🔪 2 | SQL & Data Modeling | Studi Kasus SQL |
| 🍲 3 | Data Wrangling & Otomasi | Pipeline Data |
| ⚖️ 4 | Statistik untuk Analis | Analisis A/B Test |
| 🛒 5 | Business Analytics | Studi Kasus E-commerce |
| 🍽️ 6 | Excel, Power BI & Storytelling | Dashboard Power BI |
| ✨ 7 | AI untuk Analis | Capstone (proyek besar akhir) |

Setiap proyek akhir fase masuk ke folder `portfolio/` dan bisa kamu tunjukkan saat melamar kerja.

### Aturan paling penting

1. **Progres hanya naik lewat ujian yang lulus** (nilai minimal 80%), bukan karena "sudah pernah dibahas".
2. **Ujian boleh diulang tanpa batas.** Gagal itu bagian dari belajar, bukan hukuman.
3. **Satu resep pada satu waktu.** Resep berikutnya terbuka setelah resep yang sekarang lulus.

---

## 2. Persiapan laptop (sekali saja)

Perkiraan waktu: 30–45 menit. Siapkan internet yang stabil.

### Langkah 1: Buat akun GitHub

1. Buka https://github.com/signup lalu daftar.
2. Pilih **username** yang rapi, misalnya `tasya-data`. Username ini akan terlihat di portfoliomu, jadi hindari nama yang asal-asalan.
3. Buka email dan verifikasi akunmu.
4. **Catat username-mu**, nanti ditanyakan.

### Langkah 2: Buat repo kosong di GitHub

Repo adalah "folder online" di GitHub.

1. Login ke GitHub, klik tombol **+** di kanan atas → **New repository**.
2. Isi **Repository name** persis: `advanced-data-analyst-workflow`
3. Pilih **Public**. Ini wajib, karena mentor membaca progresmu dari sini.
4. **Jangan centang apa pun** di bawahnya (*Add a README*, *.gitignore*, *license* dibiarkan kosong).
5. Klik **Create repository**. Halaman berikutnya boleh diabaikan.

### Langkah 3: Pasang tiga aplikasi

Pasang berurutan:

**a. Git** → https://git-scm.com/download/win
Unduh, buka, lalu klik **Next** terus sampai selesai. Pilihan bawaannya sudah tepat.

**b. Python** → https://www.python.org/downloads/
Klik tombol unduh versi terbaru. Saat penginstal terbuka:
> ⚠️ **Centang _Add python.exe to PATH_** di bagian bawah layar pertama. Ini langkah yang paling sering terlewat.

Lalu klik **Install Now**.

**c. VS Code** → https://code.visualstudio.com/
Saat memasang, centang **Add "Open with Code" action** supaya nanti bisa klik kanan folder lalu membukanya di VS Code.

Setelah VS Code terbuka, klik ikon **Extensions** (gambar kotak-kotak di sisi kiri), lalu cari dan pasang dua ekstensi ini (keduanya buatan Microsoft):
- **Python**
- **Jupyter**

**Cek pemasangan:** tekan tombol Windows, ketik `cmd`, buka **Command Prompt**, lalu ketik dua perintah ini satu per satu dan tekan Enter:

```text
python --version
git --version
```

Keduanya harus menampilkan nomor versi, misalnya `Python 3.13.1`. Kalau muncul tulisan *not recognized*, lihat bagian [8. Kalau ada masalah](#8-kalau-ada-masalah).

### Langkah 4: Taruh folder repo di laptop

Kamu akan menerima folder `advanced-data-analyst-workflow` (biasanya dalam bentuk zip). Ekstrak lalu taruh di:

```text
C:\Users\<nama-kamu>\Documents\advanced-data-analyst-workflow
```

> ⚠️ Jangan taruh di folder **OneDrive** atau Google Drive, karena sinkronisasi cloud bisa bentrok dengan Git.

### Langkah 5: Klik dua kali `Setup Awal.bat`

Buka folder repo, lalu klik dua kali **`Setup Awal.bat`**. Jendela hitam akan muncul dan bertanya beberapa hal:

| Pertanyaan | Jawab dengan |
|---|---|
| Username GitHub kamu | Username dari Langkah 1, misalnya `tasya-data` |
| Nama untuk riwayat Git | Namamu, misalnya `Tasya` |
| Email akun GitHub kamu | Email yang dipakai mendaftar GitHub |

Lalu akan muncul **jendela login GitHub**. Pilih **Sign in with your browser**, login, lalu klik **Authorize**.

Kalau muncul tulisan **✅ Setup selesai**, berhasil! 🎉 Cek dengan membuka `https://github.com/<username-mu>/advanced-data-analyst-workflow`; file-file repo seharusnya sudah ada di sana.

### Langkah 6 (opsional): Shortcut di Desktop

Supaya gampang, buat shortcut untuk dua file yang akan sering dipakai:

1. Klik kanan **`Simpan Progres.bat`** → **Show more options** → **Send to** → **Desktop (create shortcut)**.
2. Lakukan hal yang sama untuk **`Salin Dashboard.bat`**.

---

## 3. Menyiapkan mentor di ChatGPT (sekali saja)

### Langkah 1: Buat Project

1. Login ke https://chatgpt.com (akun gratis sudah cukup).
2. Di sidebar kiri, cari **Projects** → **New project**.
3. Beri nama **Dapur Data**.

### Langkah 2: Unggah 3 file aturan

Di folder repo, buka folder **`paket_project`** (dibuat otomatis oleh Setup Awal). Unggah ketiga file ini ke Project:

1. `aturan_mentor.md`
2. `02_roadmap.md`
3. `09_kurikulum.md`

> 💡 ChatGPT Free membatasi sekitar **3 unggahan file per hari**, pas untuk ketiga file ini. Jadi lakukan langkah ini di hari yang sama, jangan dipakai untuk mengunggah file lain dulu.

### Langkah 3: Tempel instruksi

Buka pengaturan Project → **Instructions**, lalu salin dan tempel teks di bawah ini:

```text
Kamu adalah mentor (Head Chef pembimbing) Tasya di "Dapur Data: Advanced Data Analyst". Bahasa: Indonesia. Tasya mulai dari nol, jadi jelaskan dengan sabar dan bertahap.

Sumber kebenaran ATURAN adalah file di Project ini (aturan_mentor.md, 02_roadmap.md, 09_kurikulum.md). Sumber kebenaran PROGRES adalah state di GitHub, bukan ingatanmu dan bukan percakapan lama.

Di awal setiap chat, dan setiap kali Tasya mengetik "cek progres", buka:
- https://raw.githubusercontent.com/clarenoecho/advanced-data-analyst-workflow/main/state/dashboard.md
- https://raw.githubusercontent.com/clarenoecho/advanced-data-analyst-workflow/main/state/state.yaml
Jika gagal, minta Tasya menjalankan "Salin Dashboard.bat" dan menempelkan hasilnya. Jangan menebak progres.

Kamu hanya MENGUSULKAN perubahan progres lewat Evidence Entry (satu blok kode YAML; format dan syarat di aturan_mentor.md). Jangan pernah menyatakan status naik. Setelah menyerahkan entri, ingatkan Tasya menyalinnya dan klik dua kali "Simpan Progres.bat".

Ikuti "Mode hemat ChatGPT Free": jangan minta Tasya mengunggah file (minta kode dan output ditempel sebagai teks), pecah jawaban panjang dan akhiri dengan "ketik teruskan", nilai ujian per soal secara tertulis.

Command: cek progres, lanjut, latihan, ujian, review, simpan, bingung, teruskan. Materi baru mengikuti Aturan Penyajian Materi dan daftar Wajib di 09_kurikulum.md. Jangan memberi petunjuk sebelum Tasya mencoba sendiri.
```

> ℹ️ Kalau di teks di atas masih tertulis `clarenoecho`, berarti Setup Awal belum dijalankan. Setelah Setup Awal, tulisan itu otomatis diganti username-mu. Kalau kolom **Instructions** tidak ada di akunmu, tidak masalah: tempel teks itu sebagai pesan pertama setiap kali membuka chat baru.

### Langkah 4: Coba!

Buka chat baru di dalam Project **Dapur Data**, lalu ketik:

```text
cek progres
```

Mentor seharusnya menampilkan dashboard dengan resep aktif **Setup: Python, VS Code & Jupyter**. Kalau ya, semuanya siap! 🎉

---

## 4. Belajar sehari-hari

### Alur satu resep

```text
cek progres  →  lanjut (beberapa kali)  →  latihan  →  ujian  →  Simpan Progres  →  resep berikutnya
```

1. **Buka chat baru** di Project Dapur Data, lalu ketik `cek progres`.
2. Ketik **`lanjut`** untuk mempelajari materi. Mentor menjelaskan 2–3 subtopik per sesi, lengkap dengan contoh kode.
3. **Coba sendiri kodenya** di VS Code. Simpan notebook di folder `latihan/` sesuai fasenya (lihat di bawah).
4. Ulangi `lanjut` sampai mentor bilang semua materi resep ini sudah tersaji.
5. Ketik **`latihan`** untuk pemanasan (tidak dinilai resmi).
6. Kalau sudah siap, ketik **`ujian`**. Kerjakan di notebook, lalu tempel kode dan output-nya ke chat.
7. Kalau nilainya ≥ 80%, mentor memberi **blok YAML**. Simpan progres (bagian 5).
8. Mulai **chat baru** untuk resep berikutnya.

### Daftar command

Ketik salah satu kata ini di chat mentor:

| Ketik | Untuk |
|---|---|
| `cek progres` | Melihat dashboard dan review yang jatuh tempo |
| `lanjut` | Mempelajari materi resep aktif |
| `latihan` | Pemanasan: 3–5 soal + 1 challenge, tidak dinilai resmi |
| `ujian` | Ujian resmi resep aktif ("dicicip") |
| `review` | Mengulang resep lama yang sudah dijadwalkan untuk diulang |
| `simpan` | Merangkum sesi dan meminta blok YAML bila ada ujian yang selesai |
| `bingung` | Minta dijelaskan ulang dengan cara lain atau contoh lebih sederhana |
| `teruskan` | Melanjutkan jawaban mentor yang terpotong |

Kamu juga boleh bertanya bebas kapan saja, misalnya "kenapa error ini muncul?".

### Tempat menyimpan file latihan

| Fase | Simpan di |
|---|---|
| 0 | `latihan/0_python_dasar/` |
| 1 | `latihan/1_pandas_visualisasi/` |
| 2 | `latihan/2_sql/` |
| 3 | `latihan/3_wrangling_otomasi/` |
| 4 | `latihan/4_statistik/` |
| 5 | `latihan/5_business_analytics/` |
| 6 | `latihan/6_bi_storytelling/` |
| 7 | `latihan/7_ai_analytics/` |
| Proyek akhir fase | `portfolio/<nomor>_<nama-proyek>/` |

Beri nomor di depan nama file supaya urut, misalnya `01_setup.ipynb`, `02_variabel.ipynb`. Hindari spasi di nama file.

### Membuat notebook di VS Code

1. Klik kanan folder repo → **Open with Code**.
2. Di panel kiri, klik kanan folder `latihan/0_python_dasar` → **New File** → beri nama, misalnya `01_setup.ipynb`.
3. Klik **Select Kernel** di kanan atas → pilih **Python**.
4. Tulis kode di sel, lalu tekan **Shift+Enter** untuk menjalankannya.
5. Simpan dengan **Ctrl+S**.

### Review berkala

Setelah sebuah resep lulus, mentor akan menjadwalkan **review** 7 hari kemudian (dan sekali lagi sekitar 30 hari kemudian). Review berisi 2–3 soal singkat tanpa membuka catatan. Kalau lulus, statusnya naik menjadi 📖 **Resep Hafal**. Kalau `cek progres` menyebut ada review jatuh tempo, ketik `review`.

---

## 5. Menyimpan progres

Setiap kali lulus ujian atau review, mentor memberi blok seperti ini:

```yaml
id: 2026-11-05-py-dasar
modul: py_dasar
tanggal: 2026-11-05
jenis: validasi
skor_persen: 85
mode_ai: assisted
level_soal: "2 soal L1, 2 soal L2, challenge L2"
bukti:
  - latihan/0_python_dasar/02_variabel_operator.ipynb
pemahaman: >
  Keputusan 1: ... alasannya ...
  Keputusan 2: ... alasannya ...
keputusan: validated
```

Blok ini disebut **Evidence Entry**, yaitu bukti bahwa kamu lulus.

### Cara menyimpan (2 langkah)

1. **Salin** seluruh blok itu. Klik tombol **Copy** di pojok kanan atas blok kode.
2. **Klik dua kali `Simpan Progres.bat`** (di folder repo atau shortcut Desktop).

Jendela hitam menampilkan 6 langkah. Kalau muncul **✅ Progres tersimpan**, selesai! Tunggu sekitar 5 menit sebelum `cek progres`, karena GitHub butuh waktu untuk memperbarui.

### Sebelum klik, pastikan

- ✅ File yang disebut di `bukti:` sudah **disimpan** (Ctrl+S) di folder repo.
- ✅ Nama dan lokasi filenya **sama persis** dengan yang tertulis di `bukti:`, termasuk huruf besar-kecil.
- ✅ Laptop terhubung internet.

### Kalau muncul ❌ "Entri ditolak"

Tenang, tidak ada yang rusak. Salin pesan errornya, tempel ke chat mentor, lalu minta mentor memperbaiki blok YAML-nya. Setelah itu, salin blok yang baru dan klik Simpan Progres lagi.

---

## 6. Membaca dashboard

Saat kamu mengetik `cek progres`, mentor menampilkan dashboard. Contoh potongannya:

```text
🍳 DAPUR DATA: ADVANCED DATA ANALYST
👤 KOKI   : Tasya
🎖️ PANGKAT : Commis Chef
🎯 TARGET : Advanced Data Analyst

🥕 FASE 1 — PANDAS & VISUALISASI DASAR                   🔥 BERJALAN
│
├── 🥄 NumPy Esensial                               🍽️ TERSAJI
├── 🍳 PANDAS                                       🍳 MENU AKTIF
│   ├── 🥄 Series, DataFrame & Membaca Data         🍽️ TERSAJI
│   ├── 🥄 Seleksi & Filtering                      🍽️ TERSAJI
│   ├── 🥄 Data Cleaning Dasar                      🔥 SEDANG DIMASAK ◀
│   └── 🥄 GroupBy & Agregasi                       🔒 TERKUNCI
```

### Arti label

| Label | Artinya |
|---|---|
| 🔥 SEDANG DIMASAK | Resep yang sedang kamu pelajari |
| 🥄 SIAP DICICIP | Materi selesai, tinggal ujian |
| 🍽️ TERSAJI | Lulus ujian |
| 📖 RESEP HAFAL | Lulus review setelah jeda, tanda kamu benar-benar ingat |
| ⭐ SIGNATURE DISH | Sudah kamu pakai sendiri di dua kasus berbeda; tanda benar-benar menguasai |
| 🔒 TERKUNCI | Belum terbuka |
| ⏭️ OPSIONAL | Boleh dilewati |
| 🎁 | Proyek portfolio di akhir fase |

### Pangkat

| Fase yang sudah lulus | Pangkat |
|---|---|
| belum ada | Trainee Dapur |
| 0 | Commis Chef |
| 0–1 | Demi Chef de Partie |
| 0–2 | Chef de Partie |
| 0–3 | Senior Chef de Partie |
| 0–4 | Sous Chef |
| 0–5 | Executive Sous Chef |
| 0–6 | Chef de Cuisine |
| 0–7 | **Head Chef (Advanced Data Analyst)** 👑 |

---

## 7. Tips hemat ChatGPT Free

ChatGPT gratis punya beberapa batasan. Kebiasaan ini membuat belajarmu tetap lancar:

| Kebiasaan | Kenapa |
|---|---|
| **Tempel kode sebagai teks**, jangan unggah file | Unggah file dibatasi sekitar 3 per hari |
| **Buka chat baru untuk setiap resep** | Chat yang terlalu panjang membuat mentor lupa aturan |
| Ketik **`teruskan`** bila jawaban terpotong | Jawaban panjang dipecah menjadi beberapa pesan |
| Pakai **`Salin Dashboard.bat`** bila mentor tidak bisa membuka GitHub | Progres ditempel sebagai teks, tidak memakai kuota unggah |
| Simpan kuota unggah untuk **tangkapan layar Power BI** di Fase 6 | Hanya itu yang benar-benar perlu diunggah |
| Kalau muncul pesan **batas tercapai**, istirahat dulu | Batasnya pulih setelah beberapa jam. Sambil menunggu, ulangi latihan di notebook |

---

## 8. Kalau ada masalah

| Masalah | Solusi |
|---|---|
| `python` atau `git` *not recognized* | Pasang ulang Python dan pastikan **Add python.exe to PATH** dicentang. Lalu tutup dan buka lagi Command Prompt |
| Setup Awal: *repository not found* | Cek nama repo di GitHub persis `advanced-data-analyst-workflow`, dan username yang kamu ketik benar |
| Setup Awal: *rejected* / *non-fast-forward* | Repo di GitHub tidak kosong. Hapus repo itu (Settings → paling bawah → Delete), buat ulang tanpa centang apa pun, lalu jalankan Setup Awal lagi |
| Jendela login GitHub tidak muncul | Jalankan lagi Setup Awal; pastikan browser default bisa membuka github.com |
| VS Code minta memasang *ipykernel* | Klik **Install** |
| Mentor tidak bisa membuka GitHub | Pastikan repo **Public**. Klik dua kali `Salin Dashboard.bat`, lalu tempel (Ctrl+V) ke chat |
| Simpan Progres: *bukti tidak ditemukan* | Simpan file dulu (Ctrl+S), dan cocokkan nama/lokasinya dengan `bukti:` |
| Simpan Progres: *Clipboard kosong* | Salin dulu blok YAML dari mentor, baru klik Simpan Progres |
| Simpan Progres: push gagal | Progresmu sudah tersimpan di laptop. Cek internet lalu klik Simpan Progres lagi untuk entri berikutnya, atau minta bantuan untuk menjalankan `git push` |
| Mentor bilang progres berbeda dengan yang kamu ingat | Yang berlaku adalah dashboard di GitHub. Tunggu 5 menit setelah Simpan Progres, lalu `cek progres` lagi |
| Mentor mulai aneh atau tidak mengikuti format | Buka chat baru di Project, lalu `cek progres` |

Kalau masih buntu, tempel pesan error lengkapnya ke chat mentor. Mentor bisa membantu membaca error.

---

## 9. Kamus istilah

| Istilah | Artinya |
|---|---|
| **Repo** (repository) | Folder proyek yang riwayat perubahannya dicatat Git |
| **Git** | Aplikasi pencatat riwayat perubahan file |
| **GitHub** | Situs tempat menyimpan repo secara online |
| **Commit** | Satu "foto" perubahan yang dicatat Git |
| **Push** | Mengirim commit dari laptop ke GitHub |
| **Notebook** (`.ipynb`) | File berisi sel kode dan sel penjelasan yang bisa dijalankan satu per satu |
| **Kernel** | Mesin Python yang menjalankan kode di notebook |
| **Evidence Entry** | Blok YAML berisi bukti kamu lulus ujian atau review |
| **YAML** | Format teks sederhana `kunci: nilai` yang dipakai Evidence Entry |
| **Resep** | Satu topik materi di sistem ini |
| **Dashboard** | Peta progresmu, dibuat otomatis dari catatan progres |
| **Mode AI** | Seberapa banyak AI membantumu saat ujian: `independent` (sendiri), `assisted` (dibantu petunjuk), `review` (AI hanya mengoreksi hasil akhir) |

---

Selamat memasak data, Chef Tasya! 🍳✨ Pelan-pelan saja; yang penting konsisten dan benar-benar paham.
