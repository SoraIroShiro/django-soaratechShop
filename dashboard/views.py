from django.shortcuts import render, redirect 
from dashboard.forms import FormProduk, FormHotsale, FormTermurah
from dashboard.models import Produk, Termurah, Hotsale, Merkp
from django.contrib import messages 

# Create your views here.
def tambah_produk(request):
    if request.POST:
        formp= FormProduk(request.POST)
        formh= FormHotsale(request.POST)
        formt= FormTermurah(request.POST)

        if formp.is_valid():
            if formp.save():
                messages.success(request, "Data Produk Berhasil Ditambahkan")
                formp = FormProduk()
                konteks = {
                    'formp':formp
                }
                return render (request,'tambah_barang.html',konteks)
        
        elif formh.is_valid():
            if formh.save():
                messages.success(request, "Data Produk Hotsale Berhasil Ditambahkan")
                formh = FormHotsale()
                konteks = {
                    'formh':formh
                }
                return render (request,'tambah_barang.html',konteks)
        
        elif formt.is_valid():
            if formt.save():
                messages.success(request, "Data Produk Termurah Berhasil Ditambahkan")
                formt = FormTermurah()
                konteks = {
                    'formt':formt
                }
                return render (request,'tambah_barang.html',konteks)
        
    else:
        formp=FormProduk()
        formh=FormHotsale()
        formt=FormTermurah()
        konteks ={
            'formp': formp,
            'formh': formh,
            'formt': formt
        }

    return render (request,'tambah_barang.html',konteks)



def tampil_barang(request):
    produks=Produk.objects.all()
    termurahs=Termurah.objects.all()
    hotsales=Hotsale.objects.all()
    merkps=Merkp.objects.all()
    
    konteks={
        'produks':produks, 
        'termurahs':termurahs, 
        'hotsales':hotsales , 
        'merkp': merkps

    }

    return render(request,'tampil_barang.html',konteks)

def tampil_barang_base(request):
    termurahs=Termurah.objects.all()
    hotsales=Hotsale.objects.all()
    titlenya ="Home"
    
    konteks={
        'termurahs':termurahs, 
        'hotsales':hotsales,
        'title' : titlenya,
        

    }

    return render(request,'base.html',konteks)

def tampil_barang_produk(request):
    produks=Produk.objects.all()
    termurahs=Termurah.objects.all()
    hotsales=Hotsale.objects.all()
    merkps=Merkp.objects.all()
    titlenya ="Produk Tersedia"
    
    konteks={
        'produks': produks,
        'title' : titlenya,
        'termurahs':termurahs, 
        'hotsales':hotsales, 

    }

    return render(request,'produkrdy.html',konteks)

def ubah_brgprod(request,id_produk):
    produks=Produk.objects.get(id=id_produk)
    if request.POST:
        formp=FormProduk(request.POST,instance=produks)
        if formp.is_valid():
            formp.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_brgprod', id_produk=id_produk)
    
    else:
        formp=FormProduk(instance=produks)
        konteks = {
            'formp':formp,
            'produks':produks
        }
    return render(request,'ubah_brgprod.html',konteks)

def ubah_brgter(request,id_termurah):
    termurahs=Termurah.objects.get(id=id_termurah)
    if request.POST:
        formt=FormTermurah(request.POST,instance=termurahs)
        if formt.is_valid():
            formt.save()
            messages.success(request,"Data Produk Termurah Berhasil Diubah")
            return redirect('ubah_brgprod', id_produk=id_termurah)
    
    else:
        formt=FormTermurah(instance=termurahs)
        konteks = {
            'formt':formt,
            'termurahs':termurahs
        }
    return render(request,'ubah_brgter.html',konteks)

def ubah_brghot(request,id_hotsale):
    hotsales=Hotsale.objects.get(id=id_hotsale)
    if request.POST:
        formh=FormHotsale(request.POST,instance=hotsales)
        if formh.is_valid():
            formh.save()
            messages.success(request,"Data Produk Hotsale Berhasil Diubah")
            return redirect('ubah_brghot', id_hotsale=id_hotsale)
    
    else:
        formh=FormHotsale(instance=hotsales)
        konteks = {
            'formh':formh,
            'hotsales':hotsales
        }
    return render(request,'ubah_brghot.html',konteks)


def hapus_brghot(request,id_hotsale):
    hotsales=Hotsale.objects.filter(id=id_hotsale)
    hotsales.delete()
    messages.success(request,"Data Produk Hotsale terhapus")
    return redirect('vbrg')

def hapus_brgpro(request,id_produk):
    produks=Produk.objects.filter(id=id_produk)
    produks.delete()
    messages.success(request,"Data Produk terhapus")
    return redirect('vbrg')

def hapus_brgter(request,id_termurah):
    termurahs=Termurah.objects.filter(id=id_termurah)
    termurahs.delete()
    messages.success(request,"Data Produk Termurah terhapus")
    return redirect('vbrg')