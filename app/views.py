import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = str(datetime.now())
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    list = os.listdir(path=os.getcwd())

    if len(list) == 0:
        msg = f'Нет вложенных директорий'
    else:
        msg = ', '.join(list)
        print(str(msg))

    return HttpResponse(msg)
