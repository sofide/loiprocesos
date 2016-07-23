from django.shortcuts import render

from clases.models import Clase, Exposicion
from clases.graphics import tiempo_expo_graphic

from teoria.models import Unidad



def home(request):
    clase = Clase.objects.first()
    tiempos = None
    exposiciones = Exposicion.objects.filter(clase=clase)\
                                     .order_by('grupo__numero')\
                                     .select_related('grupo')
    expo_chart = [expo for expo in exposiciones
                       if expo.start_expo and expo.start_ques and expo.finish_expo]

    if expo_chart:
        tiempos = tiempo_expo_graphic(expo_chart)


    unidades = Unidad.objects.all()

    return render(request, 'base/home.html', {'clase': clase,
                                              'tiempos': tiempos,
                                              'unidades': unidades,
                                             })


def pruebas(request):
    return render(request, 'base/pruebas.html')
