Nama    : Raisa Hannaliya Zahra

NPM     : 2206820503

Kelas   : PBP F

## 🔗 Link Deploy
https://latte-night.adaptable.app


<details open>
<summary>Tugas 2</summary>
<br>
    
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
</details>

<details>
<summary>Tugas 3</summary>
<br>
    
## 1. Apa perbedaan antara form POST dan form GET dalam Django?
Dalam Django, kita dapat menggunakan metode HTTP POST dan GET untuk mengirim data antara browser pengguna dan server Django. Form POST digunakan untuk mengirim data yang dapat mengubah status server (misalnya perubahan di database), sedangkan Form GET digunakan untuk mengambil data untuk diproses dalam bentuk URL tanpa mengubah status server. Perbedaan utama keduanya adalah metode pengiriman data, di mana Form POST mengirimkan data secara tersembunyi dalam badan permintaan HTTP, sedangkan Form GET mengirimkan data melalui URL sebagai parameter query string. Dari sini kita juga dapat melihat bahwa dari segi keamanan, Form POST dianggap lebih aman untuk mengirim data yang sensitif daripada Form GET yang datanya terlihat dalam URL. Selain itu, dari segi kapasitas data, Form POST dapat mengirimkan data yang lebih besar daripada Form GET karena data dikirim sebagai bagian dari badan permintaan HTTP dan ukurannya tidak dibatasi oleh batas URL.


## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML, JSON, dan HTML adalah tiga format yang berbeda yang sering digunakan dalam konteks pengiriman data di lingkungan web dan pemrograman. XML, yang merupakan singkatan dari eXtensible Markup Language, digunakan untuk menyusun data dalam struktur hierarki dengan menggunakan elemen, atribut, dan tag. Tujuan utama XML adalah merepresentasikan dan menukar data antar aplikasi atau sistem, sering digunakan dalam pertukaran data antar sistem yang berbeda atau untuk menyimpan konfigurasi dan struktur data. Namun, XML memerlukan parser XML untuk membaca dan memproses data, dan tidak memiliki tipe data bawaan, sehingga Anda harus mendefinisikan tipe data Anda sendiri menggunakan DTD atau XML Schema.

Di sisi lain, JSON (JavaScript Object Notation) adalah format pertukaran data yang berbasis teks dan mengorganisasi data dalam bentuk objek dan array. JSON lebih sederhana dan lebih mudah dibaca daripada XML, sehingga sangat populer dalam pengiriman data dari server ke klien dan antar aplikasi web. Ini menjadi pilihan utama dalam pengembangan RESTful API. JSON juga mudah diproses menggunakan JavaScript atau bahasa pemrograman lainnya yang mendukung JSON, yang menjadikannya sangat cocok untuk pengembangan aplikasi web. JSON mendukung tipe data dasar seperti string, angka, boolean, objek, dan array, membuatnya sangat fleksibel.

Sementara itu, HTML (HyperText Markup Language) memiliki peran yang berbeda. HTML adalah bahasa markup yang digunakan untuk membuat struktur tampilan halaman web, dengan fokus pada tampilan dan presentasi data. Ini tidak digunakan secara langsung untuk pertukaran data, tetapi untuk membuat halaman web yang dapat ditampilkan di peramban web. HTML mendefinisikan struktur tampilan, teks, gambar, tautan, dan elemen-elemen lain yang diperlukan untuk halaman web interaktif. Data dalam HTML diinterpretasikan oleh peramban web untuk membuat tampilan yang dapat dilihat oleh pengguna.

Dengan demikian, XML, JSON, dan HTML memiliki peran yang berbeda dalam pengembangan web dan pemrograman, masing-masing digunakan sesuai dengan kebutuhan dan tujuan aplikasi yang diinginkan.


## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON (JavaScript Object Notation) sering menjadi pilihan utama dalam pertukaran data antara aplikasi web modern karena sejumlah keunggulannya yang sangat relevan dengan tuntutan pengembangan web yang dinamis dan efisien. Pertama, JSON memiliki struktur data yang sederhana dan mudah dibaca oleh manusia, memberikan transparansi dan kemudahan pemahaman yang penting dalam lingkungan web yang terus berubah. Kemudian, JSON mudah diproses oleh banyak bahasa pemrograman, dengan dukungan bawaan atau pustaka JSON yang memungkinkan penguraian dan pembuatan data JSON dengan mudah.

Selain itu, JSON mendukung struktur data yang fleksibel, mengizinkan pengembang untuk menyusun data yang kompleks dan terstruktur sesuai dengan kebutuhan aplikasi. Keberadaannya yang erat terkait dengan JavaScript, bahasa pemrograman yang dominan dalam pengembangan web, memungkinkan data JSON dapat langsung digunakan dalam kode JavaScript tanpa perlu parsing tambahan.

