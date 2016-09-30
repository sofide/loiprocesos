from django.shortcuts import render, redirect, get_object_or_404
import datetime

from grupos.models import Grupo, Pertenencia
from grupos.forms import DescripcionGrupoForm, PertenenciaForm
from clases.models import Exposicion, Pregunta
from clases.graphics import tiempo_expo_graphic
from teoria.models import Unidad, Voto, Material
from teoria.models import Pregunta as Pregunta_teoria
from django.contrib.auth.models import User


def grupos_home(request, año=datetime.datetime.now().strftime('%Y')):
    grupos = Grupo.objects.filter(año = año).order_by('numero')

    return render(request, 'grupos/grupos_home.html', {'grupos': grupos, 'año': año })


def ver_grupo(request, grupo_pk):
    grupo = get_object_or_404(Grupo, pk=grupo_pk)
    exposiciones = Exposicion.objects.filter(grupo=grupo).select_related('tp', 'clase')\
                             .order_by('-tp__numero', 'virtual', '-clase')
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

def dashboard(request):
    año=datetime.datetime.now().strftime('%Y')
    heads = ["Grupos", "Exposiciones en clases", "Exposiciones virtuales", "Preguntas votadas", "Preguntas cargadas","Buenas preguntas"]
    grupos = Grupo.objects.filter(año=año)
    exposiciones_clases = [Exposicion.objects.filter(grupo=grupo, virtual=False).count()
                    for grupo in grupos]
    exposiciones_virtual = [Exposicion.objects.filter(grupo=grupo, virtual=True).count()
                    for grupo in grupos]
    preguntas_votadas = [Pregunta.objects.filter(exposicion__grupo=grupo, mejor=True).count()
                     for grupo in grupos]
    preguntas_cargadas = [Pregunta.objects.filter(grupo=grupo).count()
                     for grupo in grupos]
    buenas_preguntas = [Pregunta.objects.filter(grupo=grupo, mejor=True).count()
                     for grupo in grupos]
    tabla = zip(grupos, exposiciones_clases, exposiciones_virtual, preguntas_votadas, preguntas_cargadas, buenas_preguntas)

    unidades = Unidad.objects.all()
    unidades_head = ["Grupos", "Videos sugeridos", "Preguntas sugeridas", "videos votados +", "videos votados -"]

    tabla_unidades = []

    for u in unidades:
        videos_sug = [Material.objects.filter(unidad=u, autor=str(g)).count()
                      for g in grupos]
        preguntas_sug = [Pregunta_teoria.objects.filter(unidad=u, autor=str(g)).count()
                      for g in grupos]
        votos_pos = [Voto.objects.filter(material__unidad=u, grupo=g, voto__gt=0).count()
                      for g in grupos]
        votos_neg = [Voto.objects.filter(material__unidad=u, grupo=g, voto__lt=0).count()
                      for g in grupos]
        tabla_u = zip(grupos, videos_sug, preguntas_sug, votos_pos, votos_neg)
        tabla_unidades.append((u, tabla_u))


    return render(request, 'grupos/dashboard.html', {'heads': heads,
                                                     'tabla': tabla,
                                                     'unidades_head': unidades_head,
                                                     'tabla_unidades': tabla_unidades,
                                                    })


def dashboard_grupo(request, grupo_pk):
    grupo = get_object_or_404(Grupo, pk=grupo_pk)
    exposiciones = Exposicion.objects.filter(grupo=grupo)
    otras_expo = Exposicion.objects.filter(grupo__año=grupo.año).exclude(grupo=grupo)

    # Exposiciones del grupo
    expo_heads = ['Exposición', 'Preguntas registradas', 'Preguntas votadas']
    preguntas = [Pregunta.objects.filter(exposicion=expo).count()
                 for expo in exposiciones]
    votos = [Pregunta.objects.filter(exposicion=expo, mejor=True).count()
             for expo in exposiciones]
    tabla_expo = zip(exposiciones, preguntas, votos)

    # Exposiciones de los demás grupos
    otras_expo_heads = ['Exposición', 'Preguntas que hicimos', 'Buenas preguntas que hicimos']
    preguntas = [Pregunta.objects.filter(exposicion=expo, grupo=grupo).count()
                 for expo in otras_expo]
    votos = [Pregunta.objects.filter(exposicion=expo, grupo=grupo, mejor=True).count()
             for expo in otras_expo]
    tabla_otras_expo = zip(otras_expo, preguntas, votos)

    return render(request, 'grupos/dashboard_grupo.html', {'grupo': grupo,
                                                           'expo_heads': expo_heads,
                                                           'tabla_expo': tabla_expo,
                                                           'otras_expo_heads': otras_expo_heads,
                                                           'tabla_otras_expo': tabla_otras_expo,

                                                          })

