from django.urls import path
from .views import ProductListView, ProductDetailView, ContactView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
]



# from django.urls import path
# from catalog import views
#
# urlpatterns = [
#     path('home/', views.home, name='home'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail'),
#     path('index/', views.index, name='index'),
# ]
