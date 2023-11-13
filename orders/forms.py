from django import forms


class CreateOrder(forms.Form):
    name = forms.CharField(label="Ismingizni kiriting", max_length=100)
    phone = forms.CharField(label="Raqamingizni kiriting", max_length=100)
    location = forms.ChoiceField(label="Manzilingizni tanlang",choices=(
        ('choice', 'Manzilni tanlash'),
        ('toshkent', 'Toshkent Shahri'),
        ('andijon', 'Andijon Viloyati'),
        ('buxoro', 'Buxoro Viloyati'),
        ('fargona', "Farg'ona Viloyati"),
        ('jizzax', "Jizzax Viloyati"),
        ('qoraqalpogiston', "Qoraqalpog'iston Respublikasi"),
        ('namangan', "Namangan Viloyati"),
        ('navoiy', "Navoiy Viloyati"),
        ('samarqand', "Samarqand Viloyati"),
        ('surxondaryo', "Surxondaryo Viloyati"),
        ('toshkent_viloyati', "Toshkent Viloyati"),
        ('xorazm', "Xorazm Viloyati"),
    ))
