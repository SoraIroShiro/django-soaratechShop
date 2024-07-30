from django.db import models

# Create your models here.
class Merkp (models.Model):
    merk=models.CharField(max_length=20)
    ket = models.CharField(max_length=100)

    def __str__(self):
        return self.merk

class Produk (models.Model):
    kode_Produk=models.CharField(max_length=5)
    merk_Produk=models.ForeignKey(Merkp, on_delete=models.CASCADE, null=False)
    tipe_Produk=models.CharField(max_length=20)
    stok_Produk=models.IntegerField()
    harga_Produk=models.BigIntegerField()
    link_Gambar_Produk=models.CharField(max_length=200 , blank=True)
    
merk_choices=(
    ('Xiaomi','Xiaomi'),
    ('Samsung','Samsung'),
    ('Vivo','Vivo'),
    ('Oppo','Oppo'),
    ('Realme','Realme'),
)

class Hotsale (models.Model):
    kode_Produk_Hotsale=models.CharField(max_length=5)
    merk_Produk_Hotsale=models.CharField(max_length=20, choices=merk_choices, default='Xiaomi')
    tipe_Produk_Hotsale=models.CharField(max_length=20)
    stok_Produk_Hotsale=models.IntegerField()
    harga_Produk_Hotsale=models.BigIntegerField()
    link_Gambar_Produk_Hotsale=models.CharField(max_length=200, blank=True)

class Termurah (models.Model):
    kode_Produk_Termurah=models.CharField(max_length=5)
    merk_Produk_Termurah=models.CharField(max_length=20, choices=merk_choices, default='Xiaomi')
    tipe_Produk_Termurah=models.CharField(max_length=20)
    stok_Produk_Termurah=models.IntegerField()
    harga_Produk_Termurah=models.BigIntegerField()
    link_Gambar_Produk_Termurah=models.CharField(max_length=200, blank=True)