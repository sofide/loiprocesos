from django import forms
from django.conf import settings

from grupos.models import Grupo, Pertenencia

class DescripcionGrupoForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(DescripcionGrupoForm, self).__init__(*args,**kwargs)
        self.fields['descripcion'].widget = forms.HiddenInput()

    class Meta:
        model = Grupo
        fields = ('descripcion',)

class PertenenciaForm(forms.ModelForm):
    class Meta:
        model = Pertenencia
        fields = ('usuario',)
