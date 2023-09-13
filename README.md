# Tugas 2 PBP
Nama    : Raisa Hannaliya Zahra

NPM     : 2206820503

Kelas   : PBP F

## 🔗 Link Deploy
https://latte-night.adaptable.app

## 1. Implementasi Checklist Step by Step
**a. Membuat proyek Django baru** 

Pada step ini, pertama saya inisiasi proyek dengan membuat *requirements.txt* pada direktori utama bernama "latte_night" yang sudah diinisiasi git, sudah terhubung pada repositori, dan virtual environment aktif (untuk mengisolasi dependencies antara proyek-proyek yang berbeda). Dependencies akan dipasang dengan perintah *pip install -r requirements.txt* pada cmd latte-night. Proyek akan diinisiasi dengan perintah *django-admin startproject latte_night .* dan langkah terakhir adalah melakukan konfigurasi proyek (mengganti akses ALLOWED_HOST agar bisa diakses banyak orang).


**b. Membuat aplikasi dengan nama main pada proyek tersebut**

Pada step ini, saya membuat aplikasi "main" dengan menjalankan perintah *python manage.py startapp main* pada cmd direktori utama dengan virtual environment yang telah aktif. Kemudian saya mendaftarkan aplikasi tersebut pada INSTALLED_APPS di *settings.py* pada direktori proyek "latte_night" (yang berada dalam direktori utama) agar aplikasi terbaca dan dapat terakses pada proyek.


**c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main**

Pada step ini, saya akan menghubungkan proyek dengan tampilan "main". Saya memodifikasi *urls.py* pada direktori proyek "latte_night". Di dalamnya, saya mengimpor rute URL dari aplikasi main dengan fungsi include ke dalam berkas ini dan path 'main/' akan diarahkan ke rute yang didefinisikan tersebut. Note: *urls.py* pada proyek mengarahkan rute URL tingkat proyek dan dapat mengimpor rute URL dari berkas *urls.py* aplikasi-aplikasi (dalam step ini, aplikasi main), memungkinkan aplikasi dalam proyek Django untuk bersifat modular dan terpisah.


**d. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib name, amount, description**

Pada step ini, saya memodifikasi *models.py* dalam direktori aplikasi "main" dengan membuat class nya bernama "Item(models.Model)" sebagai kelas dasar untuk mendefinisikan model Django dengan inisiasi atribut name, amount, description, price, category, coffee_bean yang memiliki tipe data field masing-masing. Selain itu saya juga menambahkan fungsi untuk mengecek stock item dan mencetak message order sesuai category item. Untuk mengubah struktur tabel basis data (pada setiap perubahan model), saya melakukan migrasi model dengan *python manage.py makemigrations* untuk menciptakan berkas migrasi perubahan (otomatis akan terbuat direktori migrations dalam direktori aplikasi) dan *python manage.py migrate* untuk mengaplikasikan berkas tersebut ke basis data.


**e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**

Pada step ini, saya memodifikasi berkas *views.py* yang mengimport fungsi render untuk tampilan HTML. Saya tambahkan fungsi show_main dengan parameter request untuk return tampilan HTML yang sesuai. Di dalamnya, saya tambahkan dictionary context berisi nama dan kelas yang valuenya akan di-return pada tampilan HTML. Pada statement return, terdapat argumen request(sesuai fungsi), main.html (file template HTML), dan context. Kemudian di template HTML *main.html* yang telah dibuat, saya akan panggil keys dari context untuk return valuenya ex: -> {{ name }} akan return value key name pada *views.py*. Sedangkan nama aplikasi akan muncul sebagai heading 1 dari file HTML (bukan dari fungsi).


**f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**

Pada step ini, saya akan mengatur rute URL spesifik fitur-fitur aplikasi. Saya memodifikasi *urls.py* pada direktori aplikasi main. Di dalamnya, saya mengimpor fungsi show_main dari *main.views* sebagai tampilan URL yang diakses. Pada variabel urlpatterns, path akan memiliki argumen berupa pola URL yang mencakup fungsi import-an, dan namanya untuk dicantumkan dalam pola. Dalam file ini juga saya memberikan nama unik pada pola URL sesuai nama aplikasi saya yaitu 'main'. 


**g. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**

Sebelum memulai, pastikan seluruh perubahan telah dipush ke repositori github. Untuk melakukan deploy, pertama saya membuat app baru terlebih dahulu yang dihubungkan dengan repositori proyek saya dan melakukan inisiasi dasar (perintah Start Command akan menjadi python manage.py migrate && gunicorn latte_night.wsgi) hingga tahap deploy. Ketika ada perubahan atau ingin men-trigger proses deployment agar aplikasi dapat ter-update di Adaptable, saya akan melakukan git add, commit, dan push.


