from django import forms
from django_summernote.widgets import SummernoteWidget

from products.models import Product


class AddProduct(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Product
        fields = ['title', 'description', 'type', 'price', 'image']


class EditProduct(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Product
        fields = ['title', 'description', 'type', 'price', 'image']
