from django import forms
from django.utils.html import conditional_escape
from django_summernote.widgets import SummernoteWidget

from products.models import Product, PRODUCT_TYPE_CHOICES



class AddProduct(forms.ModelForm):
    description = forms.CharField(label="Mahsulot haqida batafsil ma'lumot", widget=SummernoteWidget())
    title = forms.CharField(label="Mahsulot nomi")
    type = forms.ChoiceField(label="Mahsulot kategoriyasini tanlang", choices=PRODUCT_TYPE_CHOICES)
    price = forms.IntegerField(label="Mahsulot narxi")
    image = forms.ImageField(label="Mahsulot rasmini kiriting")

    class Meta:
        model = Product
        fields = ['title', 'description', 'type', 'price', 'image']


class EditProduct(forms.ModelForm):
    description = forms.CharField(label="Mahsulot haqida batafsil ma'lumot", widget=SummernoteWidget())
    title = forms.CharField(label="Mahsulot nomi")
    type = forms.ChoiceField(label="Mahsulot kategoriyasini tanlang", choices=PRODUCT_TYPE_CHOICES)
    price = forms.IntegerField(label="Mahsulot narxi")
    image = forms.ImageField(label="Mahsulot rasmini kiriting")

    class Meta:
        model = Product
        fields = ['title', 'description', 'type', 'price', 'image']
