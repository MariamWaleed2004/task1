from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poison, Category, CartItem, Cart, Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.conf import settings





def registerPage(request):
    page = 'register'
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        num = request.POST['num']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')
        
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('home')
        
        elif pass1 != pass2:
            messages.error(request, "Password didn't match")
        
        elif not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric")
            return redirect('home')
        
        elif len(username)>10:
            messages.error(request, "Username must be under 10 characters")
        
        elif len(num) != 11:
            messages.error(request, "Phonenumber must be equal 11 characters")


        else:
            user = User.objects.create_user(username, email, pass1)
            user.username = username
            user.email = email
            user.num = num
            user.is_active = True
            user.save
            login(request, user)
            messages.success(request, "Your Account Has Been Successfully Created!")
            cart = Cart.objects.create(user=user)
            cart.save()
            return redirect('home')
        
    context = {'page': page}
    return render(request, 'base/login_register.html', context)






@csrf_exempt
def loginPage(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, "Bad Credentials!")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('home')

def home(request):
    return render(request, "base/home.html")

def category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'base/category.html', context)


def searchBar(request):
    if 'q' in request.GET:
        q = request.GET['q']
        muitiple_q = Q(Q(name__icontains=q) | Q(category__icontains=q))
        products = Poison.objects.filter(muitiple_q)
    context = {'products': products}
    return render(request, 'base/searchbar.html', context)



def product(request, pk):
    product = Poison.objects.get(id=pk)
    context = {'product' : product}
    return render(request, 'base/product.html', context)





@login_required(login_url='login')
def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    product_name = Poison.objects.get(id=product_id)
    product = Poison.objects.filter(id=product_id)
    for p in product:
        price = p.price
        user_cart = Cart.objects.get(user=request.user)
        CartItem(user=request.user, product=product_name, price=price, cart=user_cart).save()
    return redirect(f'/product/{product_id}')



@login_required(login_url='login')
def checkout(request):
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.get(user=request.user)
    Order(user=request.user, cart=cart).save()
    CartItem.objects.filter(user=request.user).update(ordered=True)

    return redirect('home')



    


def cartitem(request, pk):
    cartitem = CartItem.objects.get(id=pk)

    if request.method == 'POST':
        cartitem = CartItem.objects.create_user(
            user = request.user,
            cartitem = cartitem,  
        )
        return redirect('cartitem', pk=cartitem.id)

    context = {'cartitem': cartitem}        
    return render(request, 'base/cartitem.html', context)





@login_required(login_url='login')
def cart(request, pk):
    user = User.objects.get(id=pk)
    cartitems = CartItem.objects.filter(user= request.user,ordered=False).all()
    if cartitems:
        print("Hello")
        context = {'user': user, 'cartitems' : cartitems}
        return render(request, 'base/cart.html', context)
    else:
        print("Mariam")
        return render(request, 'base/emptyCart.html')


  
   
    
    



def products(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    products = Poison.objects.filter(category__icontains=q)

    context = {'products': products}
    return render(request, 'base/products.html', context)



# def checkout(request):
#     user = User.objects.filter(id=request.user.id).first()
#     products = Poison.objects.filter().values()

#     cart = Cart.objects.filter(user=request.user).values()

#     cartItem = CartItems.objects.filter(user=request.user, ordered=False).values()
    
#     cartItems = CartItems.objects.filter(user=request.user, ordered=False)

#     categories = Category.objects.filter()


#     for getting_Id in cartItem:
#         cartItem_id = getting_Id['id']



#     if request.method == 'POST':
#         Order.objects.create(
#             user=request.user)
#         order = Order.objects.filter(
#             user=request.user, delivered=False, paid=False).values()
        
#         for getting_Id in order:
#             order_id = getting_Id['id']
#         order_id
#         print(order_id)

        
#         CartItems.objects.filter(user=request.user, id=cartItem_id).update(
#             ordered=True,
#             orderId=order_id,
#         )
#         Cart.objects.filter(user=request.user).update(total_price=0)


        
#         return redirect('base/thankyou')
#     return render(request, 'base/checkout.html')


@login_required(login_url='login')
def thankYou(request):
    return render(request, 'base/thank-you.html')

