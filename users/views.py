from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .password_check import is_strong_password
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser
import logging
from django.contrib.auth.hashers import make_password
from products.models import Product
from django.contrib.auth.decorators import login_required


def HomePage(request):
    users = CustomUser.objects.all()
    products = Product.objects.all()
    # Set the number of products to display per page
    products_per_page = 10

    paginator = Paginator(products, products_per_page)
    page = request.GET.get('page')

    products = paginator.get_page(page)

    context = {
        'products': products,
        'users': users
    }
    return render(request, template_name="home.html", context=context)


def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        image = request.FILES.get('image')
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
            user_profile.image = image
            user_profile.save()
            user = authenticate(request, username=f"{username}", password=password)
            if user:
                login(request, user)
                return redirect("home")
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


@login_required
def Profile(request):
    user = CustomUser.objects.get(username = request.user.username)
    context = {
        'user': user
    }
    return render(request, template_name="profile.html", context=context)


def Password_Reset(request):
    return render(request, template_name="password_reset.html")
