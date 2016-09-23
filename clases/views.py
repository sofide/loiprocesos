import itertools
import re

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone

from clases.forms import (ContadorPreguntasForm, ClaseForm, ExposicionForm,
                          StartExpoForm, StartQuestionsForm, FinishExpoForm,
                          AddPreguntasForm, EditTPForm, ExposicionVirtualForm)
from clases.models import (Clase, Exposicion, Pregunta, ContadorPreguntas, TP,
                           Pregunta)
from clases.graphics import tiempo_expo_graphic, q_pregs_graphic, q_pregs_expos_graphic
from grupos.models import Pertenencia
from base.models import Text
from base.forms import EditTextForm


def clases_home(request):
    clases = Clase.objects.all().order_by('-fecha')
    texts = Text.objects.filter(reference="clases")
    if request.method == "POST":
            form = ClaseForm(request.POST)
            if form.is_valid():
                clase = form.save()
                clase.save()
                return redirect('clases.views.clases_home')
    else:
        form = ClaseForm()

    return render(
        request,
        'clases/clases_home.html',
        {'clases': clases, 'form': form, 'texts': texts}
    )


def ver_clase(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    exposiciones = Exposicion.objects.filter(clase=clase)\
                                     .order_by('grupo__numero')\
                                     .select_related('grupo')

    tiempos = None
    tiempos_chart = [expo for expo in exposiciones
                     if expo.start_expo and expo.start_ques and expo.finish_expo]

    if tiempos_chart:
        tiempos = tiempo_expo_graphic(tiempos_chart)

    preguntas = None
    preg_chart = [expo for expo in exposiciones
                  if ContadorPreguntas.objects.filter(exposicion=expo).exists()]

    if preg_chart:
        preguntas = q_pregs_expos_graphic(preg_chart)

    if request.method == "POST":
            form = ExposicionForm(request.POST)
            if form.is_valid():
                exposicion = form.save(commit=False)
                exposicion.clase = clase
                exposicion.save()
                return redirect('clases.views.ver_clase', pk=pk)
    else:
        form = ExposicionForm()

    return render(
        request,
        'clases/ver_clase.html',
        {'clase': clase,
         'exposiciones': exposiciones,
         'form': form,
         'tiempos': tiempos,
         'preguntas': preguntas,
         }
    )


def ver_exposicion(request, expo_pk):
    exposicion = get_object_or_404(Exposicion, pk=expo_pk)
    q_preguntas = ContadorPreguntas.objects.filter(exposicion=exposicion)\
                                           .order_by('preguntador__numero')\
                                           .select_related('preguntador')

    preguntas = exposicion.preguntas.select_related('grupo').all()
    preguntas_agrupadas = [(grupo, list(preguntas_grupo))
                            for grupo, preguntas_grupo
                            in itertools.groupby(preguntas, lambda p: p.grupo)]

    tiempos_graph = None
    preguntas_graph = None

    if exposicion.start_expo and exposicion.start_ques and exposicion.finish_expo:
        tiempos_graph = tiempo_expo_graphic([exposicion])

    if ContadorPreguntas.objects.filter(exposicion=exposicion):
        preguntas_graph = q_pregs_graphic(exposicion)

    if request.method == "POST":

        if 'pregunta' in request.POST:
            cont_preg_form = ContadorPreguntasForm(exposicion.grupo,
                                                   request.POST)
            if cont_preg_form.is_valid():
                pregunta = cont_preg_form.save(commit=False)
                pregunta.exposicion = exposicion
                pregunta.save()

        elif 'st_ex' in request.POST:
            st_expo_form = StartExpoForm(request.POST)
            if st_expo_form.is_valid():
                exposicion.start_expo = st_expo_form.cleaned_data["start_expo"]
                exposicion.save()

        elif 'st_qu' in request.POST:
            st_ques_form = StartQuestionsForm(request.POST)
            if st_ques_form.is_valid():
                exposicion.start_ques = st_ques_form.cleaned_data["start_ques"]
                exposicion.save()

        elif 'fi_ex' in request.POST:
            fi_expo_form = FinishExpoForm(request.POST)
            if fi_expo_form.is_valid():
                exposicion.finish_expo = fi_expo_form.cleaned_data["finish_expo"]
                exposicion.save()

    cont_preg_form = ContadorPreguntasForm(exposicion.grupo)
    st_expo_form = StartExpoForm()
    st_ques_form = StartQuestionsForm()
    fi_expo_form = FinishExpoForm()

    if exposicion.virtual:
        video_id = re.findall(r'v=[\d|\w]+&?', exposicion.video)[0].replace('v=', '').replace('&', '')
    else:
        video_id = None

    if request.user in [pert.usuario for pert in Pertenencia.objects\
                                                            .filter(grupo=exposicion.grupo)]:
        pertenece = True
    else:
        pertenece = False

    return render(
        request,
        'clases/ver_exposicion.html',
        {'exposicion': exposicion, 'q_preguntas': q_preguntas,
         'cont_preg_form': cont_preg_form, 'st_expo_form': st_expo_form,
         'st_ques_form': st_ques_form, 'fi_expo_form': fi_expo_form,
         'preguntas_graph': preguntas_graph, 'tiempos_graph': tiempos_graph,
         'preguntas_agrupadas': preguntas_agrupadas,
         'video_id': video_id, 'pertenece': pertenece,
         }
    )


def preguntas(request):
    if request.user.is_authenticated():
        if request.user.grupos.exists():
            grupo = request.user.grupos.order_by('-año').first()
        else:
            grupo = None
        user = request.user
    else:
        user = None
        grupo = None

    if grupo:
        warn = "Estás registrado en el grupo {}. Las preguntas que cargues se registrarán a nombre de ese grupo.".format(grupo)
    else:
        warn = "No estás registrado en ningún grupo."


    if request.method == "POST":
        form = AddPreguntasForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            if grupo:
                pregunta.grupo = grupo
            if user:
                pregunta.usuario = user
            pregunta.save()
            if "add" in request.POST:
                initial = pregunta.exposicion.id
            else:
                initial = None
            form = AddPreguntasForm(initial={'exposicion':initial})
    else:
        form = AddPreguntasForm()

    return render(
        request,
        'clases/preguntas.html',
        {'preguntas_form':form,
         'warn': warn,
         }
    )

def trabajos_practicos(request):
    trabajos = TP.objects.all()
    return render(
        request,
        'clases/trabajos_practicos.html',
        {'trabajos':trabajos,}
        )

def edit_tp(request, tp_pk=None):
    if tp_pk:
        tp = get_object_or_404(TP, pk=tp_pk)
    else:
        tp = None

    if request.method == "POST":
            form = EditTPForm(request.POST, instance=tp)
            if form.is_valid():
                new_tp = form.save(commit=False)
                new_tp.save()
                return redirect('trabajos_practicos')
    else:
        form = EditTPForm(instance=tp)

    return render(
        request,
        'clases/editar_tp.html',
        {'form': form}
    )


def ver_tp(request, tp_pk):
    tp = get_object_or_404(TP, pk=tp_pk)
    exposiciones = Exposicion.objects.filter(tp=tp_pk)
    preg_grupo = [Pregunta.objects.filter(exposicion__in=exposiciones,
                                          exposicion__grupo=grupo)
                  for grupo in set(expo.grupo
                                   for expo in exposiciones)]

    return render(
        request,
        'clases/ver_tp.html',
        {'tp': tp,
         'exposiciones': exposiciones,
         'preguntas': preg_grupo,
        }
    )



def edit_text(request, text_pk=None):
    if text_pk:
        text = get_object_or_404(Text, pk=text_pk)
    else:
        text = None

    if request.method == "POST":
            form = EditTextForm(request.POST, instance=text)
            if form.is_valid():
                new_text = form.save(commit=False)
                new_text.reference = "clases"
                new_text.edited = timezone.now()
                new_text.save()
                return redirect('clases_home')
    else:
        form = EditTextForm(instance=text)

    return render(
        request,
        'base/edit_text.html',
        {'form': form, 'reference': "Clases"}
    )


def votar_preg(request, preg_pk, voto):
    pregunta = get_object_or_404(Pregunta, pk=preg_pk)
    if request.user.is_authenticated() and request.user.grupos.exists():
        grupo = request.user.grupos.first()
    else:
        return redirect('ver_grupo', pregunta.exposicion.grupo.pk)

    if grupo == pregunta.exposicion.grupo:
        if pregunta.mejor and voto == '-':
            pregunta.mejor = False
            pregunta.save()
        elif not pregunta.mejor and voto == '+':
            pregunta.mejor = True
            pregunta.save()

    return redirect('ver_grupo', grupo.pk)


def virtual_expo(request):
    if request.user.is_authenticated() and request.user.grupos.exists():
        grupo = request.user.grupos.first()
    else:
        return redirect('home')

    if request.method == "POST":
            form = ExposicionVirtualForm(request.POST)
            if form.is_valid():
                expo = form.save(commit=False)
                expo.grupo = grupo
                expo.start_expo = timezone.now()
                expo.virtual = True
                expo.save()
                return redirect('ver_grupo', grupo.pk)
    else:
        form = ExposicionVirtualForm()

    return render(
        request,
        'clases/expo_virtual.html',
        {'form': form, 'grupo': grupo}

    )

