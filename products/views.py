from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to show all cars, with sorting and searches """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)