# Penelitian jumlah NIB terdaftar

Cari jumlah kumulatif Nomor Induk Berusaha (NIB) terdaftar di Indonesia yang paling baru tersedia, dengan tanggal data tidak melewati 31 Desember 2026. Jika penelitian dilakukan sebelum tanggal tersebut, jangan mengasumsikan data masa depan tersedia.

## Sumber dan verifikasi

- Cari dan periksa langsung sumber primer, terutama OSS, Kementerian Investasi dan Hilirisasi/BKPM, kementerian terkait, atau BPS. Publikasi akademik dan portal berita bereputasi dapat digunakan sebagai sumber pendukung.
- Pilih angka nasional kumulatif terbaru yang benar-benar menyatakan jumlah NIB terdaftar atau diterbitkan. Jangan menyamakan jumlah pelaku usaha, proyek, investasi, atau jumlah dalam periode tertentu dengan total kumulatif NIB.
- Catat tanggal data secara terpisah dari tanggal publikasi. Jika tanggal data tidak dinyatakan, isi `data_as_of` dengan `null` dan jelaskan keterbatasannya. Bandingkan tanggal data sebelum menentukan angka terbaru; jangan menganggap tanggal publikasi sebagai tanggal data.
- Catat URL halaman yang benar-benar diperiksa, nama penerbit, judul, tanggal publikasi jika tersedia, dan kutipan singkat yang mendukung angka. Utamakan sumber primer dan nyatakan jika hanya sumber sekunder tersedia.
- Jika definisi, cakupan, atau periode angka ambigu, jelaskan di `notes`. Jangan membuat angka, tanggal, kutipan, atau URL.
- Jika pencarian web tidak tersedia, sumber tidak dapat diakses, atau angka yang memenuhi kriteria tidak ditemukan, tulis status yang sesuai dan biarkan `count` bernilai `null`. Jangan menyatakan penelitian berhasil.

## Penyimpanan

Jangan menyimpan hasil penelitian ke file. Masukkan jumlah NIB terdaftar yang terverifikasi langsung ke tabel `usecase_harmonisasi.mart_permit_total_temp` menggunakan fungsi `insert_data` dari `tools/database.py`. Gunakan query `INSERT` dengan parameter terikat, bukan interpolasi nilai ke dalam SQL.

Isi kolom berikut:
- `value_count`: jumlah kumulatif NIB terdaftar/diterbitkan, sebagai bilangan bulat (`INT`).
- `submitted_at`: tanggal hari ini.
- `source`: nilai JSON yang berisi informasi sumber terverifikasi, minimal URL, judul, penerbit, tanggal publikasi jika tersedia, dan kutipan pendukung.

Masukkan hanya angka nasional kumulatif yang secara eksplisit menyatakan jumlah NIB terdaftar atau diterbitkan dan memiliki tanggal data yang jelas. Jangan menyamakan jumlah pelaku usaha, proyek, investasi, atau jumlah NIB dalam periode tertentu dengan total kumulatif. Jika pencarian web tidak tersedia atau angka yang memenuhi kriteria tidak ditemukan, jangan masukkan baris. Jangan mengarang nilai atau sumber.
