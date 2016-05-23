# -*- coding: utf-8 -*-

from ajax_select import register, LookupChannel
from .models import Responsavel


@register('responsavel')
class ResponsavelLookup(LookupChannel):
    """Classe responsável pelo o autocomplete de responsáveis."""

    model = Responsavel

    def get_query(self, q, request):
        return self.model.objects.filter(nome__icontains=q).order_by('nome')
