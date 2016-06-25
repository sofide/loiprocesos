from django.shortcuts import render, redirect
from clases.forms import ContadorPreguntasForm, ClaseForm
from clases.models import Clase


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


def clases_add(request):
    form = ContadorPreguntasForm()
    return render(request, 'clases/clases_add.html', {'form': form})
