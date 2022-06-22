Pembelajaran Pemrograman Secara Daring Menggunakan Coding Interface


# Kerangka Pikiran
### 1. Pembelajaran
  - Apa itu pembelajaran?
    -> Robert E. Slavin. 2000. Educational Psychology: Theory and Practice.Pearson Education. New Jersey.
    Belajar adalah perubahan yang relatif permanen dalam perilaku atau potensi perilaku sebagai hasil dari pengalaman atau latihan yang diperkuat. Belajar merupakan akibat adanya interaksi antara stimulus dan respons. [Seseorang dianggap telah belajar sesuatu jika dia dapat menunjukkan perubahan perilakunya. Menurut teori ini, dalam belajar yang penting adalah input yang berupa stimulus dan output yang berupa respons.]

    -> Gagne, R.M, (1977). The Conditions of Learning, New York: Holt, Renehart and Winston.
    Salah satu pengertian pembelajararan dikemukakan oleh Gagne (1977) yaitu pembelajaran adalah seperangkat peristiwa -peristiwa eksternal yang dirancang untuk mendukung beberapa proses belajar yang bersifat internal. Lebih lanjut, Gagne (1985) mengemukakan teorinya lebih lengkap dengan mengatakan bahwa pembelajaran dimaksudkan untuk menghasilkan belajar, situasi eksternal harus dirancang sedemikian rupa untuk mengaktifkan, mendukung, dan mempertahankan proses internal yang terdapat dalam setiap peristiwa belajar. 

    -> 
    

  - Siapa yang melakukan pembelajaran?
    + Usia produktif untuk belajar
    + Semua orang bisa belajar
  - Dimana melakukan pembelajaran?
  - Kenapa melakukan pembelajaran?
  - Bagaimana cara melakukan pembelajaran
    + Luring -> Formal (Sekolah, Kampus) & Informal (Buku, Les, Bootcamp)
    + Daring -> Webinar, Video, Artikel/Dokumentasi, Soal2, ...
### 2. Pemrograman
  - Apa?
    + Sejarah pemrograman
    + Jenis2 pemrograman
  - Siapa?
    + ??? Pemrogram terkenal?
  - Dimana?
    + ??? tempat dipakainya?
  - Kenapa?
    + Cari aja kenapa perlu pemrograman
  - Bagaimana?
    + Belajar dari beragam hal seperti yang sudah disebutkan di bagian sebelumnya.
### 3. Pembelajaran Pemrograman secara Daring
  - Kenapa secara daring?
  - Bagaimana pembelajarannya?
  - Ada apa saja?
    + Merk2nya beserta media pembelajaran yang mereka gunakan
    + Perbandingan konten materi, harga, pengguna
    + Feedback orang-orang
### 4. Coding Interface
  - Apa?
  - Siapa?
    + Platform2 yg memakai coding interface (musti sebutin ulang gak?)
  - Kenapa?
    + Pros Cons memakai Coding Interfaces
  - Bagaimana?
    + Kasih tau overview implementasinya bagaimana dan butuh apa aja
### 5. Kontainer Eksekutor (Docker)
  - Apa?
    + Sejarah?
  - Kenapa?
    + Pros & Cons
    + Kegunaan: Media Isolasi
  - Bagaimana?
    + Cara memakai Docker
    + Penggunaan Docker dalam membuat Coding Interface
### 6. Orkestrasi Kontainer (Kubernetes)
  - Apa?
    + Sejarah?
  - Kenapa?
    + Load Balancing
    + Distribusi workload
    + SoC (Separation of Concern tiap materi/course/soal)
  - Bagaimana?
    + Cara memakai Kubernetes
### 7. Komunikasi Frontend-Backend (Websocket)
  - Apa?
    + Sejarah HTTP lalu lanjut ke websocket
    + Kasih tau juga alternatif websocket kayak SSE, EventSource
    + Banyak yang pakai websocket
  - Kenapa?
    + Realtime
    + Kustomisasi
    + Keamanan
  - Bagaimana?
### 8. Keamanan Eksekusi
  - Perlu sampe sini gasi? WKWKKWKWK


# Daftar Pertanyaan
- Untuk tujuan, bagaimana wording yang tepat apabila saya ingin membuat ILE serta mendapatkan feedback dari ILE tersebut?
cari paper terkait pengujian pembelajaran pemrograman
- Saya sebenarnya ingin menggabungkan solusi pada pythontutor serta web ide seperti pada katacoda. Kira-kira bisa dibahas dimana?
coba dikasih hint terlebih dahulu sebelum dikasih visualisasi
- Pembahasan KodeBareng ditaruh dimana?
ditaro di BAB 2, dikaitkan dengan ILE, lalu di BAB 3 dikaitkan dengan lampiran requirementnya.
- Terkait deadline M1 yaitu besok, bahasannya mengenai Analisis Penyelesaian Masalah. Kira-kira bagaimana cara mempertajam analisis masalah yang sudah dilakukan di TA1 karena ketika seminar kemarin kurang terbahas?
- Terkait rancangan solusi sistem, apakah perlu diberikan penjelasan terkait teknis2 yang dipakai di BAB 2 atau bisa langsung dimasukkan saja pada BAB 3?
dibuat satu dokumen sama mario, dihighlight yang bagian faris di buku tapi di lampirannya disamakan saja.

