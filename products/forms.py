from django import forms

from products.models import Product


class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'type', 'price', 'image']


class EditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'type', 'price', 'image']
