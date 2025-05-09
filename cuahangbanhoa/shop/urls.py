from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView 
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path("",views.base ,name="base"),
    path("login/",views.login_view,name="login"),
    path("reg/",views.reg,name='reg'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path("search/",views.search_view,name='search'),
    path("cart/",views.cart_view,name='cart'),
    path("detail/<int:product_id>/",views.detail_view,name='detail'),
    path("add_to_cart/<int:product_id>/",views.add_to_cart,name='add_to_cart'),
    path("home/",views.home_view,name='home'),
    path("delete_cart_item/<int:product_id>",views.delete_cart_item,name='delete_product'),
    
]
 