from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from orders.forms import CreateOrder
from orders.models import Order
from users.models import CustomUser
from .models import Product


def product_list_view(request):
    products = Product.objects.all()

    # Set the number of products to display per page
    products_per_page = 6

    paginator = Paginator(products, products_per_page)
    page = request.GET.get('page')

    products = paginator.get_page(page)

    return render(request, 'home.html', {'products': products})


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
        form = CreateOrder(request.POST)
        if form.is_valid():
            product_name = Product.objects.get(pk=pk).title
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            location = form.cleaned_data['location']

            # Save order to the Order model
            order = Order.objects.create(
                product=product_name,  # Replace with the actual field you want to save
                customer_name=name,
                customer_phone=phone,
                customer_location=location
            )
            return redirect('order_success')

    return render(request, "product_detail.html", product)
