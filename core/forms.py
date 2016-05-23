# -*- coding: utf-8 -*-

from datetime import datetime
from django import forms
from .models import AnoLetivo


class AnoLetivoForm(forms.ModelForm):
    """Form para adição de novos anos letivos."""

    def __init__(self, *args, **kwargs):
        super(AnoLetivoForm, self).__init__(*args,**kwargs)
        self.fields['titulo'].initial = datetime.now().year
        self.fields['titulo'].widget.attrs['readonly'] = True

    class Meta:
        model = AnoLetivo
        fields = ['titulo']
