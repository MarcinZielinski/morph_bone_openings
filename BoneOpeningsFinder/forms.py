# forms.py
from django import forms
from .models import *


class XRayForm(forms.ModelForm):
    class Meta:
        model = XRay
        fields = ['xRayImg']
