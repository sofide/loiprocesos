from django import forms

from teoria.models import Unidad


class AgregaUnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ('numero', 'titulo', 'descripcion')
        
