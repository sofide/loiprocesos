from django.shortcuts import render

from clases.models import Clase, Exposicion, ContadorPreguntas
from clases.graphics import tiempo_expo_graphic, q_pregs_expos_graphic

from teoria.models import Unidad



def home(request):
    clase = Clase.objects.first()
    tiempos = None
    exposiciones = Exposicion.objects.filter(clase=clase)\
                                     .order_by('grupo__numero')\
                                     .select_related('grupo')
    expo_chart = [expo for expo in exposiciones
                       if expo.start_expo and expo.start_ques and expo.finish_expo]

    preg_chart = [expo for expo in exposiciones
                       if ContadorPreguntas.objects.filter(exposicion=expo).exists()]

    if expo_chart:
        tiempos = tiempo_expo_graphic(expo_chart)

    if preg_chart:
        preguntas = q_pregs_expos_graphic(preg_chart)

    unidades = Unidad.objects.all()

    return render(request, 'base/home.html', {'clase': clase,
                                              'tiempos': tiempos,
                                              'unidades': unidades,
                                              'preguntas': preguntas,
                                             })


def pruebas(request):
    return render(request, 'base/pruebas.html')
