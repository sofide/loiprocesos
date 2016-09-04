from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from teoria.models import Unidad, Pregunta, Material, Voto
from teoria.forms import EditUdForm, MaterialForm, PreguntaTeoriaForm

from base.models import Text
from base.forms import EditTextForm


def teoria_home(request):
    unidades = Unidad.objects.all()
    texts = Text.objects.filter(reference = "teoria")

    return render(request, 'teoria/teoria_home.html', {'unidades': unidades,
                                                       'texts': texts,
                                                      })


def ver_unidad(request, unidad_pk):
    unidad = get_object_or_404(Unidad, pk=unidad_pk)
    texts = Text.objects.filter(reference = "teoria")

    preguntas = Pregunta.objects.filter(unidad=unidad, vigente=True)
    if request.user.is_authenticated():
        if request.user.grupos.all().exists():
            material = [(m,
                        sum(v.voto for v in Voto.objects.filter(material=m)),
                        Voto.objects.filter(material=m, grupo=request.user.grupos.first()).first())
                            for m in Material.objects.filter(unidad=unidad, vigente=True)]
        else:
            material = [(m,
                        sum(v.voto for v in Voto.objects.filter(material=m)),
                        Voto.objects.filter(material=m, usuario=request.user).first())
                            for m in Material.objects.filter(unidad=unidad, vigente=True)]
    else:
        material = [(m,
                    sum(v.voto for v in Voto.objects.filter(material=m)),
                    False)
                        for m in Material.objects.filter(unidad=unidad, vigente=True)]


    material_extra = Material.objects.filter(unidad=unidad, vigente=False)
    preguntas_extra = Pregunta.objects.filter(unidad=unidad, vigente=False)

    if request.user.groups.filter(name="staff procesos").exists():
        staff = True
    else:
        staff = False

    return render(request, 'teoria/ver_unidad.html', {'unidad': unidad,
                                                      'preguntas': preguntas,
                                                      'material': material,
                                                      'preguntas_extra': preguntas_extra,
                                                      'material_extra': material_extra,
                                                      'staff': staff,
                                                      'texts': texts,
                                                      })

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


def add_recurso(request, recurso):
    if recurso == "m":
        form_class = MaterialForm
        is_material = True
    else:
        form_class = PreguntaTeoriaForm
        is_material = False

    if request.user.is_authenticated() and request.user.grupos.all().exists():
        grupo = request.user.grupos.first()
    else:
        grupo = " "

    if request.method == "POST":
        form = form_class(request.POST, initial={'autor':str(grupo), })
        if form.is_valid():

            if request.user.is_authenticated():
                user = request.user
            else:
                user = None

            recurso = form.save(commit=False)
            recurso.fecha = timezone.now()
            recurso.usuario = user

            if request.user.groups.filter(name="staff procesos").exists():
                recurso.vigente = True
            else:
                recurso.vigente = False
            recurso.save()
            ud = recurso.unidad_id
            if "save" in request.POST:
                return redirect('teoria.views.ver_unidad', ud)
            if "add" in request.POST:
                form = form_class(initial={'autor':str(grupo), 'unidad': ud})

    else:
        form = form_class(initial={'autor':str(grupo), })

    return render(request, 'teoria/add_recurso.html', {'material_form': form,
                                                        'is_material': is_material,
                                                        })


def del_recurso(request, recurso, pk):
    if recurso == 'm':
        material = get_object_or_404(Material, pk=pk)
        material.vigente = False
        material.save()
        ud = material.unidad_id
    else:
        pregunta = get_object_or_404(Pregunta, pk=pk)
        pregunta.vigente = False
        pregunta.save()
        ud = pregunta.unidad_id
    return redirect('teoria.views.ver_unidad', ud)


def edit_text(request, text_pk=None):
    if text_pk:
        text = get_object_or_404(Text, pk=text_pk)
    else:
        text = None

    if request.method == "POST":
            form = EditTextForm(request.POST, instance=text)
            if form.is_valid():
                new_text = form.save(commit=False)
                new_text.reference = "teoria"
                new_text.edited = timezone.now()
                new_text.save()
                return redirect('teoria_home')
    else:
        form = EditTextForm(instance=text)

    return render(
        request,
        'base/edit_text.html',
        {'form': form, 'reference': 'Teoría',}
    )


@login_required
def voto_recurso(request, voto, recurso, rec_pk):
    if recurso == "m":
        recurso = get_object_or_404(Material, pk=rec_pk)
        material = True
    else:
        recurso = get_object_or_404(Pregunta, pk=rec_pk)
        material = False

    if request.user.grupos.all().exists():
        grupo = request.user.grupos.first()
    else:
        grupo = None

    if material:
        if grupo:
            if Voto.objects.filter(grupo=grupo, material=recurso).exists():
                return HttpResponseRedirect(reverse('ver_unidad', args=[recurso.unidad.pk]))
        else:
            if Voto.objects.filter(usuario=request.user, material=recurso).exists():
                return HttpResponseRedirect(reverse('ver_unidad', args=[recurso.unidad.pk]))

        if voto == "+":
            valor = 1
        else:
            valor = -1

        voto = Voto(grupo=grupo,
                    usuario=request.user,
                    material=recurso,
                    voto=valor)
        voto.save()
    else:
        if grupo:
            if Voto.objects.filter(grupo=grupo, pregunta=recurso).exists():
                return HttpResponseRedirect(reverse('ver_unidad', args=[recurso.unidad.pk]))
        else:
            if Voto.objects.filter(usuario=request.user, pregunta=recurso).exists():
                return HttpResponseRedirect(reverse('ver_unidad', args=[recurso.unidad.pk]))

        if voto == "+":
            valor = 1
        else:
            valor = -1
        voto = Voto(grupo=grupo,
                    usuario=request.user,
                    pregunta=recurso,
                    voto=valor)
        voto.save()

    return HttpResponseRedirect(reverse('ver_unidad', args=[recurso.unidad.pk]))
