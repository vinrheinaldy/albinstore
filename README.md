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

![alt text](images/bagan1.png)

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
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django </b> </summary>
   
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   
Dalam proses mengimplementasi sebuah platform data delivery sangatlah penting dikarenakan data delivery ini adalah hal penting dari komunikasi antar komponen dalam sistem dan interaksi dengan pengguna. Selain itu data delivery digunakan juga untuk memastikan aliran data yang konsisten, optimasi performa sistem, menjaga keamanan pengguna.
   
### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

| Format       | XML                                                                 | JSON                                                                                     |
|--------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Perbandingan |Menggunakan tag yang mirip dengan HTML untuk menyusun data dalam bentuk elemen-elemen yang berpasangan. XML menggunakan tag yang memisahkan nama data dan nilai data. |  Menggunakan format yang lebih sederhana dan ringan dengan struktur yang terdiri dari pasangan kunci (key) dan nilai (value). |
| Sintaks      | `<tag>isi</tag>`                                                  | `{nama: '<input nama>'}` 

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method ini adalah method otomatis dan digunakan untuk memvalidasi data yang dikirimkan melalui form.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Penggunaan csrf_token merupakan langkah keamanan penting dalam menggunakan Django, dikarenakan jika tidak menggunaan ini, aplikasi kita dapat diberi permintaan palsu dari pihak yang tidak diinginkan yang dapat menggunakan sesi pengguna yang aktif untuk melakukan tindakan kriminal.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Implementasi skeleton

1. Membuat folder bernama `templates` di folder utama(`root directory`).
2. Dalam folder `templates` buat `base.html` yang berisi berikut:
   ```
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       {% block meta %} {% endblock meta %}
     </head>

     <body>
       {% block content %} {% endblock content %}
     </body>
   </html>
   ```
3. Pada `settings.py` dalam folder `albinstore` tambahkan `DIRS` dalam `TEMPLATES`
   ```
   'DIRS': [BASE_DIR / 'templates'],
   ```


### Implementasi UUID

1. Dalam folder `main` bukalah `models.py` ubahlah menjadi
   ```
   import uuid
   
   class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
   ```
2. Migrasi dengan menjalankan command
   ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

### Membuat form penambahan objek

