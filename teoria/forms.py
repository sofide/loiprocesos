from django import forms

from teoria.models import Unidad, Material, Pregunta


class EditUdForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(EditUdForm, self).__init__(*args,**kwargs)
        self.fields['descripcion'].widget = forms.HiddenInput()
    class Meta:
        model = Unidad
        fields = ('numero', 'titulo', 'descripcion')
        widgets = {
          'titulo': forms.TextInput(attrs={'size':100}),
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('nombre', 'link', 'autor')


class PreguntaTeoriaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ('pregunta', 'autor')


class MaterialEditForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('nombre', 'link', 'autor', 'vigente')


class PreguntaTeoriaEditForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ('pregunta', 'autor', 'vigente')
