from django.shortcuts import render, redirect, get_object_or_404

from teoria.models import Unidad, Pregunta, Material
from teoria.forms import EditUdForm, MaterialForm

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
        warn = "Estás editando la unidad {}".format(ud)

    else:
        ud = None
        warn = "Estás agregando una nueva unidad"

    if request.method == "POST":
            form = EditUdForm(request.POST, instance=ud)
            if form.is_valid():
                unidad = form.save(commit=False)
                unidad.save()
                return redirect('teoria.views.teoria_home')
    else:
        form = EditUdForm(instance=ud)

    return render(request, 'teoria/edit_ud.html', {'unidad_form': form,
                                                   'warn': warn,
                                                   }, )


def add_material(request):
    if request.user.grupos.all().exists():
        grupo = request.user.grupos.first()
    else:
        grupo = " "

    if request.method == "POST":
        form = MaterialForm(request.POST, initial={'autor':str(grupo), })
        if form.is_valid():
            material = form.save(commit=False)
            material.save()
            ud = material.unidad_id
            if "save" in request.POST:
                return redirect('teoria.views.ver_unidad', ud)
            if "add" in request.POST:
                form = MaterialForm(initial={'autor':str(grupo), 'unidad': ud})

    else:
        form = MaterialForm(initial={'autor':str(grupo), })

    return render(request, 'teoria/add_material.html', {'material_form': form})
