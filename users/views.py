from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
import logging
from django.contrib.auth.hashers import make_password
def HomePage(request):
    return render(request, template_name="home.html")


def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        age = request.POST['age']
        email = request.POST['email']
        password1 = request.POST['password1']

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
            print(username, password)
    return render(request, "signin.html")


def my_logout_view(request):
    logout(request)
    return redirect('home')


def Password_Reset(request):
    return render(request, template_name="password_reset.html")
