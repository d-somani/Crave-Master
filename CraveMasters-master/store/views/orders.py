from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.middleware.authorization import Auth_Middleware
from django.utils.decorators import method_decorator
class OrderView(View):
    @method_decorator(Auth_Middleware)
    def get(self , request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'orders.html' , {'orders': orders})