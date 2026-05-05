from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')




from django.views.generic import ListView, DetailView, TemplateView
from .models import Product
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'catalog/index.html'
#     context_object_name = 'products'
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/product_detail.html'
#     context_object_name = 'product'
#
class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
#
#
class HomeView(TemplateView):
    template_name = 'catalog/home.html'




#
# from django.shortcuts import render
#
# # Create your views here.
#
# def home(request):
#     return render(request, 'catalog/home.html')
#
#
# def contacts(request):
#     return render(request, 'catalog/contacts.html')
#
#
# from django.shortcuts import get_object_or_404
# from .models import Product
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'catalog/product_detail.html', {'product': product})
#
#
# def index(request):
#     products = Product.objects.all()
#     return render(request, 'catalog/index.html', {'products': products})
