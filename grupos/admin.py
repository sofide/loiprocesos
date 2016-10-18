from django.contrib import admin
from grupos.models import Grupo, Pertenencia, Autoevaluacion_grupal, Evaluacion, Criterio_evaluacion


class AdminEvaluacion(admin.ModelAdmin):
    list_display = ('evaluador', 'grupo_evaluado', 'criterio', 'puntuacion')


admin.site.register(Grupo)
admin.site.register(Pertenencia)
admin.site.register(Autoevaluacion_grupal)
admin.site.register(Evaluacion, AdminEvaluacion)
admin.site.register(Criterio_evaluacion)
