# Penelitian izin usaha yang sedang diproses OSS

Cari jumlah permohonan izin usaha yang masih aktif diproses melalui sistem OSS di Indonesia pada waktu data terbaru yang tersedia. Jangan menganggap angka historis sebagai kondisi saat ini tanpa menyebutkan tanggal atau periode datanya.

## Sumber dan verifikasi

- Cari dan periksa langsung sumber primer, terutama OSS dan Kementerian Investasi dan Hilirisasi/BKPM, termasuk dashboard dan publikasi resmi yang dapat diakses publik. Sumber pemerintah lain, publikasi akademik, dan media bereputasi dapat digunakan sebagai pendukung; jelaskan jika hanya sumber sekunder tersedia.
- Pilih angka yang secara eksplisit menghitung permohonan izin usaha yang masih dalam proses atau menunggu penyelesaian pada suatu waktu. Bedakan dari jumlah NIB atau izin yang sudah diterbitkan, jumlah permohonan masuk selama periode tertentu, jumlah pelaku usaha, dan jumlah permohonan tertunda karena kekurangan persyaratan apabila cakupannya tidak jelas. Jangan menghitung jumlah dalam proses dengan mengurangkan angka yang definisi, cakupan, atau tanggalnya tidak sebanding.
- Catat definisi status, jenis izin dan tahapan proses yang tercakup, cakupan geografis, serta tanggal dan waktu data jika tersedia. Bedakan tanggal data dari tanggal publikasi dan tanggal penelusuran. Jika sumber tidak menyatakan tanggal data, isi `data_as_of` dengan `null` dan jelaskan keterbatasannya; jangan menyimpulkan angka tersebut mencerminkan kondisi saat ini.
- Bandingkan tanggal data sebelum memilih angka terbaru. Catat judul, penerbit, URL halaman yang benar-benar diperiksa, tanggal publikasi jika tersedia, dan kutipan singkat yang mendukung angka serta statusnya. Jangan membuat angka, tanggal, kutipan, atau URL.
- Jika pencarian web tidak tersedia, sumber tidak dapat diakses, atau angka yang memenuhi kriteria tidak ditemukan, gunakan status yang sesuai dan biarkan `count` bernilai `null`. Jangan menyatakan penelitian berhasil.

## Penyimpanan

Jangan menyimpan hasil penelitian ke file. Masukkan jumlah permohonan terverifikasi langsung ke tabel `usecase_harmonisasi.mart_permit_pending_temp` menggunakan fungsi `insert_data` dari `tools/database.py`. Gunakan query `INSERT` dengan parameter terikat, bukan interpolasi nilai ke dalam SQL.

Isi kolom berikut:
- `value_count`: jumlah permohonan yang memenuhi kriteria, sebagai bilangan bulat (`INT`). Jangan masukkan angka perkiraan atau hitungan yang cakupannya tidak jelas.
- `submitted_at`: tanggal hari ini.
- `source`: nilai JSON yang berisi informasi sumber terverifikasi, minimal URL, judul, penerbit, tanggal publikasi jika tersedia, dan kutipan pendukung.

Masukkan hanya angka yang secara eksplisit menghitung permohonan izin usaha yang masih diproses/menunggu penyelesaian pada tanggal data tertentu. Jika pencarian tidak tersedia atau tidak menemukan angka yang memenuhi kriteria, jangan masukkan baris. Jangan mengarang nilai atau sumber.