## 2. Bagan Request dan Penjelasan
![Bagan Request Client to Django App](https://github.com/raisahzr/latte-night/assets/119391721/f78165df-4a23-4b03-a88b-b53330b2da19)
*note: main.html hanya contoh nama dokumen sesuai aplikasi tugas

Django sering direferensikan sebagai MTV (Model, Template, View) framework. Alurnya adalah klien akan mengakses web apilkasi dengan mengirim permintaan HTTP ke URL tertentu. Django memungkinkan untuk memisahkan dan merutekan tugas-tugas dalam pengembangan web: URLs ditangani oleh *urls.py*, logika bisnis oleh *views.py*, representasi data oleh *models.py*, dan tampilan oleh *main.html*. Request akan dihubungkan dengan *views.py* pada tahap URL routing pada *urls.py*. Berkas *views.py* kemudian akan memproses logika aplikasi dan request klien. Pada tahap ini *views.py* bisa berinteraksi degan *models.py* untuk membaca dan menulis data, dan model sebagai representasi data aplikasi dapat berinteraksi dengan database jika diperlukan. Selain itu, *views.py* juga akan merender tampilan HTML yang sesuai berdasarkan berkas *main.html*. Tahap terakhir, respons akhir akan dikirimkan kembali ke klien, berupa data HTML yang akan ditampikan browser klien.


## 3. Virtual Environment Django
Virtual environment (venv) adalah lingkungan terisolasi yang dibuat dalam sistem operasi untuk mengisolasi proyek perangkat lunak Python dari instalasi Python sistem yang ada. Virtual environment mampu membuat lingkungan Python yang terisolasi, karena setiap venv dapat memiliki paket Python yang berbeda dan versi paket yang berbeda sehingga dapat mengisolasi dependensi antar proyek. Virtual environment juga memungkinkan kita untuk memiliki dependensi dan paket Python yang berbeda untuk setiap proyek tanpa konflik atau campur tangan dengan proyek Python lainnya yang berjalan pada komputer yang sama (membuat file *requirements.txt* yang berisi daftar semua paket yang dibutuhkan oleh proyek). Terakhir, venv dapat membuat lingkungan virtual di satu mesin dan menggunakannya di mesin lain tanpa perlu menginstal ulang semua dependensi. Tools ini sangat berguna dalam pengembangan perangkat lunak Python yang lebih besar dan kompleks.

Kita tetap bisa membuat aplikasi web berbasis Django meski kita tidak menggunakan virtual environment, tetapi kita harus sangat berhati-hati dalam mengelola dependensi proyek dan memastikan bahwa proyek-proyek yang berbeda tidak mengganggu satu sama lain dalam hal dependensi Python. 


## 4. MVC, MVT, MVVM
MVC, MVT, dan MVVM adalah tiga pola desain (design pattern) yang umum digunakan dalam pengembangan perangkat lunak, terutama dalam konteks pengembangan aplikasi berbasis web dan perangkat lunak berbasis antarmuka pengguna (UI). Ketiganya memiliki tujuan yang sama, yaitu untuk memisahkan tugas-tugas yang berbeda dalam pengembangan perangkat lunak agar kode menjadi lebih terstruktur, mudah dimengerti, dan mudah untuk dikelola.

Dalam MVC, MVT, dan MVVM, ketiganya memiliki 2 komponen yang sama yaitu Model dan View. Model mewakili data dan logika bisnis dari aplikasi. Model bertanggung jawab untuk mengelola data, melakukan operasi terhadap data, dan memberikan data kepada komponen lain dalam pola desain. Sedangkan View merupakan tampilan atau antarmuka pengguna dari aplikasi. View bertanggung jawab untuk menampilkan informasi kepada pengguna dan menerima input dari pengguna.

Perbedaan ketiganya terletak pada komponen terakhir. Pada MVC (Model-View-Controller), Controller bertindak sebagai perantara antara Model dan View. Controller menerima input dari pengguna melalui View, memproses input tersebut, berinteraksi dengan Model untuk mengambil atau memperbarui data, dan kemudian memperbarui View dengan hasilnya. Pada MVT (Model-View-Template), Template adalah file yang menggabungkan logika pengambilan data dari Model dengan tampilan yang akan ditampilkan kepada pengguna. Dalam kerangka kerja seperti Django (yang menggunakan MVT), template adalah bagian yang mengendalikan presentasi data. Sedangkan pada MVVM (Model-View-ViewModel), ViewModel bertindak sebagai perantara antara Model dan View. ViewModel mengkonversi data dari Model menjadi format yang dapat ditampilkan oleh View. Ini memungkinkan View untuk lebih fokus pada tampilan, sementara logika yang terkait dengan tampilan tetap terpisah dalam ViewModel.

Berdasarkan paparan di atas, dapat disimpulan perbedaan utama MVC adalah pemisahan yang jelas antara Model, View, dan Controller. Hal ini memungkinkan pengembang untuk mengganti atau memodifikasi satu bagian tanpa harus mengganggu yang lain. Perbedaan utama MVT adalah penggunaan Template sebagai pengendali logika tampilan, sementara Controller dalam MVC mengendalikan logika pengendali. Sedangkan perbedaan utama MVVM adalah penggunaan ViewModel untuk mengelola logika tampilan, sehingga memisahkan tampilan dengan cara yang lebih terstruktur dan menghindari logika tampilan yang kompleks di dalam View.

Pilihan antara MVC, MVT, atau MVVM bergantung pada bahasa pemrograman, platform, dan kerangka kerja yang kita gunakan, serta kompleksitas proyek. Tujuannya adalah memisahkan tugas-tugas dalam pengembangan perangkat lunak agar kode lebih mudah dikelola dan dipelihara. 
