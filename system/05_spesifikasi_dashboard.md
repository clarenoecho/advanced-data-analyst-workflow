---
dokumen: spesifikasi_dashboard
versi: 1.0
tanggal: 2026-10-30
peran: Aturan tampilan dashboard bertema Dapur Data. Isi dashboard sendiri ada di state/dashboard.md.
---

# Spesifikasi Dashboard

## Prinsip

Gamifikasi adalah lapisan motivasi. Ia tidak boleh menggantikan pelacakan berbasis bukti.

```text
state/state.yaml  (sumber kebenaran)
        ↓ dibaca oleh tools/progress.py
state/dashboard.md  (tampilan)
```

## Siapa yang membuat dashboard

- **Hanya `tools/progress.py`** yang membuat `state/dashboard.md` (`python tools/progress.py dashboard --tulis`; perintah `apply` dan Simpan Progres juga membuatnya ulang otomatis).
- **Mentor menampilkan isi `state/dashboard.md` apa adanya** dalam blok kode saat Tasya mengetik `cek progres`. Mentor tidak membuat, merapikan, atau mengubah isinya.
- File itu ditandai "dihasilkan otomatis" dan tidak boleh diedit manual.

## Pola tampilan

- Bagian atas: judul, nama koki, **pangkat** (dihitung dari jumlah fase yang lulus, tabelnya di `system/02_roadmap.md`), dan target.
- **Fase lulus** menampilkan semua resepnya dan penutup `🏅 LULUS`.
- **Fase berjalan** menampilkan semua modulnya. Modul yang berisi beberapa resep dan sedang aktif ditandai `🍳 MENU AKTIF` dan diperluas.
- **Fase terkunci** hanya satu baris ringkasan.
- Bagian bawah: resep aktif, resep berikutnya, hidangan terakhir yang lulus, dan posisi sekarang.

## Label

| Status di `state.yaml` | Label di dashboard |
|---|---|
| `belum` | 🔒 TERKUNCI |
| `aktif` | 🔥 SEDANG DIMASAK ◀ |
| `learned` | 🥄 SIAP DICICIP ◀ |
| `validated` | 🍽️ TERSAJI |
| `retained` | 📖 RESEP HAFAL |
| `mastered` | ⭐ SIGNATURE DISH |
| resep opsional yang belum diambil | ⏭️ OPSIONAL |

| Status fase | Label |
|---|---|
| semua resep wajib selesai | 🏅 LULUS |
| ada resep yang sedang dikerjakan | 🔥 BERJALAN |
| belum dimulai | 🔒 TERKUNCI |

Ikon: 🥄 resep biasa, 🎁 portfolio, 🎂 capstone, 🍳 modul aktif. Ikon fase: 🥚 0, 🥕 1, 🔪 2, 🍲 3, ⚖️ 4, 🛒 5, 🍽️ 6, ✨ 7.

## Aturan konsistensi

Setelah format ini disetujui, struktur dan istilahnya tidak diubah tanpa persetujuan Tasya. Perubahan format dilakukan dengan mengubah `tools/progress.py`, spesifikasi ini, dan tes di `tests/` secara bersamaan.
