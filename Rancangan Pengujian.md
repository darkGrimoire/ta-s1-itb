# Rancangan Pengujian
## Hal-hal penting dari Mayer dan Moons
**[Mayer]** Two important properties for making hidden operations of a language clearer to a novice:
1. Simplicity -> there should be a "small number of parts that interact in ways that can be easily understood"
2. Visibility -> novices should be able to view "selected parts and processes of the model 'in action'".

## Referensi Pengujian
### Mayer
Test Name: Effects of Models on Transfer Performance  
Cara pengujian:
1. Dikasih model diagram yang menjelaskan langkah eksekusi kode pemrograman
2. Dikasih manual yang menjelaskan perintah-perintah kode eksekusi
3. Disuruh baca manual selama 20-30 menit sesuai kecepatan membaca masing-masing
4. Dilakukan test yaitu:
   1. *Generate statement* -> Diberikan permasalahan dlm bahasa inggris lalu disuruh terjemahkan menjadi **satu baris** kode
   2. *generate nonloop* -> Diberikan permasalahan dlm bahasa inggris lalu disuruh terjemahkan menjadi program sederhana **tanpa pengulangan**
   3. *generate looping* -> Diberikan permasalahan dlm bahasa inggris lalu disuruh terjemahkan menjadi program sederhana **dengan pengulangan**
   4. *interpret statement* -> Diberikan kode **satu baris** lalu disuruh jelasin apa yang dilakukan kode tersebut
   5. *interpret nonloop* -> Diberikan kode **tanpa pengulangan** lalu disuruh jelasin apa yang dilakukan kode tersebut
   6. *interpret looping* -> Diberikan kode **dengan pengulangan** lalu disuruh jelasin apa yang dilakukan kode tersebut
5. Pakai p < .05, 20 orang per grup. Penilaian memakai idea unit.

### Moons
Test Name: Experimental Pilot Evaluation (understanding of the concept of recursion)  
Cara pengujian:
#### 2 Tahun pertama
1. Dikasih kode program yang ada metode perkalian secara rekursif. Penamaannya diacak sehingga tidak memberikan indikasi akhir dari program. Grup kontrol cuman dapet teks kode, sementara grup perlakuan diberikan visualisasi. Grup yang diberikan visualisasi telah menggunakan visualization environment dalam 5 lesson dengan masing-masing 4 jam pembelajaran.
2. Dikasih 2 kuesioner yg waktunya masing2 10 menit (34 orang):
   1. Kuesioner pertama pertanyaannya berupa jawaban deskriptif, seperti menjelaskan tujuan utama dari kode program. Gradingnya pakai SOLO Level.
   2. Kuesioner kedua pertanyaanya berupa numerik, seperti berapa kali suatu metode dipanggil, atau berapa banyak *stack frame* pada suatu waktu, atau apa isi dari suatu variabel pada akhir program. Gradingnya benar salah aja.

#### Tahun ke-3
Mirip kayak pengujian pertama, tapi kontrol grup dikasih Netbeans IDE trus jadi independent t-test

## Rencana Pengujian TA2
1. Jawab Kuesioner Identitas & Pengetahuan pemrograman saat ini
2. Penjelasan Materi
   1. **SCOPE**: Tipe Data, Expression, Control Flow, Functions & Modules (?)
   2. Di awal materi, jelasin dulu penggunaan visualisasi utk grup perlakuan
   3. Suruh belajar sampai babnya selesai semua dengan kecepatan masing2
3. Kasih soal pemrograman:
   1. Soal jenis pertama bertipe *generation* yang dilakukan pada autograder, ada minimal 1 soal untuk tiap bab (dinilai menggunakan *blackbox testing*)
   2. Soal jenis kedua bertipe *interpretation* yang dilakukan pada kuis, ada minimal 2 soal untuk tiap bab. Soal ini ada yang berupa deskriptif (dinilai menggunakan SOLO level) minimal 1 soal ada juga yang berupa numerik (dinilai menggunakan benar/salah) minimal 1 soal.

Utk cek interactivity: rate pencobaannya jadi lebih banyak, lebih sering berinteraksi dengan alat yang digunakan -> ukur waktu, jumlah interaksi, 
### Kebutuhan Pengujian
1. VBuat agar explanation stage dapat memuat komponen visualizer
2. VBuat agar lesson stage dapat memuat komponen autograder + visualizer
3. VBuat agar quiz stage dapat memuat komponen visualizer
4. Masukin materi BAB 1-5
5. Tambahin Logging waktu penyelesaian tiap stage, berapa kali ILE digunakan, 
6. VBuat agar visualizer dapat mendeteksi error
7. Buat agar visualizer dapat mengeluarkan hint
8. VBuat agar visualizer dapat memperlihatkan return value
9. Buat agar visualizer dapat memblokir import yang blacklisted
10. Buat agar visualizer dapat memperlihatkan perubahan variabel
11. Buat agar visualizer memiliki penjelasan yang beginner-friendly