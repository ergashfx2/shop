from django import forms
from orders.models import Order

class CreateOrder(forms.Form):
    name = forms.CharField(label="Ismingizni kiriting", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Raqamingizni kiriting", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
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
    ), widget=forms.Select(attrs={'class': 'form-select'}))

    def clean(self):
        cleaned_data = super().clean()

        # Strip spaces from all fields
        for field in self.fields:
            if cleaned_data.get(field):
                cleaned_data[field] = cleaned_data[field].strip()

        return cleaned_data


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_phone', 'customer_location', 'customer_name', 'status']
        widgets = {
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_location': forms.Select(attrs={'class': 'form-select'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Strip spaces from all fields
        for field in self.fields:
            if cleaned_data.get(field):
                cleaned_data[field] = cleaned_data[field].strip()

        return cleaned_data
