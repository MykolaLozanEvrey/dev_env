from django.shortcuts import render
from django.http import HttpResponse


from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        'title': 'HOME - каталог товарів',
        'goods': goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
