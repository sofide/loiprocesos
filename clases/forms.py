from django import forms
from django.conf import settings
from django.utils import timezone

from clases.models import ContadorPreguntas, Clase, Exposicion, Pregunta, TP
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
    fecha = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.widgets.DateInput(format=settings.DATE_INPUT_FORMATS[0]),
        initial=timezone.now())

    class Meta:
        model = Clase
        fields = ('fecha', )


class ExposicionForm(forms.ModelForm):

    class Meta:
        model = Exposicion
        fields = ('grupo', 'tp')


class ExposicionVirtualForm(forms.ModelForm):

    class Meta:
        model = Exposicion
        fields = ('tp', 'video', 'description')


class StartExpoForm(forms.ModelForm):
    start_expo = forms.DateTimeField(
        input_formats=settings.DATETIME_INPUT_FORMATS,
        widget=forms.widgets.DateTimeInput(format=settings.DATETIME_INPUT_FORMATS[0]),
        initial=timezone.now())

    class Meta:
        model = Exposicion
        fields = ('start_expo',)


class StartQuestionsForm(forms.ModelForm):
    start_ques = forms.DateTimeField(
        input_formats=settings.DATETIME_INPUT_FORMATS,
        widget=forms.widgets.DateTimeInput(format=settings.DATETIME_INPUT_FORMATS[0]),
        initial=timezone.now())

    class Meta:
        model = Exposicion
        fields = ('start_ques',)


class FinishExpoForm(forms.ModelForm):
    finish_expo = forms.DateTimeField(
        input_formats=settings.DATETIME_INPUT_FORMATS,
        widget=forms.widgets.DateTimeInput(format=settings.DATETIME_INPUT_FORMATS[0]),
        initial=timezone.now())

    class Meta:
        model = Exposicion
        fields = ('finish_expo',)


class AddPreguntasForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ('exposicion', 'pregunta')
        widgets = {
          'pregunta': forms.Textarea(attrs={'rows':3}),
        }


class EditTPForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(EditTPForm, self).__init__(*args,**kwargs)
        self.fields['descripcion'].widget = forms.HiddenInput()
        self.fields['descripcion'].label = "Decripción"
        self.fields['numero'].label = "Número"

    class Meta:
        model = TP
        fields = ('numero', 'nombre', 'descripcion')
