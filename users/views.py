from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
import logging

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
        password = request.POST['password1']

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect("home")
        else:
            print(logging.error)
            # You can handle authentication failure here
            pass

    # For GET requests or when authentication fails, return the sign-in form
    return render(request, "signin.html")


def my_logout_view(request):
    logout(request)
    return redirect('home')


def Password_Reset(request):
    return render(request, template_name="password_reset.html")