JSON juga sangat cocok untuk pengembangan API berbasis RESTful, yang umum digunakan dalam interaksi antara aplikasi web. Format JSON yang ringan dan fleksibel memudahkan pengiriman dan penerimaan data sesuai dengan permintaan HTTP. JSON juga mendukung penanaman (nesting) data, memfasilitasi representasi data yang kompleks seperti objek bersarang atau daftar yang rumit.

Terakhir, JSON kompatibel dengan berbagai perangkat dan platform, termasuk peramban web, perangkat seluler, dan server web, sehingga menjadikannya ideal untuk pertukaran data lintas platform. Dukungan yang luas dari komunitas pengembang dan statusnya sebagai standar de facto dalam pertukaran data di web semakin mengukuhkan JSON sebagai pilihan yang sangat populer dalam pertukaran data antara aplikasi web modern. Ini memungkinkan pengembang untuk secara efisien mengirim, menerima, dan memproses data dalam lingkungan web yang dinamis saat ini.


## 4. Implementasi Checklist Step by Step
**a. Membuat input form untuk menambahkan objek model pada app sebelumnya** 
Sebelum membuat form, saya pastikan telah membuat skeleton sebagai kerangka views yaitu `base.html` pada direktori utama dan mengimplementasikan template tersebut pada `main.html`. Kemudian pada `settings.py` direktori proyek, bagian TEMPLATES, ubah menjadi 'DIRS': [BASE_DIR / 'templates'] agar `base.html` terdeteksi. Untuk membuat form, saya membuat berkas baru `forms.py` pada direktori aplikasi main (import model aplikasi). Di dalam kelasnya, saya menyatakan "Item", yaitu model saya, sebagai model yanag digunakan untuk form sehingga ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Item. Field dari model Item yang saya gunakan untuk form mencakup "name", "amount", "description", "price", "category" (coffee/non-coffee). 

Untuk menampilkan dan mengolah input forms user pada web saya, pertama saya menambahkan beberapa import pada `views.py` (django.http import HttpResponseRedirect, main.forms import ProductForm, django.urls import reverse) dan mendefinisikan sebuah fungsi baru yaitu create_product dengan parameter request. 
- form = ProductForm(request.POST or None) digunakan untuk membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.
- form.is_valid() digunakan untuk memvalidasi isi input dari form tersebut.
- form.save() digunakan untuk membuat dan menyimpan data dari form tersebut.
- return HttpResponseRedirect(reverse('main:show_main')) digunakan untuk melakukan redirect setelah data form berhasil disimpan.

**b. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID**
HTML
Pada berkas `views.py` fungsi show_main saya mengambil seluruh objek Item dengan items = Item.objects.all() dan 'items' : item untuk dibaca pada tabel nantinya. Kemudian lakukan routing pada `urls.py` untuk halaman create_product. Selanjutnya saya membuat HTML baru dengan nama `create_product.html` pada direktori templates aplikasi. Step ini berfungsi untuk membuat kerangka tampilan halaman create_product (tetap menggunakan `base.html` sebagai template utama). Di dalamnya mencakup tampilan fields form sebagai tabel, tombol submit untuk mengirim request ke `views.py`, dan menyatakan form method untuk menandakan block form dengan metode POST. Pada `main.html`, saya membuat tabel dengan iterasi object Item yang sudah tersimpan untuk ditampilkan sebagai tabel.

XML DAN JSON
Import HttpResponse dan Serializer pada `views.py` direktori aplikasi kemudian buatlah fungsi show_xml dan show_json yang menerima parameter request dan berisi variabel "data" yang menyimpan hasil query dari seluruh data yang ada pada Item. Tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML. serializers digunakan untuk translate objek model menjadi format lain.
def [show_xml/show_json](request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("[xml/json]", data), content_type="application/[xml/json]")

XML BY ID DAN JSON BY ID
Proses import dan pembuatan fungsi kurang lebih sama dengan XML dan JSON sebelumnya, hanya saja variabel "data" yang dinyatakan menyimpan hasil query dari data dengan id tertentu yang ada pada Item.
data = Item.objects.filter(pk=id)
Sedangkan parameter dan return type yang digunakan tetap sama dengan nama fungsi show_xml_by_id/show_json_by_id

**c. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin**
Pada proses ini, pertama saya mengimport semua fungsi tambahan pada poin b yang telah dibuat di dalam *views.html* pada file `urls.py`, kemudian menambahkan parh url ke dalam urlpatterns untuk mengakses fungsi-fungsi yang telah diimpor dengan format path('[nama format]/', [nama fungsi], name='[nama fungsi]'). Untuk XML by ID dan JSON by ID, bentuk format linknya adalah '[xml/json]/<int:id>/'. Kemudian hasilnya dapat dilihat dengan runserver dan membuka link http://localhost:8000/[format data].


