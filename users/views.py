from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .password_check import is_strong_password
from .forms import CustomUserCreationForm, LoginForm, EditProfileForm
from .models import CustomUser
import logging
from django.contrib.auth.hashers import make_password
from products.models import Product
from django.contrib.auth.decorators import login_required
from orders.models import Order


def HomePage(request):
    users = CustomUser.objects.all()
    products = Product.objects.all()
    # Set the number of products to display per page
    products_per_page = 12

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
        location = request.POST.get('location')
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
            user_profile.location = location
            user_profile.password = password
            user_profile.image = image
            user_profile.save()
            return redirect("signin")
    else:
        return render(request, 'signup.html')


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
    user = CustomUser.objects.get(username=request.user.username)
    context = {
        'user': user
    }
    return render(request, template_name="profile.html", context=context)


@login_required
def MyOrders(request):
    if request.user.is_staff:
        orders = Order.objects.all()
        user = CustomUser.objects.get(username=request.user.username)
    else:
        orders = Order.objects.filter(customer_phone=request.user.phone)
        user = CustomUser.objects.get(username=request.user.username)

    context = {
        'orders': orders,
        'user': user
    }

    return render(request, template_name="orders.html", context=context)


@login_required
def Notifications(request):
    if request.user.is_staff:
        orders = Order.objects.all()
        user = CustomUser.objects.get(username=request.user.username)
    else:
        orders = Order.objects.filter(customer_phone=request.user.phone)
        user = CustomUser.objects.get(username=request.user.username)

    context = {
        'orders': orders,
        'user': user
    }

    return render(request, template_name="orders.html", context=context)


@login_required
def EditProfile(request):
    user = request.user  # Assuming the user is authenticated
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after a successful update
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})


def About(request):
    return render(request, template_name="about.html")


def Password_Reset(request):
    return render(request, template_name="password_reset.html")


def Settings(request):
    return render(request, template_name="settings.html")


def Contact(request):
    return render(request, template_name="contact.html")
