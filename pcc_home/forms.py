from django import forms
from .models import Prog_contents

#--------------------------------------------------
class Prog_contents_form(forms.ModelForm):
    class Meta:
        model = Prog_contents
        fields = ['num', 'title', 'web_site']

#--------------------------------------------------
class Prog_form(forms.Form):
    num = forms.IntegerField(label = 'num', \
        widget = forms.NumberInput(attrs = {'class' : 'form-control'}))

    title = forms.CharField(label = 'title', \
        widget = forms.TextInput(attrs = {'class' : 'form-control'}))

    web_site = forms.URLField(label = 'web_site', \
        widget = forms.TextInput(attrs = {'class' : 'form-control'}))