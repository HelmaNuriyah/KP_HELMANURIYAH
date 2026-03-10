# Struktur Database: Sistem Absensi MI Aska Baitul Ulum

Berikut adalah rancangan struktur database (Schema) untuk aplikasi absensi siswa. Rancangan ini menggunakan pendekatan relasional yang optimal untuk performa dan integritas data sesuai model di Flask SQLAlchemy.

## 1. Tabel `user` (Guru)
Menyimpan data pengguna yang memiliki akses ke sistem.
| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `id` | INT (PK) | Auto increment |
| `username` | VARCHAR(50) | Unik, untuk login |
| `password` | VARCHAR(255) | Hash password |
| `full_name` | VARCHAR(100) | Nama lengkap guru |

## 2. Tabel `class` (Kelas)
Menyimpan data rombongan belajar.
| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `id` | INT (PK) | Auto increment |
| `class_name` | VARCHAR(20) | Contoh: 'Kelas 1-A', 'Kelas 6', dsb. |
| `academic_year`| VARCHAR(20) | Contoh: '2023/2024' |

## 3. Tabel `student` (Siswa)
Menyimpan data profil siswa.
| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `id` | INT (PK) | Auto increment |
| `nisn` | VARCHAR(20) | Nomor Induk Siswa Nasional (Unik) |
| `full_name` | VARCHAR(100) | Nama lengkap siswa |
| `gender` | VARCHAR(1) | 'L' atau 'P' |
| `class_id` | INT (FK) | Relasi ke `class.id` |

## 4. Tabel `attendance` (Log Presensi)
Tabel utama yang mencatat kehadiran setiap hari.
| Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `id` | INT (PK) | Auto increment |
| `student_id` | INT (FK) | Relasi ke `student.id` |
| `date` | DATE | Tanggal absensi |
| `status` | VARCHAR(1) | 'H' (Hadir), 'S' (Sakit), 'I' (Izin), 'A' (Alpa) |
| `time_in` | TIME | Jam input data |

---

## Relasi Antar Tabel (Entity Relationship)
1.  **One-to-Many**: Satu `Class` memiliki banyak `Student`.
2.  **One-to-Many**: Satu `Student` memiliki banyak catatan di tabel `Attendance`.

## Contoh Query SQL (Preview)
```sql
-- Mendapatkan statistik kehadiran hari ini untuk kelas tertentu
SELECT 
    status, COUNT(*) as jumlah 
FROM attendance a
JOIN student s ON a.student_id = s.id
WHERE s.class_id = 1 AND a.date = CURRENT_DATE
GROUP BY status;
```
