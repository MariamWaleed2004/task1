from django.contrib import admin
from .models import Poison, Category, CartItem, Cart, Order



class AdminCartItem(admin.TabularInline):
    model = CartItem
    list_display = ['id', 'user', 'product', 'price', 'quantity']





class AdminCart(admin.ModelAdmin):
    model = Cart
    list_display = ['user',
                    'total_price',
                    'ordered_date',
                    'cart_name',
                    ]
    inlines = [AdminCartItem]
    search_fields = ['user']
    

    
    def cart_name(self, obj):
        return   str(obj.user.username)
      

class AdminOrder(admin.TabularInline):
    model = Order
    list_display = ['id', 'user', 'cart', 'ordered_date', 'delivered', 'paid', 'totalPrice', "deliveryFees"]


 

admin.site.register(Poison)
admin.site.register(Category)
admin.site.register(Cart, AdminCart)
admin.site.register(CartItem)
admin.site.register(Order)













