from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('second', views.second, name='second'),
    path('', views.login, name='login'),
]
