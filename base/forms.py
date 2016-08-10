from django import forms

from base.models import Text


class EditTextForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(EditTextForm, self).__init__(*args,**kwargs)
        self.fields['text'].widget = forms.HiddenInput()
    class Meta:
        model = Text
        fields = ('text',)
