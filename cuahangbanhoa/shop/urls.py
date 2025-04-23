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
    path("detail/",views.detail_view,name='detail'),
    path("home/",views.home_view,name='home'),
]
