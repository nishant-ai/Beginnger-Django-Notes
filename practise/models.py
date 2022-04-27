from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) 
    name = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return(self.name)
    
    
class Tag(models.Model):
    name = models.CharField(max_length=220, null=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    CATEGORY = (
        ('IN', 'Indoor'),
        ('OD', 'Outdoor'),
    )
    
    name = models.CharField(max_length=220, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=2, null=True, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('PND', 'Pending'),
        ('OFD', 'Out For Delivery'),
        ('DEL', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=3, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    note = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.product.name
