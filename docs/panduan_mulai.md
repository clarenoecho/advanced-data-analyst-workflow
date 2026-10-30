# 🚀 Panduan Mulai (sekali saja)

Panduan ini menyiapkan laptop Tasya (Windows) sampai siap belajar. Perkiraan waktu: 30–45 menit. Bila ada langkah yang macet, tempel pesan errornya ke mentor di ChatGPT atau minta bantuan orang yang memberimu folder ini.

---

## 1. Buat akun GitHub

1. Buka https://github.com/signup dan daftar. Pilih username yang rapi, misalnya `tasya-data`, karena akan terlihat di portfolio.
2. Verifikasi email.

## 2. Buat repo kosong di GitHub

1. Setelah login, klik **+** (kanan atas) → **New repository**.
2. **Repository name:** `advanced-data-analyst-workflow` (harus persis sama).
3. Pilih **Public**. Mentor AI membaca progres dari repo ini, jadi repo harus publik.
4. **Jangan** centang *Add a README*, *.gitignore*, atau *license*. Repo harus benar-benar kosong.
5. Klik **Create repository**.

## 3. Pasang alat

| Alat | Unduh | Catatan saat memasang |
|---|---|---|
| Git | https://git-scm.com/download/win | Klik *Next* terus (pilihan bawaan sudah tepat) |
| Python 3.12 atau lebih baru | https://www.python.org/downloads/ | **Centang _Add python.exe to PATH_** di layar pertama, lalu *Install Now* |
| VS Code | https://code.visualstudio.com/ | Centang *Add "Open with Code" action* supaya bisa klik kanan folder |

Setelah VS Code terbuka, pasang dua ekstensi dari menu Extensions (ikon kotak di kiri): **Python** dan **Jupyter** (keduanya dari Microsoft).

Cek pemasangan: buka **Command Prompt**, ketik:

```text
python --version
git --version
```

Keduanya harus menampilkan nomor versi. Bila `python` tidak dikenali, pasang ulang Python dan pastikan *Add python.exe to PATH* tercentang.

## 4. Taruh folder repo

Simpan folder `advanced-data-analyst-workflow` di tempat yang mudah dan tanpa sinkronisasi cloud, misalnya:

```text
C:\Users\<namamu>\Documents\advanced-data-analyst-workflow
```

Hindari folder OneDrive karena bisa bentrok dengan Git.

## 5. Klik dua kali `Setup Awal.bat`

Jendela hitam akan:

1. memeriksa Python dan Git,
2. memasang paket kecil yang dibutuhkan,
3. **menanyakan username GitHub**, lalu mengisinya ke semua dokumen,
4. menanyakan nama dan email untuk Git (pakai email akun GitHub),
5. mengirim isi folder ke repo GitHub. **Jendela login GitHub akan muncul**: pilih *Sign in with your browser* dan izinkan,
6. membuat folder `paket_project/` berisi 3 file aturan untuk ChatGPT.

Bila muncul **✅ Setup selesai**, buka `https://github.com/<username-mu>/advanced-data-analyst-workflow` dan pastikan file-filenya sudah ada.

## 6. Siapkan mentor di ChatGPT

Ikuti [`panduan_chatgpt_project.md`](panduan_chatgpt_project.md).

## 7. (Opsional) Shortcut Simpan Progres di Desktop

Klik kanan `Simpan Progres.bat` → **Show more options** → **Send to** → **Desktop (create shortcut)**. Ganti namanya menjadi "💾 Simpan Progres" bila mau.

---

## Belajar sehari-hari

```text
1. Buka chat baru di ChatGPT Project "Dapur Data" → ketik: cek progres
2. Ketik: lanjut          → pelajari materinya, coba kodenya di VS Code (notebook di folder latihan/)
3. Ketik: latihan         → pemanasan; tempel kode + output sebagai teks (jangan unggah file)
4. Ketik: ujian           → dicicip mentor; bila lulus, mentor memberi blok YAML
5. Salin blok YAML itu    → klik dua kali Simpan Progres.bat
6. Kembali ke langkah 1 untuk resep berikutnya
```

Ingat: file yang disebut di `bukti:` harus sudah tersimpan di folder repo, dan namanya harus sama persis.

Sistem ini dirancang untuk **ChatGPT Free**. Kuota unggah file di paket Free sekitar 3 per hari, jadi biasakan menempelkan kode dan output sebagai teks. Bila mentor tidak bisa membuka GitHub, klik dua kali **`Salin Dashboard.bat`** lalu tempel hasilnya ke chat.

## Masalah umum

| Masalah | Solusi |
|---|---|
| `python` tidak dikenali | Pasang ulang Python dengan *Add python.exe to PATH* tercentang, lalu buka Command Prompt baru |
| Push gagal: *repository not found* | Cek nama repo di GitHub persis `advanced-data-analyst-workflow` dan username yang diketik benar |
| Push gagal: *rejected* / *non-fast-forward* | Repo di GitHub tidak kosong. Hapus repo itu lalu buat ulang tanpa README, kemudian jalankan Setup Awal lagi |
| VS Code minta memasang *ipykernel* | Klik *Install* |
| Mentor tidak bisa membuka GitHub | Pastikan repo **Public**. Bila masih gagal, klik dua kali `Salin Dashboard.bat` lalu tempel ke chat |
| ChatGPT bilang batas tercapai | Paket Free punya batas pemakaian. Tunggu beberapa jam, sementara itu kerjakan latihan di notebook |
