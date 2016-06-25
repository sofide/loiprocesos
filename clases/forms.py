from django import forms
from clases.models import ContadorPreguntas

class ContadorPreguntasForm(forms.ModelForm):

    class Meta:
        model = ContadorPreguntas
        fields = (
            'clase', 'exposicion', 'preguntador',
            'cantidad', 'primero', 'ultimo'
        )
