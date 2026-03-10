# DOKUMENTASI PENGUJIAN & ANALISIS SISTEM
## Sistem Absensi MI Aska Baitul Ulum

---

## 1. DESKRIPSI APLIKASI

Sistem Absensi MI Aska Baitul Ulum merupakan sebuah aplikasi berbasis web yang dirancang khusus untuk membantu proses pencatatan kehadiran siswa di lingkungan Madrasah Ibtidaiyah (MI) Aska Baitul Ulum secara digital, efisien, dan terpusat. Aplikasi ini dikembangkan menggunakan bahasa pemrograman Python dengan framework Flask, serta memanfaatkan SQLite sebagai sistem manajemen basis data yang ringan dan mudah dikelola.

Latar belakang pengembangan sistem ini berawal dari permasalahan yang kerap terjadi dalam proses absensi manual, yaitu penggunaan buku absensi kertas yang rentan rusak, hilang, atau sulit direkap secara berkala. Dengan hadirnya sistem ini, para guru dapat mencatat kehadiran dengan lebih cepat dan akurat.

Secara fungsional, aplikasi ini dirancang untuk digunakan oleh **Guru**. Guru memiliki akses untuk melakukan pengelolaan data kelas dan siswa, melakukan input absensi harian, serta melihat dasbor rekapitulasi kehadiran secara real-time.

Antarmuka pengguna (user interface) aplikasi ini dirancang dengan mengutamakan kemudahan penggunaan (user-friendly), menampilkan tampilan modern dengan tema gelap (dark mode), dilengkapi dengan efek glassmorphism dan aksen warna neon yang memberikan kesan premium dan profesional. Fitur utama yang tersedia di dalam aplikasi meliputi: halaman login dengan sistem autentikasi yang aman menggunakan enkripsi password (bcrypt), dasbor interaktif yang menampilkan statistik kehadiran harian secara real-time, serta halaman input absensi per kelas dengan pilihan status Hadir (H), Sakit (S), Izin (I), dan Alfa (A).

Aplikasi ini juga dilengkapi dengan fitur keamanan sesi login menggunakan Flask-Login, sehingga seluruh halaman yang membutuhkan autentikasi tidak dapat diakses oleh pengguna yang belum login.

---

## 2. TABEL BLACK BOX TESTING

| No | Modul | Skenario Pengujian | Data Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|:---:|:---|:---|:---|:---|:---|:---:|
| 1 | Login | Login dengan data valid | Username: `guru`, Password: `guru123` | Berhasil masuk ke halaman Dashboard | Berhasil masuk ke Dashboard | ✅ Pass |
| 2 | Login | Login dengan password salah | Username: `guru`, Password: `salah123` | Muncul pesan "Username atau password salah" | Pesan error muncul | ✅ Pass |
| 3 | Login | Login dengan username kosong | Username: kosong, Password: `guru123` | Form tidak terkirim, validasi HTML aktif | Form tidak terkirim | ✅ Pass |
| 4 | Dashboard | Akses dashboard tanpa login | Langsung buka `/dashboard` di browser | Diarahkan ke halaman login | Redirect ke `/login` | ✅ Pass |
| 5 | Dashboard | Melihat statistik kehadiran hari ini | Login sebagai Guru | Tampil angka Hadir, Sakit, Izin, Alfa | Data statistik tampil | ✅ Pass |
| 6 | Dashboard | Filter tabel berdasarkan status | Klik kartu "Hadir" | Tabel hanya menampilkan siswa berstatus Hadir | Tabel terfilter | ✅ Pass |
| 7 | Kelola Kelas | Menambah kelas baru | Nama: `Kelas 2-B`, Tahun: `2024/2025` | Kelas baru muncul di daftar | Kelas berhasil ditambahkan | ✅ Pass |
| 8 | Kelola Siswa | Menambah siswa baru | NISN: `12399`, Nama: `Dewi`, L/P: P, Kelas: Kelas 1-A | Siswa baru masuk ke daftar | Siswa berhasil ditambahkan | ✅ Pass |
| 9 | Kelola Siswa | Tambah siswa dengan NISN duplikat | NISN: `12345` (sudah ada) | Muncul pesan "NISN sudah terdaftar" | Pesan error duplikat muncul | ✅ Pass |
| 10 | Input Absensi | Input absensi untuk semua siswa | Pilih status H/S/I/A pada setiap baris | Data absensi tersimpan, muncul notifikasi sukses | Absensi berhasil disimpan | ✅ Pass |
| 11 | Input Absensi | Ubah absensi yang sudah diinput | Ubah status dari H ke S pada tanggal sama | Status terupdate di database | Status berhasil diperbarui | ✅ Pass |
| 12 | Input Absensi | Hadirkan semua siswa sekaligus | Klik tombol "Hadirkan Semua" | Semua radio button H tercentang | Semua tercentang otomatis | ✅ Pass |
| 13 | Input Absensi | Pilih tanggal masa lalu | Pilih tanggal 1 minggu yang lalu | Menampilkan data absensi tanggal tersebut | Data historis tampil | ✅ Pass |
| 14 | Unduh Excel | Unduh rekap absensi kelas | Klik "Unduh Excel" di halaman kelas | File `.xlsx` terunduh secara otomatis | File berhasil diunduh | ✅ Pass |
| 15 | Logout | Keluar dari sistem | Klik tombol "Keluar" | Sesi dihapus, diarahkan ke halaman login | Berhasil logout | ✅ Pass |

---

## 3. GAP ANALISIS

| No | Kebutuhan / Fitur | Kondisi Saat Ini | Kondisi Ideal | Status | Rekomendasi |
|:---:|:---|:---|:---|:---:|:---|
| 1 | Autentikasi Login | Login dengan username & password terenkripsi (bcrypt) | Login aman untuk Guru | 🟢 Tersedia | — |
| 2 | Dashboard Statistik | Statistik kehadiran hari ini (H/S/I/A) | Grafik visual (chart) | 🟡 Parsial | Integrasikan Chart.js |
| 3 | Input Absensi Harian | Input per kelas, pilih tanggal, status H/S/I/A | Input mudah & cepat | 🟢 Tersedia | — |
| 4 | Rekap Laporan Excel | Unduh rekap per kelas dalam format .xlsx | Rekap per bulan/semester | 🟢 Tersedia | — |
| 5 | Manajemen Data Kelas | Tambah kelas baru | Full CRUD Kelas | 🟡 Parsial | Tambah Edit/Hapus |
| 6 | Manajemen Data Siswa | Tambah siswa baru | Full CRUD Siswa | 🟡 Parsial | Tambah Edit/Hapus |
| 7 | Responsif Mobile | Layout desktop-first | Tampilan optimal di HP | 🟡 Parsial | Media Queries |

