"""
URL configuration for soratechShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from gudang.views import *
from dashboard.views import *
from dashboard.views import hapus_brghot





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',tampil_barang_base),
    path('produk/',produk),
    path('tentang/', tentang),
    path('alamat/', alamat),
    path('krisar/', krisar),
    path('tambahbrg/', tambah_produk),
    path('tampilbrg/', tampil_barang, name='vbrg'),
    path('hapuspro/<int:id_produk>', hapus_brgpro, name='hapus_brgpro'),
    path('hapushot/<int:id_hotsale>', hapus_brghot, name='hapus_brghot'),
    path('hapuster/<int:id_termurah>', hapus_brgter, name='hapus_brgter'),
    path('ubahprod/<int:id_produk>', ubah_brgprod, name='ubah_brgprod'),
    path('ubahhot/<int:id_hotsale>', ubah_brghot, name='ubah_brghot'),
    path('ubahter/<int:id_termurah>', ubah_brgter, name='ubah_brgter'),
    path('tampilpro/',tampil),
    path('produkrdy/',tampil_barang_produk)
]

