from django.contrib import admin
from django.urls import path
from .views.home import Index , store
#from .views.home import *
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .view import scrape_and_save
from .views.checkout import checkout

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store/', store , name='store'),
#*********scraping***************
    path('store', scrape_and_save, name='products'),
#********************************
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('checkout', checkout, name="checkout"),



]
