from django import forms
from .models import Goroskop


class GoroskopForm(forms.ModelForm):
    class Meta:
        model = Goroskop
        fields = ('title','text')