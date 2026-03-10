# DOKUMENTASI DIAGRAM SISTEM (PLANTUML)

Dokumen ini berisi kode PlantUML untuk aplikasi **Sistem Absensi MI Aska Baitul Ulum**.

## 1. Use Case Diagram

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

rectangle "Sistem Absensi MI Aska Baitul Ulum" as Box {
  usecase "Input Absensi" as UC2
  usecase "Kelola Data Kelas & Siswa" as UC4
  usecase "Unduh Rekap Excel" as UC6
}

usecase "Logout" as UC5
usecase "Login" as UC1
actor "Guru" as G

' Connections
G -up-> UC1
G --> UC2
G --> UC4
G --> UC6

' Features include login
UC2 ..> UC1 : <<include>>
UC4 ..> UC1 : <<include>>
UC6 ..> UC1 : <<include>>

' Sequence: After features, just logout
UC2 --> UC5
UC4 --> UC5
UC6 --> UC5

' Layout positioning: Box (Left) -> Logout (Middle) -> G (Right)
Box -[hidden]right-> UC5
UC5 -[hidden]right-> G
UC1 -[hidden]down-> UC5
@enduml
```

## 2. Class Diagram

```plantuml
@startuml
left to right direction
skinparam classAttributeIconSize 0

class User {
  +username: String
  +full_name: String
  +role: String
}

class Class {
  +class_name: String
  +academic_year: String
}

class Student {
  +nisn: String
  +full_name: String
}

class Attendance {
  +date: Date
  +status: String
}

User "1" -- "0..*" Class
Class "1" -- "0..*" Student
Student "1" -- "0..*" Attendance
@enduml
```

## 3. Activity Diagram — Login

```plantuml
@startuml
|Input|
start
:Username;
:Password;
|Proses|
:Validasi Username & Password;
:Cek ke Database;
if (Valid?) then (Ya)
  :Buat Sesi Login;
  |Output|
  :Tampilan Dashboard;
  stop
else (Tidak)
  |Output|
  :Pesan Error Login;
  stop
endif
@enduml
```

## 4. Activity Diagram — Input Absensi

```plantuml
@startuml
|Input|
start
:Pilih Kelas;
:Pilih Tanggal;
:Status Kehadiran (H/S/I/A);
|Proses|
:Cek Data Siswa di Kelas;
:Simpan/Update Record Absensi;
|Output|
:Notifikasi Berhasil;
:Rekap Absensi Terupdate;
stop
@enduml
```

## 5. Activity Diagram — Kelola Data Kelas & Siswa

```plantuml
@startuml
|Input|
start
:Nama Kelas / Tahun Ajaran;
:NISN / Nama / Jenis Kelamin;
|Proses|
:Validasi Kelengkapan Data;
:Cek Duplikasi NISN;
if (Valid?) then (Ya)
  :Simpan ke Database;
  |Output|
  :Data Tersimpan;
  :Tampil di Daftar;
  stop
else (Tidak)
  |Output|
  :Pesan Error / Duplikat;
  stop
endif
@enduml
```

## 6. Activity Diagram — Logout

```plantuml
@startuml
|Input|
start
:Klik Tombol Logout;
|Proses|
:Hapus Sesi Login;
|Output|
:Redirect ke Halaman Login;
stop
@enduml
```
