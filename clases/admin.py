from django.contrib import admin
from clases.models import (
    Clase,
    Grupo,
    Integrante,
    TP,
    Exposicion,
    Pregunta,
)

admin.site.register(Clase)
admin.site.register(Grupo)
admin.site.register(Integrante)
admin.site.register(TP)
admin.site.register(Exposicion)
admin.site.register(Pregunta)
