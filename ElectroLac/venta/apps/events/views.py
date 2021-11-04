from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def home(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'events/home.html', context)

def account(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'events/index.html', context)

#def #home(request):
    #categorys = Category.objects.all()
    #products = Product.objects.all()
    #context = {'products': products, 'categorys': categorys}
    #return render(request, 'events/home.html', context)