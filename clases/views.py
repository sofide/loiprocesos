from django.shortcuts import render

def clases_home(request):
    return render(request, 'clases/clases_home.html', {})
