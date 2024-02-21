from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.utils import q_search
from goods.models import Products
from django.db.models import Q


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    elif query == "":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if order_by != "default" and order_by != None:
        if category_slug == "all":
            goods = Products.objects.all().order_by(order_by)
        else:
            goods = Products.objects.filter(category__slug=category_slug).order_by(order_by)

    if on_sale:
        if category_slug == "all":
            goods = Products.objects.filter(discount__gt=0)
            if order_by != "default" and order_by != None:
                goods = goods.order_by(order_by)
        else:
            goods = Products.objects.filter(category__slug=category_slug)
            goods = goods.filter(discount__gt=0)
            if order_by != "default" and order_by != None:
                goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))

    context = {
        'title': 'SMART - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)
