from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister



# Create your views here.


def sign_up_by_html(request):
    users = ['Alex', 'Tom', 'Jerry', 'Mike', 'Jim']
    info = {}
    context = {
        'info': info,
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f"Приветствуем, {username}!")
        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
        if int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18 лет'})
        if username in users:
            info.update({'error': 'Пользователь уже существует'})

    return render(request, 'fifth_task/registration_page.html', context)




def sign_up_by_django(request):
    users = ['Alex', 'Tom', 'Jerry', 'Mike', 'Jim']
    info = {}
    form = UserRegister()
    context = {
        'info': info,
        'form': form,
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info.update({'error1': 'Пароли не совпадают'})
            if int(age) < 18:
                info.update({'error2': 'Вы должны быть старше 18 лет'})
            if username in users:
                info.update({'error3': 'Пользователь уже существует'})
        else:
            form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context)
