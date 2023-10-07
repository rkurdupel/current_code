# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect
from .models import Order
def order_home_page(request):
    user = request.user
    is_admin = int(user.role) == 1

    return render(request, "order_home.html", {"is_admin": is_admin})

def all_orders(request):
    data = Order.objects.get()
    
    return render(request, "all_orders.html",  {"orders": data})

def create_order(request):
    return render(request, "create_order.html")