from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def pruebas(request):
    return render(request, 'base/pruebas.html')
