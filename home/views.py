from django.shortcuts import render, redirect
from product.models import Product


def index(request):
    context = {'products' : Product.objects.all()}
    return render(request, 'home/index.html', context)