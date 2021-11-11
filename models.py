from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from django.contrib.auth.models import User


# Product Sections
class Color(models.Model):
    color_name=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.color_name

class SuperCategory(models.Model):
    superCategory_name=models.CharField(max_length=30,default="")

    def __str__(self):
        return self.superCategory_name

class Category(models.Model):
    category_name=models.CharField(max_length=30,default="")
    superCategory_name=models.ForeignKey(
        'SuperCategory',
        on_delete=models.SET_DEFAULT,
        default=""
        )


    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    product_category=models.ForeignKey(
        'Category',
        on_delete=models.SET_DEFAULT,
        default=""
        )
    product_description=models.TextField(max_length=2000,default="")
    product_price=models.IntegerField(default=0)
    product_quantity=models.IntegerField(default=0)
    product_color=models.ForeignKey(
        'Color',
        on_delete=models.SET_DEFAULT,
        default=""
    )
    product_image=models.ImageField(upload_to='shop/images',default="")
    product_date=models.DateField(default="")

    def __str__(self):
        return self.product_name



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id=models.AutoField
    receiver_name=models.CharField(max_length=50)
    receiver_email=models.EmailField(max_length = 254,default="")
    receiver_mobile=models.CharField(max_length=20)
    receiver_address=models.CharField(max_length=200)
    order_date = models.DateField(auto_now_add=True)
    total_price=models.IntegerField(default=0)
    service_charge=models.IntegerField(default=0)
    total_bill=models.IntegerField(default=0)
    payment_status=models.CharField(max_length=20,default='Not Paid')
    shipping_status=models.CharField(max_length=20,default='Not Shipped')

    def __str__(self):
        return str(self.user)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    product_quantity=models.IntegerField()
    order_id=models.ForeignKey(Order,null=True,blank=True,on_delete=models.CASCADE)
    order_status=models.CharField(max_length=20,default='Not Ordered')

    def __str__(self):
        return str(self.user)+ ' | ' + str(self.order_status)
