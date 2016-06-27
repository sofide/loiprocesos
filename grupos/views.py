from django.shortcuts import render, redirect, get_object_or_404
import datetime
from grupos.models import Grupo

def grupos_home(request, año=datetime.datetime.now().strftime('%Y')):
    grupos = Grupo.objects.filter(año = año).order_by('numero')

    return render(request, 'grupos/grupos_home.html', {'grupos': grupos, 'año': año })


def ver_grupo(request, grupo_pk):
    grupo = get_object_or_404(Grupo, pk=grupo_pk)

    return render(request, 'grupos/ver_grupo.html', {'grupo': grupo,})
