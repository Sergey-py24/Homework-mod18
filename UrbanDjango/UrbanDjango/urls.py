"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import index, Index2
# from task3.views import welcome, platform, spec, cart, games
from task4.views import welcome, platform, spec, cart, games
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fnct/', index),
    path('clst/', Index2.as_view()),
    path('', welcome),
    path('platform/', platform),
    path('platform/spec/', spec),
    path('platform/cart/', cart),
    path('platform/games/', games),
    path('reghtml/', sign_up_by_html),
    path('regdjango/', sign_up_by_django),

]
