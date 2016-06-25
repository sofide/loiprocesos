from django import forms
from clases.models import ContadorPreguntas, Clase, Exposicion

class ContadorPreguntasForm(forms.ModelForm):

    class Meta:
        model = ContadorPreguntas
        fields = (
            'preguntador',
            'cantidad', 'primero', 'ultimo'
        )


class ClaseForm(forms.ModelForm):

    class Meta:
        model = Clase
        fields = ('fecha', )


class ExposicionForm(forms.ModelForm):

    class Meta:
        model = Exposicion
        fields = ('grupo', 'tp')
