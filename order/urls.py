from django.urls import path
from .views import order_home_page, all_orders, create_order

urlpatterns = [
    path('', order_home_page, name = 'order_home_page'),
    path("all_orders/", all_orders, name = "all_orders"),
    path('create_order/', create_order, name = "create_order")
]