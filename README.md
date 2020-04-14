# Contoh Proyek GeoDjango #

Pada contoh proyek ini terdapat data spasial batas-batas provinsi di Indonesia dan bata-batas negara di dunia.


## Prasyarat
  - Python 3.6.x atau terbaru
  - Postgresql 9.6.x atau terbaru
  - PostGIS 2.5.4 atau terbaru
  - virtualenv (disarankan)

## Cara menggunakan
Buat virtual environment terlebih dahulu
```
virtualenv geodjango_env
```

Lalu aktifkan
```
source geodjango_env/bin/activate
```

Instal dependensi

```
$ pip install -r requirements.txt
```

Konfigurasi basisdata, buka berkas `settings.py`
```
DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': '<nama basis data>',
         'USER': '<nama pengguna basis data>',
         'password': '<sandi basis data>'
    },
}
```

Migrasi basis data dengan perintah
```
$ python manage.py migrate
```

Impor data spasial, jalankan management command ini
```
$ python manage.py import_data_spasial
```

Buat akun superuser
```
$ python manage.py createsuperuser
```

Jalankan service
```
python manage.py runserver
```

Lalu buka browser http://localhost:8000

## Peta Dunia
!["Indonesia"](https://raw.githubusercontent.com/irfanpule/contoh-geodjango/master/tangkapan_layer/indonesia.png)

## Peta Indonesia
!["Lampung"](https://raw.githubusercontent.com/irfanpule/contoh-geodjango/master/tangkapan_layer/lampung.png)