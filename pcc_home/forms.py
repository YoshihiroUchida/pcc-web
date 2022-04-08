from django import forms
from .models import Programming_contents

#==================================================
class Programming_edit_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Programming_contents
        fields = ['num', 'title', 'url']
        labels = {
            'num'   : '番号',
            'title' : 'タイトル',
            'url'   : 'URL',
        }

#==================================================
class Programming_reg_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    num = forms.IntegerField(label = '番号', \
        widget = forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder': 0}))

    title = forms.CharField(label = 'タイトル', \
        widget = forms.TextInput(attrs = {'class' : 'form-control'}))

    url = forms.URLField(label = 'URL', \
        widget = forms.TextInput(attrs = {'class' : 'form-control'}))
