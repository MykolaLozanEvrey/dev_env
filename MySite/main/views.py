from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):


    context = {
        'title': 'SMART',
        'content': 'Магазин гаджетів - SMART',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Про SMART',
        'content': 'Про нас - SMART',
        'text_on_page': 'Якийсь текст, який хвалить нас, що ми найкращий у світі магазин гаджетів'
    }
    
    return render(request, 'main/about.html', context)
