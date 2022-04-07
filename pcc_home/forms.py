from django import forms
from .models import Prog_contents

#--------------------------------------------------
class Prog_contents_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Prog_contents
        fields = ['num', 'title', 'web_site']
        labels = {
            'num'       : '番号',
            'title'     : 'タイトル',
            'web_site'  : 'URL',
        }

#--------------------------------------------------
class Prog_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    num = forms.IntegerField(label = '番号', \
        widget = forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder': 0}))

    title = forms.CharField(label = 'タイトル', \
        widget = forms.TextInput(attrs = {'class' : 'form-control'}))

    web_site = forms.URLField(label = 'URL', \
        widget = forms.TextInput(attrs = {'class' : 'form-control'}))