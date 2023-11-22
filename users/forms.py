from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)



from django import forms
from .models import CustomUser


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone', 'image', 'age', 'location']



