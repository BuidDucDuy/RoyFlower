from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
        search_query = request.POST.get("search", "")
        keys = Product.objects.filter(name__icontains=search_query)
        return render(request, "shop/search.html", {
            'search_query': search_query,
            'keys': keys
        })
    return redirect('home')
    return render(request, "shop/search.html",{'search_query' : search_query,'keys':keys ,'product': product })
def cart_view(request):
    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user = request.user)
        cart_items = Cart_item.objects.filter(cart = cart)
        return render(request,"shop/cart.html",{"cart_items":cart_items})
    else:
        return redirect('login')
def add_to_cart(request , product_id):
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)
        cart_item,created = Cart_item.objects.get_or_create(cart=cart , product = product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart')
        else:
            return redirect('cart')        
def detail_view(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    return render(request,"shop/detail.html",{'product': product})          

@login_required
def delete_cart_item(request , product_id):
    cart_item= Cart_item.objects.get(id = product_id)
    cart_item.delete()
    return redirect('cart')