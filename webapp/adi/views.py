from django.shortcuts import render


def login(request):
    return render(request, 'adi/login.html')


def second(request):
    return render(request, 'adi/second.html')
