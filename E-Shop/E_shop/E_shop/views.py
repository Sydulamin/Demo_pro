from django.shortcuts import render, redirect
from store_app.models import Product, Categories, Filter_Price, Color


def BASE(request):
    return render(request,'Main/base.html')


def HOME(request):
    product = Product.objects.filter(status='Publish')

    context = {
        'product':product,

    }
    return render(request,'Main/index.html',context)


def PRODUCT(request):
    product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()

    CATID = request.GET.get('categories')
    # print(CATID)
    if CATID:
        product = Product.objects.filter(categories=CATID)
    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,

    }
    return render(request,'Main/product.html',context)