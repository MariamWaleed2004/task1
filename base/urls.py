from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),



    path('', views.home, name="home"),
    path('category/', views.category, name="category"),


    path('product/<str:pk>/', views.product, name="product"),
    path('searchbar/',views.searchBar, name="searchbar"),
    path('products/', views.products, name="products"),


    path('cartitem/<str:pk>/', views.cartitem, name="cartitem"),
    path('cart/<str:pk>/', views.cart, name="cart"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('checkout/', views.checkout, name="checkout"),



    path('thank-you/', views.thankYou, name="thank-you"),

]