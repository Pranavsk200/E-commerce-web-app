from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    # path('shop', views.shop, name='shop'),
    path("cart",views.cart, name="cart"),
    path("updateCart/<id>",views.updateCart, name="updateCart"),
    path("ICartQuantity/<id>",views.ICartQuantity, name="ICartQuantity"),
    path("DCartQuantity/<id>",views.DCartQuantity, name="DCartQuantity"),
    path("deleteCartQuantity/<id>",views.deleteCartQuantity, name="deleteCartQuantity"), 
    path("login",views.login, name="login"),
    path("signin",views.signin, name="signin"),
    path("logout",views.log_out, name="logout"),
    path("detaiels/<id>",views.product_details, name="detaiels"),
    path("checkout",views.checkout, name="checkout"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("updateWishlist/<id>", views.updateWishlist, name="updateWishlist"),
    path("checkout", views.checkout, name="checkout"),
    path('search', views.search,name='search')
]