from django.contrib import admin

# Register your models here.
from. models import Produk, Merkp, Hotsale, Termurah

class kolomProduk(admin.ModelAdmin):
    list_display = ['kode_Produk','merk_Produk','tipe_Produk','stok_Produk','harga_Produk','link_Gambar_Produk']
    search_fields= ['kode_Produk','tipe_Produk']
    list_filter= ['merk_Produk',]
    list_per_page= 5

class kolomHotsale(admin.ModelAdmin):
    list_display = ['kode_Produk_Hotsale','merk_Produk_Hotsale','tipe_Produk_Hotsale','stok_Produk_Hotsale','harga_Produk_Hotsale','link_Gambar_Produk_Hotsale']
    search_fields= ['kode_Produk_Hotsale','tipe_Produk_Hotsale']
    list_filter= ['merk_Produk_Hotsale',]
    list_per_page= 5

class kolomTermurah(admin.ModelAdmin):
    list_display = ['kode_Produk_Termurah','merk_Produk_Termurah','tipe_Produk_Termurah','stok_Produk_Termurah','harga_Produk_Termurah','link_Gambar_Produk_Termurah']
    search_fields= ['kode_Produk_Termurah','tipe_Produk_Termurah']
    list_filter= ['merk_Produk_Termurah',]
    list_per_page= 5

admin.site.register(Produk, kolomProduk)
admin.site.register(Hotsale, kolomHotsale)
admin.site.register(Termurah, kolomTermurah)
admin.site.register(Merkp)