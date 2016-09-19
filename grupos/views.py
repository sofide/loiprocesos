from django.shortcuts import render, redirect, get_object_or_404
import datetime

from grupos.models import Grupo, Pertenencia
from grupos.forms import DescripcionGrupoForm, PertenenciaForm
from clases.models import Exposicion, Pregunta
from clases.graphics import tiempo_expo_graphic
from django.contrib.auth.models import User


def grupos_home(request, año=datetime.datetime.now().strftime('%Y')):
    grupos = Grupo.objects.filter(año = año).order_by('numero')

    return render(request, 'grupos/grupos_home.html', {'grupos': grupos, 'año': año })


def ver_grupo(request, grupo_pk):
    grupo = get_object_or_404(Grupo, pk=grupo_pk)
    exposiciones = Exposicion.objects.filter(grupo=grupo).select_related('tp', 'clase')
    ultima_exp = exposiciones[0]
    integrantes = grupo.integrantes.all()
    preguntas = Pregunta.objects.filter(exposicion__in=exposiciones)\
                                .select_related('exposicion', 'grupo')
    preguntas_list = [(preg, preg.exposicion, preg.grupo) for preg in preguntas]
    preg_votadas = [preg for preg in preguntas_list if preg[0].mejor]
    preg_no_votadas = [preg for preg in preguntas_list if not preg[0].mejor]

    expos_chart = [x for x in exposiciones if x.start_expo and x.start_ques and x.finish_expo]

    if expos_chart:
        tiempos_chart = tiempo_expo_graphic(expos_chart)
    else:
        tiempos_chart = None

    if request.method == "POST":
            form = PertenenciaForm(request.POST,)
            if form.is_valid():
                pertenencia = form.save(commit=False)
                pertenencia.grupo = grupo
                pertenencia.save()
                return redirect('grupos.views.ver_grupo', grupo_pk=grupo_pk)
    else:
        form = PertenenciaForm()


    if request.user in [pert.usuario for pert in Pertenencia.objects\
                                                            .filter(grupo=grupo)]:
        pertenece = True
    else:
        pertenece = False

    return render(request, 'grupos/ver_grupo.html', {'grupo': grupo,
                                                     'pertenece': pertenece,
                                                     'exposiciones': exposiciones,
                                                     'pertenencia_form': form,
                                                     'tiempos_chart': tiempos_chart,
                                                     'integrantes': integrantes,
                                                     'preg_votadas': preg_votadas,
                                                     'preg_no_votadas': preg_no_votadas,
                                                     })


def edit_grupo(request, grupo_pk):
    grupo = get_object_or_404(Grupo, pk=grupo_pk)

    if request.user in [pert.usuario for pert in Pertenencia.objects\
                                                            .filter(grupo=grupo)]:
        if request.method == "POST":
                form = DescripcionGrupoForm(request.POST, instance=grupo)
                if form.is_valid():
                    grupo.descripcion = form.cleaned_data["descripcion"]
                    grupo.save()
                    return redirect('grupos.views.ver_grupo', grupo_pk=grupo_pk)
        else:
            form = DescripcionGrupoForm(instance=grupo)
    else:
        return redirect('grupos.views.ver_grupo', grupo_pk=grupo_pk)

    return render(request, 'grupos/ver_grupo.html', {'grupo': grupo,
                                                     'editar_form': form})