# Catatan Bimbingan
Bikin dokumen requirement buat KodeBareng, digabungkan dengan Mario. Tapi yang dibahas di buku cuman yang punya masing2.
Cari masalah di segmen usernya dari psikologi dsb, dari paper
Pengujiannya bisa dikomparasi
cari bagaimana mengukur ILE dari paper2
cari tahu terkait inquiry learning
Coba dicari hubungan dengan gamifikasi, secara user experience. Jangan sampai gamifikasi rupanya dependensi terhadap ILE atau bahkan ILE membutuhkan gamifikasi
progress report tiap minggu, bentar aja.

# REVISI SIDANG
- [ ] Ubah User/Frontend jadi Siswa/Pengguna
  - Tinggal ubah di Use Case
- [ ] Use Case pengguna harus merefer ke pembelajar/admin
  - Tinggal ubah kata pengguna jadi Siswa
- [ ] Use case lama harusnya ada di bab 2
  - Tinggal pindahin usecasenya
- [ ] Disebutkan banyak peluang ILE pada Choy & Eng, akan tetapi hanya sebagian saja yang diaplikasikan.
  - Jelasin kenapa kamu mengaplikasikan yang latihan kode praktis
- [ ] Simpulan dan saran harus ada kuantifikasi dan berdasarkan hasil pengujian, jangan pakai bahasa bisnis
  - Masukin aja angka2nya ke kesimpulan
- [ ] Tabel font spasi kecil & 1 spasi & header + caption hrus direpeat
  - Tinggal pake \small, >{\baselineskip} sama caption masukin ke luar firsthead
- [ ] Diagram terlalu kecil, kalau ada yang kekecilan bisa agak makan margin ke kanan
  - Pake adjustbox buat bisa keluar margin
- [ ] Alur pembelajaran ILE yg kuning hrus dijelasin legendanya
  - Masukin legenda ke activity diagram
- [ ] Harus dijelaskan bagaimana rumusan masalah terhadap kondisi KodeBareng, bagaimana hasil akhir dlm menyelesaikan (kaitin KodeBareng ke dalam bab 1)
  - Masukin KodeBareng ke dalam Latar Belakang, Rumusan Masalah, dan Tujuan
- [ ] Perlu pendefinisian ILE yang lebih konkrit dan harus jelas definisi kontribusi ILE dan definisi konkrit
  - Jelasin ILE macam apa yang mau diimplementasikan, jelasin juga KodeBareng sebenarnya termasuk ILE tapi kamu pengen buat ILE yang lebih spesifik yaitu visualisasi eksekusi kode. 
  - Taro di bab 2, buat sub-bab mengenai visualisasi eksekusi kode, lalu refer di bab 3 kamu mau buat yang kayak gimana
- [ ] Perlu disampaikan existing ILE pada KodeBareng di Bab 2
  - Jelasin di KodeBareng ILEnya yang sekarang kayak gimana, struktur kelas dsbnya jelasin dan kasih gambar
- [ ] Sehingga perlu jelasin bagaimana dari KB yang perlu diperbaiki berdasarkan masukan dari pengguna
  - Jelasin kekurangan dari ILE KodeBareng yang sekarang
- [ ] 2.2 Harus melakukan tabel komparasi dari tools/tempat lain yang bisa diadaptasi ke KodeBareng utk perbaikan KodeBareng
  - Masukin dulu tiap ILE di platform lain kayak gimana pros/consnya, lalu buat tabel komparasi apa yang mau diambil buat KodeBareng
- [ ] Perlu analisis bagaimana konsep yang diimplementasi, tidak hanya sekedar dilist
  - Jelasin konsepnya diambil dari Moons de Backer yang diubah menyesuaikan bahasa Python, lalu jelasin kenapa mengimplementasikan poin2 yang di tabel itu (untuk pemula)
- [ ] Harus ada elaborasi bagaimana tools dirancang dan bukan hasil akhirnya saja.
  - Jelasin hasil eksplorasi PDB, kasih penjelasan terkait activity diagram Parser dan Executor.
  - Hasil eksplorasi PDB bisa berupa command apa saja yang bisa dieksekusi, bagaimana hasil keluarannya, dsb. Nanti di komponen Parser dan Executor tinggal refer input/output apa yang harus dipakai
- [ ] Perlu ada penjelasan teknis bagaimana keluaran PDB diproses sehingga menghasilkan visualisasi
  - Dari hasil eksplorasi, masukin penjelasannya di komponen Parser