## 5. Screenshot hasil akses URL pada postman
- HTML
  ![html](https://github.com/raisahzr/latte-night/assets/119391721/9cafbc77-e0ca-471a-8246-9a6393eaec97)

- XML
  ![xml](https://github.com/raisahzr/latte-night/assets/119391721/06e3c6ae-85af-4a81-b443-ea13e6b91b2d)

- JSON
  ![json](https://github.com/raisahzr/latte-night/assets/119391721/b3370475-6620-4eeb-8ece-b5f122107c49)
  
- XML BY ID
  ![xml by id](https://github.com/raisahzr/latte-night/assets/119391721/1abae373-b30c-4000-ae81-6edca1344659)

- JSON BY ID
  ![json by id](https://github.com/raisahzr/latte-night/assets/119391721/5c2f7fc3-0ef3-4ab4-b3de-ace16c83343d)

## 5. Bonus
Untuk menambahkan pesan yang menunjukkan berapa Item yang disimpan dalam sistem, pada `main/html` saya menambahkan "Current inventory: {{item_amount}} drinks menu stored" di mana variabel item_amount dinyatakan sebagai:

'item_amount' : item.count(),

pada context di berkas `views.py`
</details>

<details open>
<summary>Tugas 4</summary>
<br>

## 1. Django UserCreationForm, kelebihan dan kekurangannya
`UserCreationForm` adalah salah satu bentuk yang disediakan oleh Django dalam modul django.contrib.auth.forms untuk memudahkan pembuatan dan pendaftaran pengguna baru dalam aplikasi web Django yang melibatkan otentikasi pengguna. Form ini digunakan untuk mengumpulkan data yang diperlukan untuk membuat pengguna baru seperti nama pengguna (username), password, dan konfirmasi password. Ini adalah salah satu cara yang umum digunakan untuk membuat formulir pendaftaran pengguna dalam proyek Django.

| Kelebihan | Kekurangan |
| --- | --- |
| Mudah digunakan | ustomisasi terbatas untuk kompleksitas lebih tinggi |
| Sudah ada validasi bawaan | Tampilan default HTML mungkin tidak sesuai dan harus membuat template sendiri |
| Sudah terintegrasi dengan Django Authentication | Perlu memastikan keamanannya |


## 2. Perbedaan dan pentingnya autentikasi dan otorisasi
Dalam konteks Django, autentikasi dan otorisasi adalah dua konsep penting yang berhubungan dengan keamanan dan kontrol akses dalam aplikasi web. Meskipun keduanya terkait dengan perlindungan data dan sumber daya, mereka memiliki perbedaan yang signifikan dalam fungsinya.

Autentikasi mengacu pada proses verifikasi identitas pengguna. Ini adalah langkah pertama yang harus dilakukan ketika seorang pengguna mencoba mengakses aplikasi web atau sumber daya tertentu di dalamnya. Tujuannya adalah untuk memastikan bahwa pengguna yang mengklaim identitasnya (seperti dengan nama pengguna dan kata sandi) adalah pengguna yang sebenarnya. Dalam konteks Django, autentikasi biasanya dilakukan dengan mengidentifikasi pengguna berdasarkan informasi akun mereka, seperti nama pengguna dan kata sandi, dan memeriksa apakah kombinasi tersebut sesuai dengan yang ada di database. Django memiliki sistem autentikasi yang kuat dan fleksibel yang dapat dengan mudah diintegrasikan ke dalam proyek.

Sedangkan, otorisasi adalah proses yang berikutnya setelah autentikasi dan berhubungan dengan mengendalikan akses pengguna terhadap sumber daya atau fitur tertentu dalam aplikasi. Ini adalah tentang menentukan apa yang diizinkan atau tidak diizinkan untuk pengguna setelah mereka berhasil terautentikasi. Dalam Django, otorisasi dapat diimplementasikan melalui penggunaan decorator seperti `@login_required` atau menggunakan perizinan (permissions) yang diberikan pada model atau view tertentu. Otorisasi memeriksa apakah pengguna yang terautentikasi memiliki izin atau hak akses yang sesuai untuk melakukan tindakan tertentu seperti membaca, menulis, atau menghapus data.

Pentingnya untuk menerapakan keduanya adalah melindungi keamanan data sensitif sehingga hanya pengguna terdaftar yang bisa mengakses, menjaga privasi pengguna dengan data pribadi yang terdaftar, melindungi aplikasi dari tindakan berbahaya dari luar, dan memenuhi persyaratan hukum/regulasi perlindungan akses data pribadi.


## 3. Cookies dalam konteks aplikasi web dan penggunaan cookies untuk mengelola data sesi pengguna oleh Django
Cookies dalam konteks aplikasi web adalah data kecil yang disimpan di perangkat pengguna saat mereka berinteraksi dengan sebuah situs web. Cookies digunakan untuk menyimpan informasi yang dapat diakses oleh situs web tersebut saat pengguna kembali mengunjungi situs tersebut di masa mendatang. Dalam Django, cookies digunakan untuk mengelola data sesi pengguna. Django menciptakan ID sesi unik untuk setiap pengguna dan menyimpannya dalam cookie di perangkat pengguna. ID sesi ini mengidentifikasi pengguna saat mereka berinteraksi dengan situs web, sementara data sesi sebenarnya disimpan di server Django. Ketika pengguna mengakses situs web, server akan menggunakan ID sesi dalam cookie untuk mengambil dan memodifikasi data sesi yang sesuai. Ini memungkinkan Django untuk menjaga status dan preferensi pengguna di seluruh sesi mereka tanpa perlu menyimpan data sensitif di perangkat pengguna.


## 4. Keamanan penggunaan cookies secara default dalam pengembangan web dan risiko potensial yang harus diwaspadai
Penggunaan cookies dalam pengembangan web memiliki risiko potensial yang harus diwaspadai. Meskipun cookies adalah bagian integral dari banyak aplikasi web, ada beberapa risiko keamanan yang terkait dengan mereka. Beberapa risiko tersebut termasuk pencurian cookie, serangan Cross-Site Scripting (XSS), session fixation, session hijacking, dan potensi kebocoran data sensitif jika tidak dielola dengan baik. Untuk mengurangi risiko ini, penting untuk menerapkan praktik keamanan yang baik, seperti penggunaan HTTPS untuk melindungi komunikasi antara server dan perangkat pengguna, validasi dan sanitasi data yang benar sebelum menyimpannya dalam cookies, serta pemantauan dan pembaruan berkala terhadap kebijakan keamanan yang sesuai. Dengan tindakan pencegahan yang tepat, penggunaan cookies dapat menjadi aman dalam pengembangan web.

## 5. Implementasi Checklist Step by Step
**a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar**

Registrasi
Pada step ini, pertama saya melakukan import redirect, UserCreationForm, dan messages pada `views.py` kemudian saya membuat sebuah fungsi `register` dengan parameter `request`. Isi fungsi ini akan membuat UserCreationForm dengan memasukkan QueryDict dari input user, memvalidasi input, menyimpan data, dan akan secara otomatis redirect ke halaman show_main. Setelah membuat algoritma logikanya, saya membuat kerangka tampilan HTML page register dengan membuat `register.html` untuk menampilkan halaman register di web. Langkah terakhir adalah melakukan *routing* URL pada `urls.py` aplikasi `main` dengan mengimpor fungsi yang dibuat dan menambahkan path url register ke dalam `urlpatterns` untuk mengakses fungsi tersebut.

Login
Pada step ini, pertama saya melakukan import authenticate dan login pada `views.py` untuk melakukan autentikasi dan login jika berhasil, kemudian saya membuat sebuah fungsi `login_user` dengan parameter `request`. Isi fungsi ini akan melakukan autentikasi pengguna berdasarkan username dan password, kemudian akan secara otomatis redirect ke halaman show_main jika berhasil. Setelah membuat algoritma logikanya, saya membuat kerangka tampilan HTML page login dengan membuat `login.html` untuk menampilkan halaman login di web. Selanjutnya saya melakukan *routing* URL pada `urls.py` aplikasi `main` dengan mengimpor fungsi yang dibuat dan menambahkan path url login_user ke dalam `urlpatterns` untuk mengakses fungsi tersebut. Langkah terakhir adalah saya merestriksi akses halaman `main` dengan import login_required dan kode `@login_required(login_url='/login')` agar halaman main hanya dapat diakses setelah pengguna terautentikasi login.

Logout
Pada step ini, pertama saya melakukan import logout pada `views.py`, kemudian saya membuat sebuah fungsi `logout_user` dengan parameter `request`. Isi fungsi ini akan melakukan penghapusan sesi pengguna dan secara otomatis redirect ke halaman login. Setelah membuat algoritma logikanya, saya menambahkan kerangka HTML button logout pada `main.html` untuk menampilkan button logout. Langkah terakhir adalah melakukan *routing* URL pada `urls.py` aplikasi `main` dengan mengimpor fungsi yang dibuat dan menambahkan path url logout_user ke dalam `urlpatterns` untuk mengakses fungsi tersebut.

**b. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal**

Pada step ini, saya coba melakukan registrasi 1 akun terlebih dahulu (raisa_01) sehingga 2 data dummy yang sudah dibuat pada tugas sebelumnya akan menjadi properti Item milik user raisa_01 setelah integrasi user-Item. Setelah itu saya menambahkan satu dummy data lagi pada akun tersebut. Setelah melakukan step integrasi model Item dengan User, saya membuat satu akun lagi (raisa_02) yang isinya akan kosong karena belum ada data Item yang terdaftar terhubung dengan user tersebut. Maka, saya akan menambahkan 3 dummy data baru pada akun tersebut.

<img width="442" alt="user raisa_01" src="https://github.com/raisahzr/latte-night/assets/119391721/a01fddf4-fbe6-4fe9-9e14-f8fa2257c91e">

<img width="442" alt="user raisa_02" src="https://github.com/raisahzr/latte-night/assets/119391721/32b2cb1d-af2d-47cd-9c3c-b57e6b5e74f0">

**c. Menghubungkan `model` Item dengan `User`**

Pada step ini, saya melakukan migrasi model dengan tambahan import user dan menambahkan `user = models.ForeignKey(User,on_delete=models.CASCADE)` untuk menghubungkan satu user dengan satu item menggunakan ForeignKey. Kemudian saya memodifikasi fungsi `create_product` dengan menambahkan parameter `commit=False` yang berfungsi untuk memodifikasi objek terlebih dahulu sebelum disimpan ke database. Terakhir saya menambahkan `Item.objects.filter(user=request.user)` pada show_main untuk hanya menampilkan objek Item yang terasosiasi dengan user.

**d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi**

Untuk menampilkan detail informasis pengguna yang sedang logged in, saya mengubah context `name` pada show_main di `views.py` dengan `request.user.username` untuk menyesuaikan nama dengan user yang sedang login. Kemudian untuk menerapkan cookies, pertama pada `views.py` saya melakukan import HttpResponseRedirect, reverse, dan datetime. Selanjutnya saya memodifikasi fungsi login_user dengan menambahkan fungsi untuk cookie bernama `last_login` dengan mengganti kode dalam blok `if user is not None` menjadi:
```
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
response.set_cookie(...) berfungsi untuk membuat _cookie last_login dan menambahkannya ke dalam response. 

Untuk menghapus cookie last_login, saya menambahkan kode pada fungsi logout_user dengan:
```
response = HttpResponseRedirect(reverse('main:login'))
response.delete_cookie('last_login')
```

Terakhir, untuk menampilkan informasi last login pada halaman main, saya menambahkan `'last_login': request.COOKIES['last_login'],` pada context dan menambahkan variabel {{ last_login }} pada `main.html` untuk ditampilkan.

</details>

<details>
<summary>Tugas 5</summary>
<br>

## 1. Element Selector
| Selector | Manfaat |	Waktu Penggunaan |
| --- | --- | --- |
Universal `(*)` | Memilih semua elemen dalam dokumen HTML | Cocok digunakan ketika ingin menerapkan gaya yang sama pada semua elemen dengan jenis tag yang sama |
Elemen `(Tag)` | Memilih semua elemen HTML dengan jenis tag tertentu | Cocok digunakan ketika ingin menerapkan gaya yang sama pada semua elemen dengan jenis tag yang sama |
ID `(#id)` | Memilih elemen berdasarkan atribut id yang unik | Cocok digunakan ketika ingin mengatur gaya untuk elemen tunggal yang memiliki atribut id unik |
Class `(.class)` | Memilih elemen berdasarkan atribut class | Cocok digunakan jika ingin menerapkan gaya yang sama pada beberapa elemen dengan atribut class yang sama |
Atribut `([attribute])` | Memilih elemen berdasarkan atribut HTML | Cocok digunakan jika ingin memilih elemen berdasarkan atribut khusus |
Kombinasi `element, element` | Memilih elemen berdasarkan hubungan hierarki atau kombinasi elemen | Cocok untuk memilih elemen yang terkait secara spesifik dalam struktur dokumen |
Pseudo-class `(:pseudo-class)` | Memilih elemen dalam keadaan tertentu atau berdasarkan interaksi pengguna | Cocok digunakan jika ingin mengubah gaya elemen saat interaksi pengguna, seperti mengubah warna tautan saat diklik (:hover) atau mengatur ulang inputan saat difokuskan (:focus) |
Pseudo-element `(::pseudo-element)` | Memilih bagian dari elemen yang mungkin tidak ada dalam markup HTML | Cocok digunakan jika ingin mengatur gaya bagian-bagian tertentu dari elemen, seperti menambahkan konten sebelum atau sesudah elemen (::before dan ::after) atau memformat teks yang dipilih (::selection) |


## 2. Tag HTML 5
Berikut beberapa tag HTML5 yang saya ketahui dan banyak terapkan pada tugas ini:
| Tag | Deskripsi |
| --- | --- |
| `<a>` | Spesifikasi anchor atau tautan |
| `<body>` | Spesifikasi badan HTML |
| `<br>` | Satu baris break |
| `<button>` | Spesifikasi button |
| `<col>` | Spesifikasi kolom tabel |
| `<div>` | Spesifikasi section |
| `<b>` | Spesifikasi bold text |
| `<font>` | Spesifikasi font |
| `<head>` | Spesifikasi kepala/informasi dokumen |
| `<h1> to <h6>` | Spesifikasi header 1 - header 6 |
| `<html>` | Spesifikasi dokumen HTML |
| `<img>` | Spesifikasi gambar/foto |
| `<keygen>` | Generate key information dalam form |
| `<p>` | Spesifikasi paragraf |
| `<section>` | Representasi section |
| `<style>` | Spesifikasi gaya yang digunakan |
| `<table>` | Spesifikasi tabel |
| `<th>` | Spesifikasi header tabel |
| `<tr>` | Spesifikasi baris tabel |
| `<td>` | Spesifikasi datacell tabel |

## 3. Margin dan padding
![B1QiTx9ya](https://github.com/raisahzr/latte-night/assets/119391721/8de91934-5db5-413f-b4b7-d03489a12dca)
| Box Model | Fungsi | Pengaruh | Penggunaan |
| --- | --- | --- | --- |
| Margin | Mengosongkan area di sekitar border (transparan) | Memengaruhi jarak antara elemen dengan elemen-elemen di sekitarnya | Digunakan untuk mengontrol jarak antara elemen dengan elemen-elemen lain di sekitarnya |
| Padding | Mengosongkan area di sekitar konten (transparan) | Memengaruhi jarak antara batas elemen dan kontennya sendiri | Digunakan untuk mengontrol jarak antara batas elemen dan kontennya |

Kesimpulannya, margin mempengaruhi jarak antara elemen dengan elemen di sekitarnya, sedangkan padding mempengaruhi jarak antara batas elemen dan kontennya sendiri. Keduanya berkontribusi pada tata letak dan tampilan halaman web secara keseluruhan.

## 4. Bootstrap dan Tailwind
| Bootstrap | Tailwind |
| --- | --- |
| Menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung | Membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya |
| Memiliki file CSS yang lebih besar karena termasuk banyak komponen yang telah didefinisikan | Memiliki file CSS yang lebih kecil sedikit karena hanya memuat kelas-kelas utilitas yang ada |
| Sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan | Memiliki memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek |

Kesimpulannya, Bootstap lebih cocok digunakan untuk proyek dengan jadwal cepat dan memerlukan antarmuka pengguna yang bagus tanpa banyak kustomisasi, memiliki desain konsisten dan cepat, serta tidak membutuhkan pemahaman kompleks. Sedangkan, Tailwind lebih cocok digunakan untuk proyek yang memerlukan desain yang sangat kustom dan unik,  ingin menghindari kelas-kelas yang tidak digunakan dan memiliki kontrol yang lebih besar terhadap tampilan akhir halaman, dan sudah memiliki pemahaman tingkat lanjut untuk kustomisasi yang fleksibel.

## 5. Implementasi checklist step-by-step
**a. Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin**

Pertama saya menginisiasi penggunaan Bootstrap pada `base.html` sebagai default template CSS proyek. Untuk ketiga file ini, saya menerapkan styling CSS dengan presedensi yang lebih tinggi (overwrite) menggunakan Internal CSS dan In-line CSS. Untuk penerapannya saya memanfaatkan selektor untuk melakukan kustomisasi yang umumnya terkait warna, font, box model, margin, dan alignment. Misal pada `login.html` saya memanfaatkan selektor Class .login, lalu selektor elemen seperti h1. Sisanya, in-line CSS hnaya saya gunakan jika dibutuhkan pada elemen spesifik tertentu, misal pada h1 yang berisi judul saya ingin memiliki font yang berbeda dari h1 lain. Kemudian untuk memastikan tema yang dimiliki konsisten, Internal CSS pada `regiser.html` dan `create_product` kurang lebih isinya sama.


**b. Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card**

Sebelumnya, saya menerapkan konsep Internal CSS dan in-line CSS yang mirip pada register, login, tambah inventori. Kemudian, saya memanfaatkan navbar dari Bootstrap untuk membuat navigation bar pada `main.html`
```
<nav class="navbar navbar-expand-lg"  style="background-color: #ccc0a7;">
        <div class="container-fluid">
            <a class="navbar-brand" href="#" style="font-family: Luminari, serif;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/1200px-Default_pfp.svg.png" height="35px" width="35px" alt="Logo" style="margin-right: 10px;"> 
                ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ Latte-Night 
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup" style="font-family: Luminari, serif;">
                <div class="navbar-nav">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                    <a class="nav-link" href="{% url 'main:create_product' %}">Add New Product</a>
                    <a class="nav-link" href="{% url 'main:logout' %}">Logout</a>
                </div>
            </div>
        </div>
    </nav>
```

Untuk membentuk dafatar inventori menjadi Cards, saya merancang agar pada tampilan cards maksimal 4 buah dalam 1 baris, dan akan berada pada baris berikutnya jika ada penambahan item lagi. Saya juga memanfaatkan style Bootstrap pada button dalam cards seperti primary button (add/substract) dan danger button (delete).
```
<div class="container">
        <div class="row">
            {% for item in items %}
                <div class="col-md-3 mb-4">
                    <div class="card {% if forloop.last %}custom-background{% endif %}">
                        <div class="card-body">
                            <h5 class="card-title">{{item.name}}</h5>
                            <p class="card-text">Amount: {{item.amount}}</p>
                            <p class="card-text">Description: {{item.description}}</p>
                            <p class="card-text">Date Added: {{item.date_added}}</p>
                            <p class="card-text">Price: {{item.price}}</p>
                            <p class="card-text">Category: {{item.category}}</p>
                            <div class="text-center">
                                <form method="post" action="{% url 'main:add_amount' item.id %}">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-primary">Add</button>
                                </form>
                                <form method="post" action="{% url 'main:substract_amount' item.id %}">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-primary">Substract</button>
                                </form>
                                <form method="post" action="{% url 'main:delete_item' item.id %}">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-danger">Delete</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                {% if forloop.counter|divisibleby:4 and not forloop.last %}
                    </div><div class="row">
                {% endif %}
            {% endfor %}
        </div>
    </div>
```
Notes: `{% if forloop.last %}custom-background{% endif %}` digunakan sebagai conditional agar item terakhir yang terdapat pada inventori memiliki background dan font berbeda (diterapkan melalui selector)
</details>

<details>
<summary>Tugas 6</summary>
<br>

## 1. Synchronous Programming vs Asynchronous Programming
| Synchronous | Asynchronous|
| --- | --- |
| Eksekusi kode berlangsung secara sekuensial, berarti operasi dilakukan secara berurutan atau sejalan. Dalam programming synchronous, kode dieksekusi baris per baris, dan setiap operasi harus menunggu operasi sebelumnya selesai. Ini sederhana dan mudah dipahami, tapi bisa menjadi bottleneck dalam situasi di mana ada penundaan, seperti saat menunggu respons dari server. Oleh karena itu, synchronous lebih cocok untuk pendekatan programming yang memiliki urutan eksekusi terstruktur | Operasi-operasi yang mungkin membutuhkan waktu, seperti pemanggilan API atau operasi file, dapat dilakukan tanpa harus menunggu operasi tersebut selesai. Kode dapat melanjutkan eksekusi sementara operasi tersebut berlangsung. Asynchronous programming sangat berguna dalam situasi di mana aplikasi perlu merespons terhadap input pengguna atau berkomunikasi dengan server tanpa memblokir eksekusi program |


## 2. Event-Driven Programming pada AJAX
Event-Driven Programming adalah paradigma di mana alur eksekusi program ditentukan oleh kejadian (events) yang terjadi. Dalam JavaScript dan AJAX, program menanggapi kejadian-kejadian tertentu tanpa harus menunggu operasi selesai.

Contoh penerapannya pada tugas ini adalah klik pada tombol add product by ajax akan men-trigger sebuah event yang memunculkan modal form. Selanjutnya saat form di-submit, fungsi dari AJAX adalah mengirim data form tersebut ke server untuk update tampilan web  tanpa harus menunggu pengguna melakukan refresh.

## 3. Penerapan Asynchronous Programming pada AJAX
AJAX (Asynchronous JavaScript and XML) dirancang untuk bekerja secara asynchronous. Dengan menggunakan AJAX, permintaan ke server dapat dikirim tanpa harus menunda eksekusi program, dan respon dari server ditangani melalui callback functions. Dengan demikian, aplikasi dapat melakukan proses data tanpa harus menunggu operasi lain selesai. 

## 4. Fetch API vs jQuery
Berikut perbandingan antara Fetch API dan jQuery:
| Fetch API | jQuery|
| --- | --- |
| Fetch API adalah bagian dari standar JavaScript modern yang relatif lebih ringan karena fokus pada pengambilan sumber daya dari jaringan dan pengelolaan respons HTTP |  jQuery yang lebih kuat dan berfitur, bisa dianggap berat jika hanya membutuhkan fungsionalitas AJAX karena  memiliki fitur-fitur lain yang mungkin tidak diperlukan dalam proyek kecil atau aplikasi yang membutuhkan performa maksimal |
| Fetch API dirancang untuk menjadi modular dan mudah digunakan dengan konsep Promise sehingga lebih bebas dalam membangun arsitektur proyek |  jQuery punya pustaka yang lengkap, sehingga jika hanya digunakan untuk AJAX, jQuery masih membawa sejumlah besar fungsionalitas lain yang mungkin tidak diperlukan |
| Menggunakan konsep Promise, yang membuat penanganan asynchronous lebih mudah dibaca dan ditulis | Menggunakan konsep callback, yang bisa membuat beberapa lapisan callback dan membuat kode tampak lebih bersarang |
| Lebih modern, oleh karena itu bisa tidak didukung oleh browser yang lebih tua tanpa menggunakan polifil (polyfill) | Dikenal karena kompatibilitas lintas-browsernya yang baik, termasuk dengan browser lama |
| Memberikan lebih banyak kontrol dan kustomisasi terhadap request dan respons | Menyederhanakan banyak detail, yang bisa menjadi kelebihan atau kekurangan tergantung pada kebutuhan proyek |


## 5. Implementasi Step by Step
**a. Ubah kode cards data item agar mendukung AJAX GET dan lakukan pengambilan task menggunakan AJAX GET**
Menghapus representasi cards sebelumnya dengan `<div class="row" id="item-cards"></div>` lalu membuat fungsi 
```
def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
```
Kemudian import dan routing fungsi tersebut pada `urls.py`.
Terakhir, tambahkan fungsi `getProducts()` pada blok <script>:
```
async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json());
        }
```

**b. Buat tombol untuk membuka modal form untuk menambahkan item**

Pada `main.html` tambahkan button ` <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>` dan kode untuk membuat modal:
```
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount:</label>
                            <input type="number" class="form-control" id="amount" name="amount"></input>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price:</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                        <div class="mb-3">
                            <label for="category" class="col-form-label">Category:</label>
                            <input type="text" class="form-control" id="category" name="category"></input>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
    </div>
```

**c. Buat fungsi view untuk menambahkan item baru**

Import `from django.views.decorators.csrf` lalu tambahkan fungsi create_ajax dan menyesuaikan isinya dengan models yang saya punya
```
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category = request.POST.get("category")
        user = request.user

        new_product = Item(name=name, amount=amount, price=price, description=description, category=category, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

**d. Buat path `/create-ajax/` yang mengarah ke fungsi view tadi**

Import fungsi tersebut kemudian menambahkan path fungsi di views ke `urls.py`:
`path('create-ajax/', create_ajax, name='create_ajax'),`

**e. Hubungkan form yang telah dibuat di dalam modal ke path `/create-ajax/`**

Tambahkan fungsi `addProduct()` pada `main.html` dalam blok `<script>`:
```
function addProduct() {
            fetch("{% url 'main:create_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts);
            window.location.reload()

            document.getElementById("form").reset();
            return false;
        }

        document.getElementById("button_add").onclick = addProduct;
    </script>
```

**f.Refresh halaman utama secara async untuk menampilkan daftar item terbaru tanpa reload**

Tambahkan fungsi `refreshProducts()` pada blok `<script>`:
```
async function refreshProducts() {
            const cardContainer = document.getElementById("product_cards");
            cardContainer.innerHTML = "";
            const products = await getProducts();

            products.forEach((item) => {
                const card = document.createElement("div");
                const addAmount = `{% url 'main:add_amount' 999999%}`.replace('999999', item.id);
                const subsAmount = `{% url 'main:substract_amount' 999999%}`.replace('999999', item.id);
                const delItem = `{% url 'main:delete_item' 999999%}`.replace('999999', item.id);
                card.className = "col-md-3 mb-4";
                card.classList.add(className);

                const cardContent = `
                    <div class="card ${item.is_last ? 'custom-background' : ''}">
                        <div class="card-body">
                            <h5 class="card-title">${item.fields.name}</h5>
                            <p class="card-text">Amount: ${item.fields.amount}</p>
                            <p class="card-text">Description: ${item.fields.description}</p>
                            <p class="card-text">Date Added: ${item.fields.date_added}</p>
                            <p class="card-text">Price: ${item.fields.price}</p>
                            <p class="card-text">Category: ${item.fields.category}</p>
                            <div class="text-center">
                                <a href="${addAmount}" class="btn btn-primary" Add</a>
                                <a href="${subsAmount}" class="btn btn-primary" Substract</a>
                                <a href="${delItem}" class="btn btn-danger" Delete</a>
                            </div>
                        </div>
                    </div>
                `;
                card.innerHTML = cardContent;
            });
        }

        refreshProducts();
```

**g. collectstatic**

Menambahkan STATIC_URL dan STATIC_ROOT ke `settings.py` lalu menjalankan command `python manage.py collect static`.
</details>
