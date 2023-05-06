from django.views import View
import requests
from django.shortcuts import render
from .utils import cookieCart, cartData, guestOrder

def checkout(request):
	data = cartData(request)
	
	orders = data['orders']

	context = { 'orders':orders,}
	return render(request, 'checkout.html', context)