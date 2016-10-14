from django import forms
from django.conf import settings

from grupos.models import Grupo, Pertenencia, Evaluacion


class DescripcionGrupoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DescripcionGrupoForm, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.HiddenInput()

    class Meta:
        model = Grupo
        fields = ('descripcion',)


class PertenenciaForm(forms.ModelForm):
    class Meta:
        model = Pertenencia
        fields = ('usuario',)


class AutoevaluacionForm(forms.ModelForm):
    def __init__(self, grupo=None, criterio=None, *args, **kwargs):
        super(AutoevaluacionForm, self).__init__(*args, **kwargs)
        self.fields['criterio'].widget = forms.HiddenInput()
        self.fields['grupo_evaluado'].widget = forms.HiddenInput()
        if criterio and grupo:
            self.fields['puntuacion'].label = "{} - {}".format(grupo, criterio)

    class Meta:
        model = Evaluacion
        fields = ('criterio', 'grupo_evaluado', 'puntuacion')
