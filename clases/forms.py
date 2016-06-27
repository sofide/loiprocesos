from django import forms
from clases.models import ContadorPreguntas, Clase, Exposicion
from grupos.models import Grupo

class ContadorPreguntasForm(forms.ModelForm):
    def __init__(self,grupo,*args,**kwargs):
        super(ContadorPreguntasForm, self).__init__(*args,**kwargs)
        self.fields['preguntador'].queryset = Grupo.objects.exclude(id=grupo.id)

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
