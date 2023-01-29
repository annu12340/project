import random
from django.shortcuts import redirect, render
from .models import Product
from qrcode_details.models import Orders


def shop_page(request):
    data = Product.objects.filter()
    recommended_products = data[:3]
    remaining_products = data[3:]
    context = {
        'recommended_products': recommended_products,
        'remaining_products': remaining_products
    }
    return render(request, 'shop/shop.html', context)


def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    related_products = Product.objects.exclude(id=product_id)[:4]
    context = {
        'product': product_details,
        'related_products': related_products
    }

    return render(request, 'shop/product-details.html', context)


def my_orders(request):
    order = Orders.objects.filter(user_id=request.user.id)
    data = list(order.values())[0]['product_id']
    products = Product.objects.filter(id=2)

    context = {
        'products': products,
    }
    return render(request, 'shop/orders.html', context)


def maps(request):
    return render(request, 'shop/recently_seen_places.html')


def checkout(request):
    return render(request, 'checkout.html')


def successful(request):
    return render(request, 'succesfull.html')
