from django.shortcuts import render

def home(request):
    return render(request, 'clases/clases_principal.html', {})
