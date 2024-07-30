from django import forms # type: ignore
from django.forms import ModelForm # type: ignore
from dashboard.models import Produk, Hotsale, Termurah

class FormProduk (ModelForm):
    class Meta :
        model=Produk
        fields='__all__'

        widgets = {
            'kode_Produk': forms.TextInput({'class':'form-control'}),
            'merk_Produk': forms.Select({'class':'form-control'}),
            'tipe_Produk': forms.TextInput({'class':'form-control'}),
            'stok_Produk': forms.NumberInput({'class':'form-control'}),
            'harga_Produk': forms.NumberInput({'class':'form-control'}),
            'link_Gambar_Produk': forms.TextInput({'class':'form-control'})
        }

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()


class FormHotsale (ModelForm):
    class Meta :
        model=Hotsale
        fields='__all__'

        widgets = {
            'kode_Produk_Hotsale': forms.TextInput({'class':'form-control'}),
            'merk_Produk_Hotsale': forms.Select({'class':'form-control'}),
            'tipe_Produk_Hotsale': forms.TextInput({'class':'form-control'}),
            'stok_Produk_Hotsale': forms.NumberInput({'class':'form-control'}),
            'harga_Produk_Hotsale': forms.NumberInput({'class':'form-control'}),
            'link_Gambar_Produk_Hotsale': forms.TextInput({'class':'form-control'})
        }


class FormTermurah (ModelForm):
    class Meta :
        model=Termurah
        fields='__all__'

        widgets = {
            'kode_Produk_Termurah': forms.TextInput({'class':'form-control'}),
            'merk_Produk_Termurah': forms.Select({'class':'form-control'}),
            'tipe_Produk_Termurah': forms.TextInput({'class':'form-control'}),
            'stok_Produk_Termurah': forms.NumberInput({'class':'form-control'}),
            'harga_Produk_Termurah': forms.NumberInput({'class':'form-control'}),
            'link_Gambar_Produk_Termurah': forms.TextInput({'class':'form-control'})
        }