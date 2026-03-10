# Konsep Sistem Absensi Siswa MI Aska Baitul Ulum Berbasis Web (E-Presensi MI)

## 1. Pendahuluan
Sistem Absensi Siswa MI Aska Baitul Ulum Berbasis Web adalah solusi digital untuk mencatat, mengelola, dan memantau kehadiran siswa secara real-time. Sistem ini dirancang untuk menggantikan absensi manual kertas agar lebih efisien, akurat, dan transparan bagi pihak madrasah maupun wali murid.

## 2. Target Pengguna
1.  **Administrator (Tata Usaha)**: Mengelola data madrasah, kelas, guru, dan siswa secara keseluruhan.
2.  **Guru Kelas**: Melakukan input absensi setiap hari dan melihat rekapitulasi kelas yang diampunya.
3.  **Wali Murid**: Dapat memantau kehadiran anak mereka melalui laporan yang dihasilkan.
4.  **Kepala Madrasah**: Memantau statistik kehadiran seluruh madrasah sebagai bahan evaluasi.

## 3. Fitur Utama
### A. Manajemen Data (CRUD)
- Data Siswa (Nama, NISN, Jenis Kelamin, Kelas).
- Data Guru & Kelas.
- Data Tahun Ajaran.

### B. Proses Absensi (Daily Logging)
- **Manual Check**: Guru memilih status hadir di dashboard kelas.
- **Kategori Kehadiran**: Hadir (H), Sakit (S), Izin (I), Alpa (A).

### C. Dashboard & Visualisasi
- Statistik kehadiran harian di Dashboard.
- Persentase kehadiran siswa secara otomatis.

### D. Rekapitulasi & Laporan
- Export laporan ke format Excel (.xlsx) per kelas.
- Rekap data kehadiran siswa untuk arsip administrasi.

## 4. Keunggulan Sistem
- **User-Friendly**: Antarmuka modern (Outfit Font) yang mudah digunakan oleh guru.
- **Real-Time System**: Data langsung tersimpan di database segera setelah diinput.
- **Responsif**: Dapat diakses melalui Laptop, Tablet, maupun Smartphone.

## 5. Arsitektur Teknologi
- **Frontend**: HTML5, Vanilla CSS3 (Modern UI), Bootstrap (Optional).
- **Backend**: Python (Flask).
- **Database**: SQLite.
- **Keamanan**: Authentication dengan Flask-Login.

## 6. Struktur Project
```text
/aplikasi-kp
├── /static (CSS/JS)
├── /templates (HTML Pages)
├── app.py (Main Application)
├── models.py (Database Models)
└── /instance (Database File)
```
