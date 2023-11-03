from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photo/%y/%m/%d")


    def __str__(self):
        return self.name



class Poison(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to="photo/%y/%m/%d")
    active = models.BooleanField(default=True)
    categories = [
        ('Scorpion Poisons', 'Scorpion Poisons'),
        ('Snake Venom', 'Snake Venom'),
        ('Plant Toxins', 'Plant Toxins'),
        ('Animal Toxins', 'Animal Toxins'),
    ]
    category = models.CharField(max_length=50, null=True, blank=True, choices=categories)

    def __str__(self):
        return self.name
    
  


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    total_price = models.FloatField(default=0)
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)                       
    product = models.ForeignKey(Poison, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    totalOrderItemPrice = models.PositiveIntegerField(default=0)





    def __str__(self):
        return str(self.product.name) 




class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    totalPrice = models.PositiveIntegerField(default=0)
    deliveryFees = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.user)



    def get_total(self):
        total = 0
        for order_item in self.item.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total








    









