from django.contrib import admin
from grupos.models import Grupo, Pertenencia, Autoevaluacion_grupal, Evaluacion, Criterio_evaluacion

admin.site.register(Grupo)
admin.site.register(Pertenencia)
admin.site.register(Autoevaluacion_grupal)
admin.site.register(Evaluacion)
admin.site.register(Criterio_evaluacion)
