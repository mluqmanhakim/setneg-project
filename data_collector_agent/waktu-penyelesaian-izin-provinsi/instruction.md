# Penelitian waktu penyelesaian izin usaha per provinsi

Cari data terbaru yang tersedia tentang waktu aktual penyelesaian izin usaha atau penerbitan Nomor Induk Berusaha (NIB) untuk setiap provinsi di Indonesia. Kumpulkan hanya data yang berhasil diverifikasi; lewati provinsi yang tidak memiliki data yang memenuhi kriteria.

## Sumber dan verifikasi

- Cari dan periksa langsung sumber primer seperti OSS, Kementerian Investasi dan Hilirisasi/BKPM, BPS, pemerintah provinsi, dan DPMPTSP. Publikasi akademik dan media bereputasi dapat digunakan jika sumber primer tidak tersedia.
- Cari setiap provinsi secara sistematis. Masukkan data hanya jika sumber secara eksplisit menyatakan cakupan provinsi tersebut. Jangan menggeneralisasi data kabupaten/kota, sektor, jenis izin, atau tingkat risiko menjadi data seluruh provinsi.
- Utamakan rata-rata waktu aktual yang diukur. Jangan menyamakan rata-rata dengan standar pelayanan, batas waktu, estimasi, median, atau klaim proses instan. Jika hanya ukuran lain tersedia, masukkan sebagai temuan terpisah dengan jenisnya secara jelas, bukan sebagai rata-rata.
- Catat jenis layanan, cakupan, periode pengukuran, serta titik awal dan akhir proses jika tersedia. Bandingkan periode data, bukan hanya tanggal publikasi, ketika memilih data terbaru. Jangan menghitung rata-rata dari batas atau contoh waktu layanan.
- Untuk setiap temuan, catat judul, penerbit, URL halaman yang benar-benar diperiksa, tanggal publikasi jika tersedia, dan kutipan singkat yang mendukung angka serta cakupan geografisnya. Jelaskan keterbatasan definisi, cakupan, dan periode.
- Jangan mengarang angka, satuan, tanggal, kutipan, atau URL. Jika pencarian web tidak tersedia, gunakan status `search_unavailable` dan daftar provinsi kosong; jika pencarian dilakukan tetapi tidak ada data yang memenuhi kriteria, gunakan `not_found` dan daftar kosong.

## Penyimpanan

Jangan menyimpan hasil penelitian ke file. Masukkan setiap temuan berupa rata-rata aktual yang terverifikasi langsung ke tabel `usecase_harmonisasi.mart_permit_by_province_temp` menggunakan fungsi `insert_data` dari `tools/database.py`. Tulis query `INSERT` dengan parameter terikat, bukan interpolasi nilai ke dalam SQL.

Isi kolom berikut:
- `province` (text): Nama provinsi sesuai referensi provinsi yang tersedia.
- `submitted_at` (date): tanggal hari ini.
- `duration_days` (int): durasi rata-rata aktual dalam hari. Konversikan hanya bila sumber memberikan unit eksplisit. Jangan mengonversi standar pelayanan, estimasi, median, atau klaim proses instan menjadi rata-rata.
- `source` (text): JSON semua sumber yang benar-benar diperiksa dan mendukung angka serta cakupan provinsi.

Masukkan hanya data dengan rata-rata aktual terukur dan cakupan provinsi yang eksplisit. Lewati data yang hanya berupa standar, estimasi, atau ukuran lain karena tabel ini tidak memiliki kolom untuk membedakan jenis temuan. Jangan mengarang nilai atau memasukkan baris yang tidak terverifikasi.