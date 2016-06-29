from django.shortcuts import render, redirect, get_object_or_404
from clases.forms import (ContadorPreguntasForm, ClaseForm, ExposicionForm,
                          StartExpoForm, StartQuestionsForm, FinishExpoForm)
from clases.models import Clase, Exposicion, Pregunta, ContadorPreguntas



def clases_home(request):
    clases = Clase.objects.all()
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
        {'clases': clases, 'form': form}
    )


def ver_clase(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    exposiciones = Exposicion.objects.filter(clase = clase)\
                                     .order_by('grupo__numero')
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
        {'clase': clase, 'exposiciones': exposiciones, 'form': form}
    )

def ver_exposicion(request, expo_pk):
    exposicion = get_object_or_404(Exposicion, pk=expo_pk)
    preguntas = ContadorPreguntas.objects.filter(exposicion = exposicion)\
                                         .order_by('preguntador__numero')
    if request.method == "POST":
        if 'pregunta' in request.POST:
            form = ContadorPreguntasForm(exposicion.grupo, request.POST)
            if form.is_valid():
                pregunta = form.save(commit=False)
                pregunta.exposicion = exposicion
                pregunta.save()
                return redirect('clases.views.ver_exposicion', expo_pk=expo_pk)
    else:
        form = ContadorPreguntasForm(exposicion.grupo)

    return render(
        request,
        'clases/ver_exposicion.html',
        {'exposicion': exposicion, 'preguntas': preguntas, 'form': form}
    )


def clases_add(request):
    form = ContadorPreguntasForm()
    return render(request, 'clases/clases_add.html', {'form': form})
