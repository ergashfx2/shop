from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .password_check import is_strong_password
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser
import logging
from django.contrib.auth.hashers import make_password


def HomePage(request):
    return render(request, template_name="home.html")

def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Foydalanuvchi nomi band ! Iltimos boshqa nom o'ylab toping")
            return render(request, 'signup.html', {'form': CustomUserCreationForm()})
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Bu email manzili ro'yxatdan o'tgan ! Iltimos boshqa email kiriting")
            return render(request, 'signup.html', {'form': CustomUserCreationForm()})
        elif not is_strong_password(password1):
            messages.error(request, "Bu parol juda ham oson ! Iltimos boshqa qiyinroq parol kiriting")
            return render(request, 'signup.html', {'form': CustomUserCreationForm()})
        else:
            password = make_password(password1)
            user_profile = CustomUser()
            user_profile.username = username
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.phone = phone
            user_profile.age = age
            user_profile.email = email
            user_profile.password = password
            user_profile.save()

        return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def SignIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=f"{username}", password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            pass
    form = LoginForm()
    return render(request, "signin.html", {'form': form})


def my_logout_view(request):
    logout(request)
    return redirect('home')


def Password_Reset(request):
    return render(request, template_name="password_reset.html")
