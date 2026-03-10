# Tabel Database (Kamus Data) - Sistem Presensi MI Aska Baitul Ulum

Berikut adalah rincian struktur tabel database beserta tipe data dan ukurannya untuk laporan Bab IV, sesuai dengan implementasi pada aplikasi Flask:

### 1. Tabel: `user`
Menyimpan data akun pengguna (Admin dan Guru) untuk akses masuk ke sistem.
| Nama Kolom | Tipe Data | Ukuran | Keterangan |
| :--- | :--- | :--- | :--- |
| `id` | Integer | 11 | Primary Key, Auto Increment |
| `username` | Varchar | 50 | Nama pengguna unik untuk login |
| `password` | Varchar | 255 | Hash kata sandi (keamanan akun) |
| `full_name` | Varchar | 100 | Nama lengkap Guru / Admin |
| `role` | Varchar | 10 | Peran (admin, guru) |

### 2. Tabel: `class`
Menyimpan data rombongan belajar / kelas di MI Aska Baitul Ulum.
| Nama Kolom | Tipe Data | Ukuran | Keterangan |
| :--- | :--- | :--- | :--- |
| `id` | Integer | 11 | Primary Key, Auto Increment |
| `class_name` | Varchar | 20 | Nama kelas (Misal: Kelas 1-A) |
| `academic_year`| Varchar | 20 | Tahun ajaran aktif |
| `teacher_id` | Integer | 11 | Foreign Key ke `user.id` |

### 3. Tabel: `student`
Menyimpan data identitas Siswa.
| Nama Kolom | Tipe Data | Ukuran | Keterangan |
| :--- | :--- | :--- | :--- |
| `id` | Integer | 11 | Primary Key, Auto Increment |
| `nisn` | Varchar | 20 | Nomor Induk Siswa Nasional (Unik) |
| `full_name` | Varchar | 100 | Nama lengkap siswa |
| `gender` | Varchar | 1 | Jenis kelamin (L/P) |
| `class_id` | Integer | 11 | Foreign Key ke `class.id` |

### 4. Tabel: `attendance`
Menyimpan record kehadiran harian siswa.
| Nama Kolom | Tipe Data | Ukuran | Keterangan |
| :--- | :--- | :--- | :--- |
| `id` | Integer | 11 | Primary Key, Auto Increment |
| `student_id` | Integer | 11 | Foreign Key ke `student.id` |
| `date` | Date | - | Tanggal absensi |
| `status` | Varchar | 1 | Status (H=Hadir, S=Sakit, I=Izin, A=Alpa) |
| `time_in` | Time | - | Waktu data diinput ke sistem |
