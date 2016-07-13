from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from clases.forms import (ContadorPreguntasForm, ClaseForm, ExposicionForm,
                          StartExpoForm, StartQuestionsForm, FinishExpoForm,
                          AddPreguntasForm, EditTPForm)
from clases.models import Clase, Exposicion, Pregunta, ContadorPreguntas, TP

from clases.graphics import tiempo_expo_graphic, q_pregs_graphic, graphic

from grupos.models import Pertenencia


def clases_home(request):
    clases = Clase.objects.all().order_by('-fecha')
    if request.method == "POST":
            form = ClaseForm(request.POST)
            if form.is_valid():
                clase = form.save()
                clase.save()
                return redirect('clases.views.clases_home')
    else:
        form = ClaseForm()

    script, div = graphic()

    return render(
        request,
        'clases/clases_home.html',
        {'clases': clases, 'form': form, 'script':script, 'div':div}
    )


def ver_clase(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    exposiciones = Exposicion.objects.filter(clase=clase)\
                                     .order_by('grupo__numero')\
                                     .select_related('grupo')

    tiempos_chart = None
    expo_chart = [expo for expo in exposiciones
                       if expo.start_expo and expo.start_ques and expo.finish_expo]

    if expo_chart:
        tiempos_chart = tiempo_expo_graphic(expo_chart)

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
        {'clase': clase, 'exposiciones': exposiciones, 'form': form,
         'tiempos_chart': tiempos_chart,
         }
    )

def ver_exposicion(request, expo_pk):
    exposicion = get_object_or_404(Exposicion, pk=expo_pk)
    preguntas = ContadorPreguntas.objects.filter(exposicion = exposicion)\
                                         .order_by('preguntador__numero')\
                                         .select_related('preguntador')

    tiempos_graph = None
    preguntas_graph = None

    if exposicion.start_expo and exposicion.start_ques and exposicion.finish_expo:
        tiempos_graph = tiempo_expo_graphic([exposicion])

    if ContadorPreguntas.objects.filter(exposicion=exposicion):
        preguntas_graph = q_pregs_graphic(exposicion)

    cont_preg_form = ContadorPreguntasForm(exposicion.grupo)
    st_expo_form = StartExpoForm()
    st_ques_form = StartQuestionsForm()
    fi_expo_form = FinishExpoForm()

    if request.method == "POST":

        if 'pregunta' in request.POST:
            cont_preg_form = ContadorPreguntasForm(exposicion.grupo,
                                                   request.POST)
            if cont_preg_form.is_valid():
                pregunta = cont_preg_form.save(commit=False)
                pregunta.exposicion = exposicion
                pregunta.save()
                return redirect('clases.views.ver_exposicion', expo_pk=expo_pk)

        elif 'st_ex' in request.POST:
            st_expo_form = StartExpoForm(request.POST)
            if st_expo_form.is_valid():
                exposicion.start_expo = st_expo_form.cleaned_data["start_expo"]
                exposicion.save()
                return redirect('clases.views.ver_exposicion', expo_pk=expo_pk)

        elif 'st_qu' in request.POST:
            st_ques_form = StartQuestionsForm(request.POST)
            if st_ques_form.is_valid():
                exposicion.start_ques = st_ques_form.cleaned_data["start_ques"]
                exposicion.save()
                return redirect('clases.views.ver_exposicion', expo_pk=expo_pk)

        elif 'fi_ex' in request.POST:
            fi_expo_form = FinishExpoForm(request.POST)
            if fi_expo_form.is_valid():
                exposicion.finish_expo = fi_expo_form.cleaned_data["finish_expo"]
                exposicion.save()
                return redirect('clases.views.ver_exposicion', expo_pk=expo_pk)

    side_bar = [
        ["Ver más expos del {}".format(exposicion.clase),
            reverse('ver_clase', args=[exposicion.clase.id])],
    ]

    return render(
        request,
        'clases/ver_exposicion.html',
        {'exposicion': exposicion, 'preguntas': preguntas,
         'cont_preg_form': cont_preg_form, 'st_expo_form': st_expo_form,
         'st_ques_form': st_ques_form, 'fi_expo_form': fi_expo_form,
         'preguntas_graph': preguntas_graph, 'tiempos_graph': tiempos_graph,
         'side_bar': side_bar,
         }
    )

def preguntas(request):
    grupo = request.user.grupos.order_by('-año').first()

    if grupo:
        warn = "Estás registrado en el grupo {}. Las preguntas que cargues se registrarán a nombre de ese grupo.".format(grupo)
    else:
        warn = "No estás registrado en ningún grupo. Se cargará la pregunta anónimamente"


    if request.method == "POST":
        form = AddPreguntasForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            if grupo:
                pregunta.grupo = grupo
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
