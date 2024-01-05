from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    context = {
        'title': 'Home',
        'content': 'Магазин меблів - HOME'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Про нас - HOME',
        'content': 'Про нас - HOME',
        'text_on_page': 'Якийсь текст, який хвалить нас, що ми найкращий у світі магазин меблів'
    }
    return render(request, 'main/about.html', context)
