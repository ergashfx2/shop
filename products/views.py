from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from orders.forms import CreateOrder
from orders.models import Order
from users.models import CustomUser
from .forms import AddProduct, EditProduct
from .models import Product


def Add_Product(request):
    if request.user.is_staff:
        if request.method == 'POST':
            if request.user.is_authenticated:
                form = AddProduct(request.POST, request.FILES)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    description = form.cleaned_data['description']
                    price = form.cleaned_data['price']
                    type = form.cleaned_data['type']
                    image = form.cleaned_data['image']
                    product = Product.objects.create(
                        title=title,  # Replace with the actual field you want to save
                        description=description,
                        type=type,
                        price=price,
                        image=image

                    )

                    return redirect('home')
        else:
            form = AddProduct()
            return render(request, "add_product.html", {"form": form})


def Edit_Product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = EditProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProduct(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})


def Search_Product(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(title__contains=searched)

        return render(request,
                      'search_product.html',
                      {'searched': searched,
                       'products': products})
    else:
        return render(request,
                      'home.html',
                      {})


def ProductFilter(request, category):
    products = Product.objects.filter(type=category)
    context = {
        "products": products
    }
    return render(request, "home.html", context)


def ProductDetail(request, pk):
    product = Product.objects.get(pk=pk)
    try:
        user = CustomUser.objects.all()
        form = CreateOrder()
    except Product.DoesNotExist:
        raise Http404("Given query not found....")
    product = {
        'product': product,
        'form': form
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_name = Product.objects.get(pk=pk).title
            user = CustomUser.objects.get(username=request.user.username)
            name = user.first_name
            phone = user.phone
            location = user.location
            status = "Qabul qilindi"
            print(user.username)
            order = Order.objects.create(
                product=product_name,  # Replace with the actual field you want to save
                customer_name=name,
                customer_phone=phone,
                customer_location=location,
                status=status
            )
            return redirect('order_success')
        else:
            form = CreateOrder(request.POST)
            if form.is_valid():
                product_name = Product.objects.get(pk=pk).title
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                location = form.cleaned_data['location']
                order = Order.objects.create(
                    product=product_name,  # Replace with the actual field you want to save
                    customer_name=name,
                    customer_phone=phone,
                    customer_location=location
                )
                return redirect('order_success')

    return render(request, "product_detail.html", product)
