# 🤖 Panduan ChatGPT Project (ChatGPT Free)

Mentor Dapur Data berjalan di **ChatGPT Project** dan dirancang untuk **ChatGPT Free**. Project hanya berisi aturan (3 file). **Progres dibaca mentor langsung dari GitHub** di awal setiap sesi, jadi tidak ada file progres yang perlu diunggah ulang.

## Batasan ChatGPT Free yang membentuk rancangan

| Batasan (per Oktober 2026) | Penyesuaian di sistem ini |
|---|---|
| Maksimal **5 file per Project** | Paket aturan hanya **3 file** |
| Unggah file sekitar **3 per hari**, dan bisa lebih rendah saat ramai | 3 file bisa diunggah dalam satu hari. Saat belajar, kode dan output **ditempel sebagai teks**, bukan diunggah |
| Ingatan percakapan lebih pendek, dan model gratis lebih terbatas | **Chat baru setiap resep baru**; jawaban panjang dipecah (`teruskan`); mentor menilai ujian per soal secara tertulis |
| Mentor kadang gagal membuka alamat web | `Salin Dashboard.bat` menyalin progres ke clipboard untuk ditempel ke chat |

Batasan ini bisa berubah sewaktu-waktu. Bila ChatGPT menampilkan pesan batas tercapai, tunggu sampai batasnya pulih (biasanya beberapa jam) atau lanjutkan belajar sendiri dari notebook dulu.

## Alamat progres di GitHub

| File | Alamat |
|---|---|
| Dashboard | https://raw.githubusercontent.com/clarenoecho/advanced-data-analyst-workflow/main/state/dashboard.md |
| State | https://raw.githubusercontent.com/clarenoecho/advanced-data-analyst-workflow/main/state/state.yaml |

(Bila alamat di atas belum berisi username GitHub yang asli, Setup Awal belum dijalankan.)

## Langkah membuat Project

1. Di ChatGPT, buka **Projects** di sidebar kiri → **New project**, beri nama **Dapur Data**.
2. Unggah 3 file dari folder `paket_project/` di repo (dibuat oleh Setup Awal):

| # | File | Isi |
|---|---|---|
| 1 | `aturan_mentor.md` | Gabungan otomatis: konstitusi, rubrik validasi, protokol mentor, penyajian materi, alur dan command, spesifikasi dashboard, kebijakan referensi |
| 2 | `02_roadmap.md` | Fase dan urutan |
| 3 | `09_kurikulum.md` | Isi wajib setiap resep |

3. Buka pengaturan Project → **Instructions**, lalu tempel teks di bawah. Bila kolom Instructions tidak tersedia, tidak apa-apa: instruksi inti sudah ada di awal `aturan_mentor.md`, cukup tempel teks ini sebagai pesan pertama di setiap chat baru.

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

## Kebiasaan belajar yang hemat kuota

- **Satu chat per resep.** Mulai chat baru di dalam Project setiap kali resep aktif berganti, atau bila mentor mulai melenceng. Ketik `cek progres` sebagai pesan pertama.
- **Tempel, jangan unggah.** Salin kode dari VS Code dan output-nya, lalu tempel di chat. Untuk grafik, jelaskan singkat apa yang terlihat; unggah tangkapan layar hanya bila mentor benar-benar perlu melihatnya.
- **Simpan kuota unggah** untuk hal yang tidak bisa ditempel, misalnya tangkapan layar dashboard Power BI di Fase 6.
- **Ketik `teruskan`** bila jawaban mentor berhenti di tengah.

## Bila aturan di `system/` berubah (jarang)

1. Jalankan `python tools\bangun_paket.py` di folder repo.
2. Di Project, hapus file lama yang berubah, lalu unggah versi barunya dari `paket_project/` (ingat kuota 3 unggahan per hari).

## Tips

- Jika jawaban mentor tidak menyebut isi dashboard, minta: "buka dashboard.md dari GitHub dulu", atau tempel hasil `Salin Dashboard.bat`.
- Jangan mengunggah `state.yaml` atau `dashboard.md` ke Project; salinannya akan basi dan bisa terbaca sebagai progres lama.
- Jika mentor mulai melenceng dari format, ingatkan: "ikuti Aturan Penyajian Materi", atau mulai chat baru.

## Sumber batasan

- [ChatGPT File Upload Limits 2026 (AI Toolbox)](https://www.ai-toolbox.co/chatgpt-management-and-productivity/chatgpt-file-upload-limits-2026): 5 file per Project dan 3 unggahan per hari untuk Free.
- [ChatGPT Free Plan Limits in 2026 (FreeAcademy)](https://freeacademy.ai/blog/chatgpt-free-plan-limits-2026): ingatan percakapan lebih pendek di paket Free.
