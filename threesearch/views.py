from django.shortcuts import render
from threeshop.models import Product

# Create your views here.

def do_search(request):
    products = Product.object.filter(name__icontains=request.GET['q'])
    return render(request, "shop.html",{"products":products})