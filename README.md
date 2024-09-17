# albinstore

https://malvin-rheinaldy-albinstoree.pbp.cs.ui.ac.id/


<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>
   
## Bagaimana cara mengimplementasi Tugas

### 1. Cara membuat Repositori baru
1. Buatlah sebuah direktori baru di komputer anda
2. Inisialisasi repositori dan hubungkan dengan GitHub
   ```bash
   git init
   git remote add origin <URL>
   git add .
   git commit -m "Initial commit"
   git push origin master
   ```
### 2. Menjalankan virtual enviorment
1. Jalankan perintah berikut dalam cmd/Powershell dalam direktori sebelumnya
   ```bash
   python -m venv env
   ```
2. Aktifkan virtual enviorment yang tadinya dibuat
      - **Windows**:
         ``` bash
         env\Scripts\activate
         ```
    - **Mac/Linux**:
      ``` bash
      source env\Scripts\activate
      ```
### 3.Menyiapkan dependencies/requirements
1. Dalam direktori yang sama buatlah sebuah berkas `requirements.txt` dan tambahkan beberapa dependencies
    ```bash
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
2. Jalankan perintah berikut ini agar dapat menginstall dependenciesnya
   ```bash
   pip install -r requirements.txt
   ```
### 4. Membuat proyak Django baru
1. Buatlah sebuah proyek Django baru dengan nama `<name>`:
   ```bash
   django-admin startproject <name>
   ```
2. Membuat folder baru bernama main:
   ```bash
   django-admin startapp main
   ```
### 5. Membuat template 
1. Tambahkan kode berikut pada `views.py`
   ```bash
    from django.shortcuts import render

    def show_main(request):
      context = {
        'name_aplikasi': 'albinstore',
        'name': 'Alvin',
        'npm' : '2306275866',
        'class': 'PBP D'
    }
      return render(request, "main.html", context)
   ```
2. Pada `urls.py`, tambahkan `path('', include(`main.urls`))` pada `urlpatterns` agar URL pada `main` bisa diakses
3. Pada folder `main`, buatlah sebuah folder baru bernama `templates` dan di dalam folder ini buatlah sebuah file bernama `main.html` yang menampilkan data-data yang kita butuhkan

### 6. Mengubah berkas `models.py`
1. Di `models.py`, buat model produk dengan atribut berikut:
   - `name`
   - `price`
   - `description`
### 7. Melakukan migration
1. Pada terminal balik kepada folder/directory utama
2. Jalankan proses migration pada terminal
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 8. Deploy ke Pacil Web Service
1. Buat proyek baru dengan menekan tombol `Create New Project`. 
2. Setelah menekan tombol tersebut isilah nama project dengan sesuai keinginan.
3. Kemudian akan ada `Project Credential` simpanlah `Credentials` ini dalam folder luar.
4. Pada file `settings.py`, tambahkan `<URL Deployment Kamu>`, kedalam list `ALLOWED_HOSTS`.
   - **Notes**
     format URL PWS pada umumnya adalah
      ```bash
      <username-sso>-<nama proyek>.pbp.cs.ui.ac.id
      ```
5. Simpan semua perubahan dengan menjalankan perintah ini dalam terminal/command center
   ```bash
    git add .
    git commit -m "Deploy to PWS"
    git push origin master
   ```
6. Kemudian masukkan remote PWS dalam terminal
   ```bash
   git remote add pws <url>
   git branch -M master
   git push pws master
   ```

### 9. Selesai!
Aplikasi bisa diakses dengan URL yang kamu pilih!

# Bagan request client dan responsnya

![alt text](bagan1.png)

## Penjelasan

 1. User melakukan HTTP request yang ditangani oleh View: URL yang diminta oleh user diproses melalui urls.py, yang menentukan function View di views.py yang akan dijalankan.
 2. View me-request data dari Model: Function View akan mengambil data yang diperlukan dari model di models.py berdasarkan data field yang telah ditentukan.
 3. View me-request Template yang dipopulasikan data: Berdasarkan function View, berkas HTML tertentu akan dipilih dari Template, kemudian View mengirimkan HTML yang sudah diisi data tersebut sebagai HTTP response kepada user.

# Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git digunakan untuk melakukan version control dan agar dapat melihat apa saja yang ditambahkan pada proyek pada waktu tertentu yang terekam. Git juga dapat membantu kita dalam proses kolaborasi
dan juga dapat memungkinkan rollback ke versi-versi yang sebelumnya sudah di upload.

# Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dijadikan permulaan pembelajaran karena mudah dipelajari, terstruktur, memiliki fitur lengkap, aman, dan didukung komunitas besar serta dapat digunakan untuk aplikasi skala besar.

# Mengapa model pada Django disebut sebagai ORM?

Karena memungkinkan programmer untuk berinteraksi dengan basis data menggunakan Python, sehingga data yang disimpan di tabel-tabel basis data relasional dapat diakses dan dimanipulasi seolah-olah mereka adalah objek dalam kode, tanpa perlu menulis query SQL secara langsung.

</details>

   
<details>
<summary> <b> Tugas 3: ... </b> </summary>
### abcd
Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   
Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
