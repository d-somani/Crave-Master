from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.middleware.authorization import Auth_Middleware
from django.utils.decorators import method_decorator
class Cart(View):

    @method_decorator(Auth_Middleware)
    def get(self , request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)

        return render(request, 'cart.html' , {'products' : products})
