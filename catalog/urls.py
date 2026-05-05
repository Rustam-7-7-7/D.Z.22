from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    HomeView, ContactView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),


    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
]




# from django.urls import path
# from .views import ProductListView, ProductDetailView, ContactView, HomeView
#
# urlpatterns = [
#     path('', ProductListView.as_view(), name='index'),
#     path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
#     path('contacts/', ContactView.as_view(), name='contacts'),
#
#     path('home/', HomeView.as_view(), name='home'),
# ]



# from django.urls import path
# from catalog import views
#
# urlpatterns = [
#     path('home/', views.home, name='home'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail'),
#     path('index/', views.index, name='index'),
# ]
