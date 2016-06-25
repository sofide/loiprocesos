from django.shortcuts import render, redirect, get_object_or_404
from clases.forms import ContadorPreguntasForm, ClaseForm
from clases.models import Clase, Exposicion


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
    exposiciones = Exposicion.objects.filter(clase__id = pk).order_by('grupo__numero')

    return render(
        request,
        'clases/ver_clase.html',
        {'clase': clase, 'exposiciones': exposiciones}
    )


def clases_add(request):
    form = ContadorPreguntasForm()
    return render(request, 'clases/clases_add.html', {'form': form})
