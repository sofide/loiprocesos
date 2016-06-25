from django.shortcuts import render
from clases.forms import ContadorPreguntasForm

def clases_home(request):
    return render(request, 'clases/clases_home.html', {})

def clases_add(request):
    form = ContadorPreguntasForm()
    return render(request, 'clases/clases_add.html', {'form': form})
