from django.shortcuts import render, redirect, get_object_or_404

from teoria.models import Unidad, Pregunta, Material
from teoria.forms import EditUdForm

def teoria_home(request):
    unidades = Unidad.objects.all()

    return render(request, 'teoria/teoria_home.html', {'unidades': unidades})


def ver_unidad(request, unidad_pk):
    unidad = get_object_or_404(Unidad, pk=unidad_pk)

    preguntas = Pregunta.objects.filter(unidad=unidad)

    material = Material.objects.filter(unidad=unidad)

    return render(request, 'teoria/ver_unidad.html', {'unidad': unidad,
                                                      'preguntas': preguntas,
                                                      'material': material})

def edit_ud(request, ud_pk=None):
    if ud_pk:
        ud = get_object_or_404(Unidad, pk=ud_pk)
    else:
        ud = None

    if request.method == "POST":
            form = EditUdForm(request.POST, instance=ud)
            if form.is_valid():
                unidad = form.save(commit=False)
                unidad.save()
                return redirect('teoria.views.teoria_home')
    else:
        form = EditUdForm(instance=ud)

    return render(request, 'teoria/edit_ud.html', {'unidad_form': form})
