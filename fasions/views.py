from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth import authenticate, login as dj_login,logout
from .models import *
from django.contrib import messages
from django.db.models import Q

# Create your views here
def home(request):
    return render(request,"index.html")

# def shop(request):
#     name = request.search
#     products=Product.objects.filter(Q(productName__icontains = name)|Q(brand__icontains = name))
#     count= products.count()
#     context =  {
#         'products': products,
#         'count':count
#         }
#     return render(request,"shop.html",context)

def cart(request):
    if request.user.is_authenticated:
        user=request.user.customer
        cart=Cart.objects.filter(user=user)
        count = 0
        s=0
        for c in cart:
            s +=  c.product.correct_price
        for i in cart:
            count += 1
        context={
            'cart':cart,
            'Total':s,
            'count':count
        }
        return render(request, "shopping-cart.html",context)
    else:
        return redirect("login")    

def updateCart(request,id=None):
    if request.user.is_authenticated:
        product=Product.objects.get(id=id)
        user=request.user.customer
        cart, created=Cart.objects.get_or_create(user=user, product=product) 
        cart.save() 
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect("login")    

def ICartQuantity(request,id=None):
    cart=Cart.objects.get(id=id) 
    cart.quantity=(cart.quantity+1)
    cart.save() 
    return redirect("/cart")

def DCartQuantity(request,id=None):
    cart=Cart.objects.get(id=id) 
    if cart.quantity<=1:
        cart.delete()
    else:
        cart.quantity=(cart.quantity-1)
        cart.save() 
    return redirect("/cart")

def  deleteCartQuantity(request,id=None):
    cart=Cart.objects.get(id=id) 
    cart.delete()
    return redirect("/cart") 

def login(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['pass']
        user=authenticate(username=name, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect("home")
        else:
            messages.info(request, "username or password is incorrect") 
            return redirect("login")   
    else:    
        return render(request, "login.html")

def signin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        first_name = request.POST['first_name']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['pass']
        repassword = request.POST['repass']
        if password==repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"user name already exists,please resistor with another username")    
            else:    
                user =User.objects.create_user(username=username,first_name=first_name, email=email, password=password)
                user.save()
                print('user created')
                return render(request, 'login.html')
        else:
            messages.info(request, "conform passowerd and password are not matching")
    else:
        return render(request, "sign-in.html") 

def log_out(request):
    logout(request)
    messages.info(request,"you have succesfully logout")
    return redirect("login")

def product_details(request,id=None):
    product = Product.objects.filter(id=id)[0]
    product_images = Product_images.objects.filter(image_product=product)
    context={
        'product':product,
        'images':product_images
    }
    return render(request, "shop-details.html",context)    

def checkout(request):
    if request.user.is_authenticated:
        user = request.user.customer
        cart = Cart.objects.filter(user = user)
        address = Address.objects.filter(user = user)[0]
        print(address.country)
        total = 0
        count =0
        for i in cart:
            count += 1 
            total += i.product.correct_price

        context = {
            'cart':cart,
            'address':address,
            'total':total,
            'count':count,
            'user':user 
        }
        return render(request,'checkout.html',context)
    else:
        return redirect("login")       

def wishlist(request,id=None):
    if request.user.is_authenticated:
        user=request.user.customer
        WishList = Wishlist.objects.filter(user=user)   
        count = 0
        for i in WishList:
            count+=1

        context = {
            'wishlists' : WishList,
            'count': count
        } 
        return render(request, 'wishlist.html',context)
    else:
        return redirect("login")       

def updateWishlist(request,id=None):
    if request.user.is_authenticated:
        user = request.user.customer
        product=Product.objects.get(id=id)
        user_wishlist = Wishlist.objects.filter(user=user)
        if user_wishlist.filter(product=product).exists()==False:
            product=Product.objects.get(id=id)
            w=Wishlist(user=user,product=product)
            w.save()
            return redirect(request.META['HTTP_REFERER'])
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect("login")    

def search(request):
    if request.method == 'POST' :
        name = request.POST['search']
        products=Product.objects.filter(Q(productName__icontains = name)|Q(brand__icontains = name))
        product_count = products.count()
        context = {
            'products':products,
            'count':product_count
        }
        return render(request,'shop.html', context)    
    return render(request,'search.html')    
    
        
