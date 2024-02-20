from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index.html',views.index,name="index"),
    path('product.html',views.products,name="product"),
    path('login.html',views.login,name="login"),
    path('signup.html',views.signup,name="signup"),
    path('blog_list.html',views.blogs,name="blog"),
    path('contact.html',views.contact,name="contact"),
    path('cart.html',views.cart,name="cart"),
    
]
