from django.shortcuts import render


def auth(request):
    return render(request, 'auth.html')


def account(request):
    return render(request, 'lk.html')


def registration(request):
    return render(request, 'registration.html')
