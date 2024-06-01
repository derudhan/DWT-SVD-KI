<h1>PANDUAN PENGGUNAAN</h1>
<h3>Melakukan Proses Embed</h3>
<b>Program ini dibuat menggunakan MATLAB R2024a dengan lisensi pelajar / mahasiswa.</b> <br>
Berikut ini merupakan cara untuk melakukan embedding pada program:<br>
1.	Unduh / clone folder dari Git https://github.com/hatedark/DWT-SVD-KI <br>
2.	Simpan dan buka pada MATLAB<br>
3.	Buka “embedding.m”<br>
4.	Masukkan path gambar host pada line 6 dan path gambar watermark pada line 23<br>
5.	Run projek dan hasilnya akan tersimpan pada folder “original”<br><br>

<h3>Melakukan Proses Extract</h3>
Berikut ini merupakan cara untuk melakukan extracting pada program:<br>
1.	Akses folder programnya di MATLAB<br>
2.	Buka “extracting.m”<br>
3.	Masukkan path gambar ber-watermark pada line 7, path gambar aslinya di line 24, dan path gambar watermarknya di line 40<br>
4.	Run projek dan hasilnya akan tersimpan pada folder “original”<br><br>

<h3>File program “attack.m” dan “fdisplay.m”</h3><br>
•	Program “attack.m” berfungsi untuk melakukan beberapa serangan yang sudah kami program untuk membantu dalam pengujian ketahanan watermark.<br>
Cara untuk menggunakannya yaitu dengan mengubah path pada line 4 dengan path gambar yang akan diserang.<br>
•	Program “fdisplay.m” berfungsi untuk membantu menampilkan gambar ber-watermark dan hasil ekstraknya berdampingan. Fungsi utama program ini hanya untuk membantu kami menampilkan hasil pengujian untuk dimasukkan ke dalam KTI kami.<br>
Selain itu juga, di akhir line terdapat fungsi untuk melakuakan perbandingan PNSR dan MSE dengan parameter pertama merupakan gambar utama dan parameter kedua untuk referensinya.<br>
