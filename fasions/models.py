from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank= True)
    name = models.CharField(max_length= 200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    productName = models.CharField(max_length=60,null=True,blank=True)
    brand = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    wrong_price = models.IntegerField(null=True, blank=True)
    correct_price = models.IntegerField(null=True, blank=True)
    delivery_charge = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse ("updateCart", kwargs={"id": self.id})


class Product_images(models.Model):    
    img = models.ImageField(upload_to='pics')
    image_product= models.ForeignKey(Product, on_delete=models.CASCADE)

class Products_size(models.Model):
    size = models.CharField(max_length=60)
    size_product= models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)    
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def ICartQuantity(self):
        return reverse ("ICartQuantity", kwargs={"id": self.id})

    @property
    def DCartQuantity(self):
        return reverse ("DCartQuantity", kwargs={"id": self.id})

    @property
    def deleteCartQuantity(self):
        return reverse ("deleteCartQuantity", kwargs={"id": self.id})

class Wishlist(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True) 
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)

    def __self__(self):
        return self.user.user.username +" - "+ self.product.brand

class Address(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True) 
    country=models.CharField(max_length=20)
    streetAdreess = models.CharField(max_length=100)
    apartment = models.CharField(max_length = 30, null=True, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length = 20)
    postcode = models.CharField(max_length = 10)

    def __self__(self):
        return self.user.user.username

class Checkout(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL,null=True)
    Cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    date  = models.DateTimeField(auto_now_add = True)
    ordered = models.BooleanField(default=False)
    orderName = models.CharField(max_length=20,null=True,blank=True)
    
    def __self__(self):
        return self.user.user.username






    
     



