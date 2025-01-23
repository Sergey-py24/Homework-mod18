from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'fourth_task/welcome.html')

def platform(request):
    return render(request, 'fourth_task/platform.html')

games_list = ['Serious Sam', 'Counter Strike: Global Offensive', 'Call of Duty: Modern Warfare', 'Caliber']

def games(request):
    context = {
        'games': games_list
    }
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')

def spec(request):
    return render(request, 'fourth_task/specification.html')