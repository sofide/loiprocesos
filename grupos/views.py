from django.shortcuts import render, redirect, get_object_or_404
import datetime

from grupos.models import Grupo, Pertenencia
from grupos.forms import DescripcionGrupoForm, PertenenciaForm


def grupos_home(request, año=datetime.datetime.now().strftime('%Y')):
    grupos = Grupo.objects.filter(año = año).order_by('numero')

    return render(request, 'grupos/grupos_home.html', {'grupos': grupos, 'año': año })


def ver_grupo(request, grupo_pk):
    grupo = get_object_or_404(Grupo, pk=grupo_pk)

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
                                                     'pertenencia_form': form})


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
