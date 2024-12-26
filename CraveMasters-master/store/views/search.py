from django.shortcuts import render , redirect
from store.models import Product
from store.models.category import Category
from django.views import View

def searchmatch(query , item):
    if query in item.description.lower() or query in item.name.lower():
        return True
    return False
# Create your views here.
class Searcher(View):
    def get(self,request):
        query = request.GET.get('search')
        cart = request.session.get('cart')
        if(not cart):
            request.session['cart']={}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if (categoryID):
            products = Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        productsnew = [item for item in products if searchmatch(query, item)]
        products = productsnew
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)



