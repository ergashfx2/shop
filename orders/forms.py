from django import forms

from orders.models import Order


class CreateOrder(forms.Form):
    name = forms.CharField(label="Ismingizni kiriting", max_length=100)
    phone = forms.CharField(label="Raqamingizni kiriting", max_length=100)
    location = forms.ChoiceField(label="Manzilingizni tanlang", choices=(
        ('choice', 'Manzilingizni tanlash'),
        ('Toshkent Shahri', 'Toshkent Shahri'),
        ('Andijon Viloyati', 'Andijon Viloyati'),
        ('Buxoro Viloyati', 'Buxoro Viloyati'),
        ("Farg'ona Viloyati", "Farg'ona Viloyati"),
        ('Jizzax Viloyati', "Jizzax Viloyati"),
        ("Qoraqalpog'iston Respublikasi", "Qoraqalpog'iston Respublikasi"),
        ('Namangan Viloyati', "Namangan Viloyati"),
        ('Navoiy Viloyati', "Navoiy Viloyati"),
        ('Samarqand Viloyati', "Samarqand Viloyati"),
        ('Surxondaryo Viloyati', "Surxondaryo Viloyati"),
        ('Toshkent Viloyati', "Toshkent Viloyati"),
        ('Xorazm Viloyati', "Xorazm Viloyati"),
    ))


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_phone','customer_location','customer_name','status']

