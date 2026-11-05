# Penelitian waktu penyelesaian izin usaha atau NIB

Cari rata-rata waktu aktual yang diperlukan untuk menyelesaikan izin usaha atau menerbitkan Nomor Induk Berusaha (NIB) di Indonesia. Prioritaskan data nasional terbaru yang tersedia dan periksa apakah angka tersebut merupakan rata-rata yang diukur, bukan target layanan.

## Sumber dan verifikasi

- Cari dan periksa langsung sumber primer seperti OSS, Kementerian Investasi dan Hilirisasi/BKPM, kementerian atau lembaga pemerintah terkait, dan BPS. Publikasi akademik dan portal berita bereputasi dapat digunakan sebagai sumber pendukung.
- Bedakan NIB dari izin usaha lain. Catat jenis layanan, cakupan geografis, periode pengukuran, dan titik awal serta akhir proses jika dinyatakan. Jangan menggeneralisasi angka daerah, sektor, jenis izin, atau tingkat risiko tertentu sebagai angka nasional.
- Bedakan rata-rata aktual dari standar pelayanan, batas waktu, estimasi, median, dan klaim proses instan. Jangan melaporkan ukuran-ukuran tersebut sebagai rata-rata. Jika hanya standar atau estimasi tersedia, catat sebagai temuan terpisah dan biarkan rata-rata bernilai `null`.
- Bandingkan periode data saat memilih temuan terbaru; tanggal publikasi tidak selalu sama dengan periode pengukuran. Jelaskan jika periode, definisi, atau cakupan tidak diketahui.
- Catat URL halaman yang benar-benar diperiksa, nama penerbit, judul, tanggal publikasi jika tersedia, dan kutipan singkat yang mendukung setiap temuan. Utamakan sumber primer dan nyatakan jika hanya sumber sekunder tersedia.
- Jangan membuat angka, satuan, tanggal, kutipan, atau URL. Jangan menghitung rata-rata dari batas atau contoh waktu layanan.
- Jika pencarian web tidak tersedia, sumber tidak dapat diakses, atau rata-rata yang memenuhi kriteria tidak ditemukan, gunakan status yang sesuai dan biarkan `average_duration` bernilai `null`. Jangan menyatakan penelitian berhasil.

## Penyimpanan

Jangan menyimpan hasil penelitian ke file. Masukkan rata-rata nasional aktual yang terverifikasi langsung ke tabel `usecase_harmonisasi.mart_permit_total_temp` menggunakan fungsi `insert_data` dari `tools/database.py`. Gunakan query `INSERT` dengan parameter terikat, bukan interpolasi nilai ke dalam SQL.

Isi kolom berikut:
- `duration_days`: rata-rata aktual dalam satuan hari, sebagai bilangan bulat (`INT`). Konversikan hanya bila sumber menyatakan unit dan konversinya jelas; jika hasil konversi bukan bilangan bulat, jangan membulatkan atau mengubah data—jangan masukkan baris.
- `submitted_at`: tanggal hari ini dalam format tanggal (`DATE`, `YYYY-MM-DD`).
- `source`: nilai JSON yang berisi informasi sumber terverifikasi, minimal URL, judul, penerbit, tanggal publikasi jika tersedia, dan kutipan pendukung.

Masukkan hanya rata-rata nasional aktual yang terukur, dengan tanggal/periode pengukuran jelas dan cakupan Indonesia yang eksplisit. Jangan masukkan standar pelayanan, batas waktu, estimasi, median, klaim proses instan, atau angka daerah/sektor/jenis layanan yang tidak mewakili cakupan nasional. Jika pencarian web tidak tersedia atau rata-rata yang memenuhi kriteria tidak ditemukan, jangan masukkan baris. Jangan mengarang nilai atau sumber.
