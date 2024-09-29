from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'platform.html')


def games_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'games': games}
    return render(request, 'games.html', context=context)


def cart_page(request):
    return render(request, 'cart.html')