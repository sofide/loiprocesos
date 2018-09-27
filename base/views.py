from django.shortcuts import render

from clases.models import Clase, Exposicion, ContadorPreguntas
from clases.graphics import tiempo_expo_graphic, q_pregs_expos_graphic

from teoria.models import Unidad


def home_original(request):
    def clase_data(exclude=None):
        '''
        Return data information about the first clase (except given id parameter)
        '''
        clase = Clase.objects.exclude(pk=exclude).first()
        tiempos = None
        preguntas = None
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

        return clase, tiempos, preguntas

    # Datos de la última clase
    clase, tiempos, preguntas = clase_data()
    # Datos de la anteúltima clase
    clase_ant, tiempos_ant, preguntas_ant = clase_data(clase.pk)

    unidades = Unidad.objects.all()

    return render(request, 'base/home_original.html', {'clase': clase,
                                              'tiempos': tiempos,
                                              'preguntas': preguntas,
                                              'clase_ant': clase_ant,
                                              'tiempos_ant': tiempos_ant,
                                              'preguntas_ant': preguntas_ant,
                                              'unidades': unidades,
                                             })


def home_dos(request):
    return render(request, 'base/home.html')


def home_tres(request):
    def clase_data(exclude=None):
        '''
        Return data information about the first clase (except given id parameter)
        '''
        clase = Clase.objects.exclude(pk=exclude).first()
        tiempos = None
        preguntas = None
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

        return clase, tiempos, preguntas

    # Datos de la última clase
    clase, tiempos, preguntas = clase_data()
    # Datos de la anteúltima clase
    clase_ant, tiempos_ant, preguntas_ant = clase_data(clase.pk)

    unidades = Unidad.objects.all()

    return render(request, 'base/home_tres.html', {'clase': clase,
                                                   'tiempos': tiempos,
                                                   'preguntas': preguntas,
                                                   'clase_ant': clase_ant,
                                                   'tiempos_ant': tiempos_ant,
                                                   'preguntas_ant': preguntas_ant,
                                                   'unidades': unidades,
                                                  })


def pruebas(request):
    return render(request, 'base/pruebas.html')