1. Dalam folder `main` buatlah folder `forms.py` yang diisi
   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductEntryForm(ModelForm):
       class Meta:
           model = Product
           fields = ["name", "price", "description"]
   ```
2. Dalam folder `main/template` buatlah `create_product_entry.html` yang berisi
   ```
   {% extends 'base.html' %} 
   {% block content %}
   <h1>Add New Product Entry</h1>

   <form method="POST">
     {% csrf_token %}
     <table>
       {{ form.as_table }}
       <tr>
         <td></td>
         <td>
           <input type="submit" value="Add Product Entry" />
         </td>
       </tr>
     </table>
   </form>

   {% endblock %}
   ```
3. Dalam `views.py` dalam folder yang sama saya menambahkan function baru yaitu
   ```
   def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
   ```
4. Lalu dalam file yang sama dalam function `show_main` saya menambahkan edit
   ```
   def show_main(request):
      product_entries = Product.objects.all()

      ...

      'product_entries': product_entries
   ```

5. Lalu saya mengubah `main.html` dalam direktori `template`
   ```
   {% extends 'base.html' %}
   {% block content %}
   <h1>albinstore</h1>

   <h5>NPM: </h5>
   <p>{{ npm }}<p>

   <h5>Name:</h5>
   <p>{{ name }}</p>

   <h5>Class:</h5>
   <p>{{ class }}</p>

   {% if not product_entries %}
   <p>Belum ada product pada toko ini.</p>
   {% else %}
   <table>
     <tr>
       <th>Name</th>
       <th>Price</th>
       <th>Description</th>
     </tr>

     {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
     {% endcomment %} 
     {% for product_entry in product_entries %}
     <tr>
       <td>{{product_entry.name}}</td>
       <td>{{product_entry.price}}</td>
       <td>{{product_entry.description}}</td>
     </tr>
     {% endfor %}
   </table>
   {% endif %}

   <br />

   <a href="{% url 'main:create_product_entry' %}">
     <button>Add New Product Entry</button>
   </a>

   {% endblock content %}
   ```

### Return data dalam bentuk XML & JSON

1. Dalam folder `main`  mengedit `views.py` dengan manambahkan
   ```
   from django.http import HttpResponse
   from django.core import serializers
   ```
2. Lalu menambahkan function baru untuk bisa mengambil XML & JSON
   ```
   def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

   def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
   ```
3. Lalu cara mengembalikan data XML & JSON dengan ID dilakukan dengan cara menambahkan function seperti
   ```
   def show_xml_by_id(request, id):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

   def show_json_by_id(request, id):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
   ```

4. Dalam folder yang sama bukalah `urls.py` lalu masukkan
   ```
   from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
   ```
5. Dalam `urlpatterns` tambahkan
   ```
   urlpatterns = [
    ...
    path('create_product_entry/', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ...
   ]
   ```

### Lakukan push ke github
```
git add .
git commit -m"<Commit message>"
git push origin main
git push pws master
```

### Screenshots

1. XML
   ![alt text](images/xml.png)

2. XML by id
   ![alt_text](images/xml-id.png)

3. JSON
   ![alt_text](images/json.png)

4. JSON by id
   ![alt_text](images/json_id.png)
   
</details>
   
<details>
<summary> <b> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </b> </summary>

### Apa perbedaan antara HttpResponseRedirect() dan redirect()
   

| Format       | HttpsResponseRedirect()                                                                 | redirect()                                                           |
|--------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Perbandingan |Membuat respons pengalihan manual ke URL tertentu. |  Shortcut yang lebih pintar untuk pengalihan ke URL, view, atau model. |
| Sintaks      | `HttpResponseRedirect('/some/url/')`                                                  | `redirect('/some/url/')`  atau `redirect('view_name')`

   Secara ringkas HttpResponseRedirect() digunakan untuk pengalihan manual yang hanya menerima URL, sedangkan redirect() lebih fleksibel karena dapat menerima URL, view name, atau model instance dan lebih sering digunakan di Django karena kemudahannya.


### Jelaskan cara kerja penghubungan model Product dengan User!

Menghubungkan model Product dan User dapat dilakukan dengan ForeignKey(Relasi one-to-many). Hubungan one-to-many berarti satu pengguna dapat memiliki banyak produk, tetapi setiap produk hanya dimiliki oleh satu pengguna. Field ForeignKey menyimpan referensi ke User, dan jika User dihapus, maka Product yang terasosiasi dengan User tersebut juga akan ikut terhapus.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

| Format       | Authentication                                                                 | Authorization                                                          |
|--------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Perbandingan | Proses memverifikasi identitas pengguna (apakah mereka siapa yang mereka klaim). |  Proses menentukan apa yang boleh dilakukan pengguna (hak akses). |
| Implementasi      | `authenticate`, `login`, `logout`                                           | `@login_required`, `@permission_required` |


### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menggunakan session yang disimpan di server dan dihubungkan dengan pengguna melalui cookies. Django kemudian menggunakan cookies tersebut untuk mengidentifikasi pengguna. 

Kegunaan lain dari cookies adalah untuk mengatur preferensi/setting pengguna seperti tema website(light/dark), font size, atau dengan fitur "remember me" yang membuat pengguna untuk tidak lagi harus mengisi username/email dan password lagi pada websitenya. Tidak semua cookies aman, cookies dapat disalahgunakan dalam serangan seperti session hijacking, XSS, dan CSRF.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

## Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

1. Membuat fungsi registrasi yang saya lakukan adalah pada folder `main` saya membuka `views.py` lalu menambahkan potongan kode seperti berikut
   ```
   def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
   ```
2. Membuat tampilan web untuk register dalam folder `templates` dalam direktori yang sama saya membuat file baru bernama `register.html` yang berisi
   ```
   {% extends 'base.html' %}

   {% block meta %}
   <title>Register</title>
   {% endblock meta %}

   {% block content %}

   <div class="login">
     <h1>Register</h1>

     <form method="POST">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td><input type="submit" name="submit" value="Daftar" /></td>
         </tr>
       </table>
     </form>

     {% if messages %}
     <ul>
       {% for message in messages %}
       <li>{{ message }}</li>
       {% endfor %}
     </ul>
     {% endif %}
   </div>

   {% endblock content %}
   ```

3. Untuk membuat login saya tambahkan code berikut pada `views.py`
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

    
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response 

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

4. Untuk tampilan loginnya pada `templates` saya membuat file html baru bernama `login.html` yang berisi
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

5. Untuk logout pada `views.py` saya menambahkan potongan kode sebagai berikut
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

6. Untuk menampilkan tombol logout, dalam folder `templates` pada `main.html` saya tambahkan code berikut pada bagian bawah code html(namun masih diatas `{% endblock content %}`
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

7. Routing semua fitur, saya mengubah `urls.py` menjadi
```
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product_entry/', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```
8. Pada `models.py` saya menambahkan field `user` agar setiap user yang unik bisa melihat produk produk yang ditambahkan
```
from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()

```
9. Untuk memverifikasi apakah user sudah login pada `views.py` saya menambahkan potongan kode berikut diatas `show_main`
```
@login_required(login_url='/login')
```
10. Untuk cookies saya tambahkan dengan `login_user` pada `views.py`
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

    
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
```

</details>

<details>

<summary><b> Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS </b> </summary>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

1. Inline styles (diterapkan langsung di elemen) – prioritas tertinggi.

    Contoh: `<div style="color: red;"></div>`

2. ID Selector (`#id`) – prioritas tinggi.

    Contoh: `#header { color: blue; }`

3. Class Selector, Attribute Selector, dan Pseudo-Class Selector (seperti `.class`, `[type="text"]`, `:hover`) – prioritas sedang.

    Contoh: `.menu { color: green; }`

4. Element Selector dan Pseudo-Element Selector (seperti `div`, `h1`, `::before`) – prioritas rendah.

    Contoh: `div { color: pink; }`

5. Universal Selector (`*`) dan Combinator Selector (`>`,`+`, `~`) – prioritas terendah.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design adalah konsep penting dalam pengembangan aplikasi web karena memungkinkan tampilan dan fungsionalitas situs atau aplikasi untuk beradaptasi dengan berbagai ukuran layar dan perangkat, seperti smartphone, tablet, laptop, dan desktop. Dengan semakin meningkatnya penggunaan perangkat mobile, responsive design memastikan bahwa pengguna mendapatkan pengalaman yang optimal, terlepas dari perangkat yang mereka gunakan.

Contoh aplikasi yang sudah: 
- Twitter(X)
- Youtube

Contoh aplikasi yang belom:
- Aplikasi/Webpage lama yang belom di update(?)
- Web pemerintah (kwoakwowkwaa)

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin adalah ruang di luar border elemen. Margin digunakan untuk memberikan jarak antar elemen. Ini tidak mempengaruhi ukuran elemen itu sendiri. Cara untuk mengimplementasinya bisa dengan:
```
.element{
   margin: 20px;
}
```
Border adalah garis yang mengelilingi elemen dan berada di antara margin dan padding. Border bisa diberi warna, gaya, dan ketebalan. Cara untuk mengimplementasinya bisa dengan: 
```
.element {
    border: 2px solid black; 
}
```
Padding adalah ruang di dalam border elemen, antara konten elemen dan border. Padding mempengaruhi ruang di dalam elemen tanpa mempengaruhi jarak antara elemen dan elemen lainnya. Cara untuk implementasinya adalah dengan:
```
.element {
    padding: 20px; 
}
```

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

| Format       | Flex Box                                                                 | Grid Layout                                                          |
|--------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Konsep | Flexbox adalah modul tata letak satu dimensi yang digunakan untuk mengatur elemen dalam satu arah: baris (row) atau kolom (column). |  CSS Grid Layout adalah modul tata letak dua dimensi yang memungkinkan pengembang web untuk membuat desain grid yang kompleks dan fleksibel. |
| Kegunaan      | Flexbox sangat berguna waktu kamu pengen mengatur elemen secara dinamis, misalnya mengatur elemen agar menyesuaikan ukuran mereka secara otomatis untuk mengisi ruang yang tersedia, atau agar berperilaku dengan fleksibilitas yang lebih tinggi di berbagai ukuran layar.                                         | Dengan Grid Layout, kamu bisa mengatur elemen dalam baris dan kolom secara bersamaan, sehingga sangat berguna untuk membuat tata letak yang lebih bagus dibandingkan sama Flexbox. |

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Implementasikan fungsi untuk menghapus dan mengedit product.

1. Pertama yang saya lakukan adalah buka `main/views.py` lalu menambahkan function baru bernama `edit_product_entry` yang berisi:
```
def edit_product_entry(request, id):
    product_entry = Product.objects.get(pk=id)
    form = ProductEntryForm(request.POST or None, instance=product_entry)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product_entry.html", context)
```
2. Lalu saya membuat file HTML baru bernama `edit_product_entry_html.` pada `main/templates` yang berisi:
```
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-transparent">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>
  
    <div class="bg-white rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6" enctype="multipart/form-data">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                  Edit Product Entry
              </button>
          </div>
      </form>
  </div>
  </div>
</div>
{% endblock %}
```
3. Lalu pada `urls.py` saya mengimpor function tersebut
   ```
   from main.views import edit_product_entry
   ```
4. Lalu tambahkan pathnya kepada url patterns
   ```
   path('edit_product/<uuid:id>/', edit_product_entry, name='edit_product'),
   ```
5. Untuk tombol delete saya menambahkan function `hapus_product_entry` pada `views.py` yang berisi:
   ```
   def hapus_product_entry(request, id):
    product_entry = Product.objects.get(pk=id)
    product_entry.delete()
    return redirect('main:show_main')
   ```
6. Sama seperti sebelumnya pada `urls.py` kita mengimport `hapus_product_entry` lalu kita tambahkan pathnya
   ```
   path('delete_product/<uuid:id>/', hapus_product_entry, name='delete_product'),
   ```
7. Untuk mengaplikasikan kedua tersebut kedalam aplikasi bukalah `product_card.html` lalu tambahkan kode berikut:
```
<div class="absolute top-0 -right-4 flex space-x-1">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
```
#### Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
- Melakukan penambahan background
- Mengganti warna/design font
- Mengganti warna tombol

#### Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
Saya memberikan foto orang sedih dan memberi teks.

#### Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
Saya mengedit cardnya untuk menjadi unik, dan mengikuti tema website saya.

#### Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!

Untuk mengaplikasikan kedua tersebut kedalam aplikasi bukalah `product_card.html` lalu tambahkan kode berikut:
```
<div class="absolute top-0 -right-4 flex space-x-1">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
```

#### Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

1.Pada `templates` yang berada pada root directory buat file html baru bernama `navbar.html` lalu saya beri isi:
```
<nav class="bg-indigo-600 shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-2xl font-bold text-center text-white">Mental Health Tracker</h1>
        </div>
        <div class="hidden md:flex items-center">
          {% if user.is_authenticated %}
            <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Register
            </a>
          {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
      <div class="pt-2 pb-3 space-y-1 mx-auto">
        {% if user.is_authenticated %}
          <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
```
2. Namun saya edit beberapa agar lebih mirip dengan tema website saya.

</details>
