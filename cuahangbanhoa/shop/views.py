from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def base(request):
    products = Product.objects.all()
    categories = {}
    for product in products :
        category_name = dict(product.category_choices)[product.category]
        if category_name not in categories:
            categories[category_name] = []
        categories[category_name].append(product)
    return render(request,"shop/base.html" , {'products': products, 'categories': categories})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None :
            login(request,user)
            messages.success(request,"ĐĂNG NHẬP THÀNH CÔNG")
            return redirect('base')
        else:
            messages.error(request,"LỖI ĐĂNG NHẬP")
            
    return render (request , "shop/login.html")

def reg(request):
    user = None
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if not email or not username or not password1 or not password2:
            messages.error(request , "VUI LÒNG ĐIỀN ĐẦY ĐỦ THÔNG TIN")
        elif password1 != password2 :
            messages.error(request , "MẬT KHẨU KHÔNG TRÙNG KHỚP")
        elif User.objects.filter(username=username).exists():
            messages.error(request , "TÊN TÀI KHOẢN TỒN TẠI")
        elif User.objects.filter(email=email).exists():
            messages.error(request , "TÊN EMAIL TỒN TẠI")
        else:
            user = User(username=username , email = email, )
            user.set_password(password1)
            user.save()
            messages.success(request,"ĐĂNG KÝ THÀNH CÔNG")
            return redirect('login')
    context = {'user':user}
    return render(request, "shop/reg.html", context)
def home_view(request):
    return render(request , "shop/home.html")
def logout_view(request):
    logout(request)
    return render(request, 'shop/logout.html')
def search_view(request):
    if request.method == "POST":
        search_query = request.POST["search"]
        keys = Product.objects.filter(name__contains = search_query)
    return render(request, "shop/search.html",{'search_query' : search_query,'keys':keys})
def cart_view(request):
    return render(request,"shop/cart.html")
def detail_view(request):
    products = Product.objects.all()
    return render(request,"shop/detail.html",{'Product': products})