from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Product
from .forms import ProductForm

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модератор продуктов').exists()

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модератор продуктов').exists()





from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Product
from .forms import ProductForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_moderator'] = self.request.user.groups.filter(name='Модератор продуктов').exists()
        return context


from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .models import Product

@method_decorator(cache_page(60 * 15), name='dispatch')  # Кеширование на 15 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


from django.shortcuts import render
# from .services import get_products_by_category
#
# def products_by_category_view(request, category_id):
#     products = get_products_by_category(category_id)
#     return render(request, 'catalog/products_by_category.html', {'products': products})


from .services import get_products_by_category_with_cache

def products_by_category_view(request, category_id):
    products = get_products_by_category_with_cache(category_id)
    return render(request, 'catalog/products_by_category.html', {'products': products})


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/product_detail.html'
#     context_object_name = 'product'



# @method_decorator(login_required, name='dispatch')
# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'catalog/product_form.html'
#     success_url = reverse_lazy('product_list')
#
# @method_decorator(login_required, name='dispatch')
# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'catalog/product_form.html'
#     success_url = reverse_lazy('product_list')
#
# @method_decorator(login_required, name='dispatch')
# class ProductDeleteView(DeleteView):
#     model = Product
#     template_name = 'catalog/product_confirm_delete.html'
#     success_url = reverse_lazy('product_list')




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
