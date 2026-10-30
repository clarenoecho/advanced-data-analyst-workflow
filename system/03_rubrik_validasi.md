---
dokumen: rubrik_validasi
versi: 1.0
tanggal: 2026-10-30
peran: Menjawab "kapan sebuah resep boleh naik status?" Dibaca oleh mentor AI dan oleh tools/progress.py.
otoritas: Di bawah constitution, di atas protokol_mentor
---

# Rubrik Validasi

Rubrik ini menentukan kapan sebuah resep (modul atau quest) boleh naik status. Aturannya bersifat **constraint**, bukan saran. Perubahan rubrik hanya sah dengan persetujuan eksplisit Tasya.

## 1. Empat status

| Status | Label dashboard | Arti | Syarat naik |
|---|---|---|---|
| **Learned** | 🥄 SIAP DICICIP | Materi dan latihan terpandu selesai, belum diuji | Materi selesai dipelajari |
| **Validated** | 🍽️ TERSAJI | Lulus ujian validasi | Bagian 3 |
| **Retained** | 📖 RESEP HAFAL | Masih bisa setelah jeda, di konteks baru | Bagian 5 |
| **Mastered** | ⭐ SIGNATURE DISH | Terbukti dipakai mandiri di situasi baru | Bagian 6 |

Skor tinggi atau challenge yang sukses tidak otomatis berarti Retained atau Mastered.

## 2. Bentuk ujian per tipe resep

| Tipe | Contoh | Bentuk ujian validasi |
|---|---|---|
| Resep materi | `sql_window_ranking`, `pd_groupby_agg` | 3–5 soal + 1 challenge (aturan sesi `latihan`) |
| Portfolio (🎁) | Laporan EDA, Studi Kasus SQL | Proyek lengkap + README + refleksi (masalahnya apa, keputusan, keterbatasan, rekomendasi) |
| Capstone (🎂) | Analisis End-to-End | Seperti portfolio, ditambah presentasi insight dan bukti verifikasi hasil AI |

Level soal: **L1** terpandu, **L2** terapan (memilih konsep sendiri), **L3** transfer (masalah baru, pendekatan dipilih sendiri). Setiap ujian memuat minimal satu soal L2. Porsi L3 bertambah di fase yang lebih tinggi: mulai Fase 2, challenge validasi minimal L2; mulai Fase 4, minimal L3.

Mulai Fase 2, setiap challenge **berawal dari pertanyaan bisnis** (misalnya "produk mana yang penjualannya turun tiga bulan berturut-turut?"), bukan dari instruksi teknis.

## 3. Syarat Validated

Semua syarat harus terpenuhi:

1. **Akurasi ≥ 80%** pada skor gabungan (soal 50%, challenge 50%).
2. **Pemahaman:** Tasya menjelaskan alasan dari **dua keputusan** yang ia ambil (bukan hanya sintaks).
3. **Bukti tersimpan:** file yang bisa dibuka kembali di folder repo (notebook, `.sql`, `.xlsx`, `.pbix`, gambar, atau PDF), dirujuk di Evidence Entry.
4. **Cakupan lengkap:** ujian mencakup semua item *Wajib* resep itu di `system/09_kurikulum.md`.

Jika tidak lulus: status tetap. Mentor memberi umpan balik, dan Tasya boleh mengulang kapan saja dengan soal berbeda, tanpa batas jumlah percobaan.

## 4. Mode bantuan AI

Tiga mode, selalu **dicatat** di Evidence Entry:

- **Independent**: Tasya mencoba sendiri sepenuhnya.
- **Assisted**: AI memberi hint, debugging, atau umpan balik terarah.
- **Review**: AI hanya mengkritik solusi yang sudah selesai.

Aturan:
- Untuk **Validated**, bantuan AI boleh (tidak dibatasi), tetapi modenya wajib dicatat apa adanya dan keluaran AI tidak dianggap benar otomatis.
- Untuk **Retained** dan **Mastered**, mode wajib **Independent**.

## 5. Syarat Retained (retrieval review)

- Dilakukan **minimal 7 hari** setelah tanggal Validated.
- 2–3 soal **retrieval** tanpa membuka catatan, pada **konteks baru**.
- Akurasi **≥ 80%**, mode **Independent**.
- Jadwal otomatis: review pertama H+7 setelah Validated. Setelah lulus, konfirmasi dijadwalkan H+30 dari tanggal Validated (paling cepat 7 hari setelah retrieval). Setelah konfirmasi lulus, tidak ada review terjadwal lagi.

Jika retrieval gagal: status **tidak turun**. Resep diberi tanda `perlu_review` dan dijadwalkan ulang H+3.

## 6. Syarat Mastered

- Skill terbukti dipakai **mandiri (Independent)** di **≥ 2 konteks berbeda** (dataset atau masalah berbeda), misalnya challenge L3 dan proyek portfolio.
- Bukti dari kedua konteks dirujuk.
- Hanya resep berstatus Retained yang boleh naik ke Mastered.

## 7. Evidence Entry (bukti wajib)

Setiap perubahan status disertai satu entri:

| Kolom | Isi |
|---|---|
| id | Pengenal unik, contoh `2026-11-05-py-dasar` |
| modul | `id` resep di `state/state.yaml` (contoh `sql_window_ranking`) |
| tanggal | YYYY-MM-DD |
| jenis | `validasi`, `retrieval`, atau `mastery` |
| skor_persen | Angka 0–100 |
| mode_ai | `independent`, `assisted`, atau `review` |
| level_soal | Ringkasan L1/L2/L3 yang diuji |
| bukti | Daftar path file di repo (atau URL) |
| pemahaman | Dua keputusan beserta alasannya (wajib untuk `validasi`) |
| konteks | Khusus `mastery`: minimal dua konteks berbeda beserta buktinya |
| keputusan | Status baru yang diusulkan; tulis `tetap` bila tidak lulus |

`tools/progress.py` menghitung sendiri hasil akhirnya. Bila `keputusan` tidak sama dengan hasil perhitungan, entri ditolak.

## 8. Resep opsional

Resep bertanda opsional (misalnya `py_oop`) boleh dilewati. Bila Tasya ingin mengambilnya, resep itu boleh divalidasi kapan saja setelah semua resep wajib sebelumnya selesai, tanpa menggeser resep aktif.

## 9. Siapa yang boleh mengubah state?

- **Mentor AI** hanya **mengusulkan** Evidence Entry dan tidak boleh mengklaim progres dari ingatan.
- **`tools/progress.py`** memeriksa aturan di atas lalu menulis `state.yaml`.
- **Tasya** menyetujui dan menyimpan progres (Simpan Progres).

## 10. Yang dilarang

- Menaikkan status karena topik "pernah dibahas".
- Melompati resep atau fase yang masih terkunci.
- Menghapus atau menurunkan status yang sudah tervalidasi.
- Mengubah format dashboard di luar spesifikasi yang disetujui.
