from django.urls import path
from . import views
from .views import login_view, register

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
