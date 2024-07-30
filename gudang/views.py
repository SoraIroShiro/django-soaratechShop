from django.shortcuts import render
from dashboard.models import Produk, Termurah, Hotsale, Merkp

# Create your views here.

def home(request):
    titelnya = "Home"
    konteks = {
        'title' : titelnya,
    }
    return render(request,'base.html', konteks)

def produk(request):
    titelnya = "Produk"
    konteks = {
        'titel': titelnya,
    }
    return render(request,'produk.html',konteks)

def kontak(request):
    titelnya = "Kontak"
    konteks = {
        'titel': titelnya,
    }
    return render(request,'kontak.html',konteks)


def tentang(request):
    termurahs=Termurah.objects.all()
    hotsales=Hotsale.objects.all()
    titlenya = "Tentang Kami"
    konteks = {
        'title': titlenya,
        'termurahs':termurahs, 
        'hotsales':hotsales,
    }
    return render(request, 'tentang.html',konteks)

def alamat(request):
    termurahs=Termurah.objects.all()
    hotsales=Hotsale.objects.all()
    titlenya = "Alamat Anda"
    konteks = {
        'title': titlenya,
        'termurahs':termurahs, 
        'hotsales':hotsales,
    }
    return render(request, 'alamat.html',konteks)

def krisar(request):
    titlenya = "Kritik Dan Saran dari Anda"
    konteks = {
        'title': titlenya,
    }
    return render(request, 'krisar.html',konteks)

def tampil(request):
    titlenya = "Management Produk"
    konteks = {
        'title': titlenya,
    }
    return render(request, 'tampil_barang.html',konteks)

def tampilp(request):
    titlenya = "Management Produk"
    konteks = {
        'title': titlenya,
    }
    return render(request, 'tampil_produk.html',konteks)

