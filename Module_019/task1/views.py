from django.shortcuts import render, HttpResponse
from .forms import UserRegister
from .models import *

def main_page(request):
    title = 'Мой сайт'
    context = {
        'title': title,
    }
    return render(request, 'main_page.html', context)


def shop(request):
    title = 'Магазин'
    games = Game.objects.all()
    context = {
        'title': title,
        'games': games
    }
    return render(request, 'shop.html', context)


def basket(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'basket.html', context)


def sign_up_by_form(request):
    buyers = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for buyer in buyers:
                if username == buyer.name:
                    error = 'Пользователь уже существует'
                    info['error'] = error
                    for key, value in info.items():
                        if value == error:
                            return HttpResponse(f'{key}: {value}')
            if password != repeat_password:
                error = 'Пароли не совпадают'
                info['error'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            elif age < 18:
                error = 'Вы должны быть старше 18'
                info['error'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        return render(request, 'registration_page_form.html', {'form': form})
