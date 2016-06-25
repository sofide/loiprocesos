from django.shortcuts import render

def clases_home(request):
    return render(request, 'clases/clases_home.html', {})

def clases_add(request):
    return render(request, 'clases/clases_add.html', {})
