from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


from django.shortcuts import get_object_or_404
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def index(request):
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {'products': products})
