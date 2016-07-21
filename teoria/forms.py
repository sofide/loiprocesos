from django import forms

from teoria.models import Unidad


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
