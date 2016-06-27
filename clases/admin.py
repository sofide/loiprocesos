from django.contrib import admin
from clases.models import (
    Clase,
    TP,
    Exposicion,
    Pregunta,
    ContadorPreguntas,
)

admin.site.register(Clase)
admin.site.register(TP)
admin.site.register(Exposicion)
admin.site.register(Pregunta)
admin.site.register(ContadorPreguntas)
