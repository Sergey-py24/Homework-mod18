from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=30)
    password = forms.CharField(label='Введите пароль', min_length=8)
    repeat_password = forms.CharField(label='Повторите пароль', min_length=8, )
    age = forms.IntegerField(label='Введите возраст', min_value=1, max_value=100)