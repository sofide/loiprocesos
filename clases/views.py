from django.shortcuts import render

def clases_principal(request):
    return render(request, 'clases/clases_principal.html', {})
