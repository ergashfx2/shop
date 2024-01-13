from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .password_check import is_strong_password
from .forms import LoginForm, EditProfileForm
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from products.models import Product
from django.contrib.auth.decorators import login_required
from orders.models import Order
from django_user_agents.utils import get_user_agent


def HomePage(request):
    users = CustomUser.objects.all()
    products = Product.objects.all()
    user_agent = get_user_agent(request)
    products_per_page = 0
    if user_agent.is_pc:
        products_per_page = 18
    elif user_agent.is_mobile:
        products_per_page = 12
    elif user_agent.is_tablet:
        products_per_page = 16

    paginator = Paginator(products, products_per_page)
    page = request.GET.get('page')

    products = paginator.get_page(page)

    context = {
        'products': products,
        'users': users,
        'agent' : user_agent
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
            return render(request, 'registration/signup.html', )
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Bu email manzili ro'yxatdan o'tgan ! Iltimos boshqa email kiriting")
            return render(request, 'registration/signup.html', )
        elif not is_strong_password(password1):
            messages.error(request, "Bu parol juda ham oson ! Iltimos boshqa qiyinroq parol kiriting")
            return render(request, 'registration/signup.html', )
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
        return render(request, 'registration/signup.html')


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
    return render(request, "registration/signin.html", {'form': form})


def my_logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def Profile(request):
    user = CustomUser.objects.get(username=request.user.username)
    context = {
        'user': user
    }
    return render(request, template_name="user/profile.html", context=context)


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

    return render(request, template_name="order/orders.html", context=context)


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

    return render(request, template_name="order/orders.html", context=context)


@login_required
def EditProfile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'registration/edit_profile.html', {'form': form})


def About(request):
    return render(request, template_name="user/about.html")


def Password_Reset(request):
    return render(request, template_name="registration/password_reset.html")


def Settings(request):
    return render(request, template_name="user/settings.html")


def Contact(request):
    return render(request, template_name="user/contact.html")
