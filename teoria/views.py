from django.shortcuts import render

from teoria.models import Unidad

def teoria_home(request):
    unidades = Unidad.objects.all()

    return render(request, 'teoria/teoria_home.html', {'unidades': unidades})
