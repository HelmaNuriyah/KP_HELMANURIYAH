# BAB V
# PENUTUP

Setelah melalui seluruh rangkaian tahapan Kerja Praktik, mulai dari observasi lapangan, analisis kebutuhan, perancangan sistem, hingga tahap implementasi dan pengujian pada Sistem Informasi Absensi Siswa MI Aska Baitul Ulum, maka pada bab ini penulis merangkum kesimpulan yang telah dicapai serta menyampaikan saran bagi pengembangan selanjutnya.

## V.1 Kesimpulan

Kesimpulan dari kegiatan Kerja Praktik ini dibagi menjadi dua aspek utama, yaitu aspek pelaksanaan kerja praktik dan aspek teknis substansi sistem yang dibangun.

### V.1.1 Kesimpulan Pelaksanaan Kerja Praktik

1.  Pelaksanaan Kerja Praktik di MI Aska Baitul Ulum telah berjalan sesuai rencana dan berhasil mengidentifikasi permasalahan krusial berupa ketidakefisienan proses rekapitulasi data kehadiran siswa yang masih bersifat manual (berbasis kertas).
2.  Penulis telah berhasil mengimplementasikan teori rekayasa perangkat lunak dan pemrograman web yang diperoleh selama perkuliahan ke dalam solusi nyata berupa aplikasi web "E-Presensi MI".
3.  Proses pengerjaan sistem membantu penulis dalam memahami dinamika lingkungan kerja profesional, kebutuhan manajemen administrasi di sekolah dasar (Madrasah Ibtidaiyah), serta pentingnya dokumentasi sistem yang baik.
4.  Interaksi dengan pihak madrasah memberikan wawasan mendalam mengenai bagaimana teknologi informasi dapat dimanfaatkan untuk meningkatkan efektivitas pemantauan kedisiplinan siswa secara real-time.

### V.1.2 Kesimpulan Substansi Sistem (E-Presensi MI)

1.  Telah berhasil dibangun sebuah aplikasi absensi berbasis web menggunakan framework **Flask (Python)** dan database **SQLite** yang dirancang khusus untuk kebutuhan MI Aska Baitul Ulum.
2.  Sistem menyediakan fungsionalitas manajemen data yang terstruktur, meliputi data Guru, Kelas, dan Siswa, serta proses pencatatan harian yang user-friendly dengan status kehadiran H, S, I, dan A.
3.  Fitur otomatisasi laporan dalam format **Microsoft Excel (.xlsx)** telah terintegrasi dengan baik menggunakan library Pandas, sehingga menghilangkan kebutuhan rekapitulasi manual oleh guru kelas.
4.  Berdasarkan hasil **Black Box Testing** yang meliputi pengujian login, input absensi, manajemen data, dan ekspor laporan, seluruh modul dinyatakan **valid** dan berjalan sesuai dengan spesifikasi fungsional yang telah ditetapkan.
5.  Aplikasi ini menjadi solusi digital yang mampu meningkatkan keamanan arsip dan mempercepat penyusunan laporan bulanan madrasah secara akurat.

## V.2 Saran

Untuk meningkatkan kualitas sistem dan keberlanjutan pemanfaatannya di masa mendatang, penulis menyampaikan beberapa saran sebagai berikut:

### V.2.1 Saran Pengembangan Sistem

1.  **Penguatan Keamanan**: Menambahkan fitur enkripsi password yang lebih kompleks dan pembatasan akses halaman yang lebih ketat berdasarkan *role-based access control* (RBAC) pada setiap endpoint.
2.  **Dashboard Visual**: Mengimplementasikan grafik statistik kehadiran menggunakan library Chart.js untuk memudahkan kepala madrasah dalam melakukan evaluasi tren kehadiran secara visual.
3.  **Integrasi Notifikasi**: Mengembangkan fitur notifikasi otomatis melalui WhatsApp atau Email kepada wali murid apabila siswa tidak hadir tanpa keterangan agar komunikasi sekolah-orang tua lebih efektif.
4.  **Optimalisasi Mobile**: Melakukan penyempurnaan pada antarmuka pengguna agar lebih responsif dan nyaman saat diakses melalui perangkat smartphone (Tabelt/HP) guru di kelas.
5.  **Manajemen Riwayat**: Menambahkan fitur filter laporan yang lebih detail berdasarkan rentang tanggal atau per-semester untuk memudahkan arsip jangka panjang.

### V.2.2 Saran Pelaksanaan Kerja Praktik

1.  **Bagi Mahasiswa**: Disarankan untuk melakukan observasi kebutuhan instansi secara lebih mendalam di awal waktu agar solusi yang ditawarkan benar-benar menjawab permasalahan yang paling mendesak di lapangan.
2.  **Bagi MI Aska Baitul Ulum**: Diharapkan pihak sekolah dapat menyediakan sarana infrastruktur jaringan yang stabil dan melakukan pelatihan singkat bagi seluruh guru agar pemanfaatan sistem absensi ini dapat berjalan optimal secara berkelanjutan.
3.  **Bagi Universitas Bale Bandung**: Disarankan untuk terus memperluas jaringan kerja sama dengan instansi pendidikan dasar (MI/SD) guna membuka peluang bagi mahasiswa dalam memberikan kontribusi teknologi bagi kemajuan pendidikan di tingkat dasar.

---
*— Akhir dari Laporan Kerja Praktik —*

