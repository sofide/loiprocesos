from django import forms
from django.conf import settings

from grupos.models import Grupo, Pertenencia

class DescripcionGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ('descripcion',)

class PertenenciaForm(forms.ModelForm):
    class Meta:
        model = Pertenencia
        fields = ('usuario',)
