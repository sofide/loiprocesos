from django import forms
from clases.models import ContadorPreguntas, Clase

class ContadorPreguntasForm(forms.ModelForm):

    class Meta:
        model = ContadorPreguntas
        fields = (
            'exposicion', 'preguntador',
            'cantidad', 'primero', 'ultimo'
        )


class ClaseForm(forms.ModelForm):

    class Meta:
        model = Clase
        fields = ('fecha', )
