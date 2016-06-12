from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User

from dal.autocomplete import Select2QuerySetView

from .models import Responsavel, Professor, AnoLetivo, Turma

@login_required
def home(request):
    user_group = request.user.groups.first()
    if user_group.name == "pais":
        return render(request, "core/index_responsaveis.html")
    elif user_group.name == "professores":
        return render(request, "core/index_professores.html")
    elif user_group.name == "Administrador":
        return redirect("/paada_admin")


#################
# autocompletes #
#################
class ResponsaveisAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        qs = Responsavel.objects.all()
        if self.q:
            qs = qs.filter(nome__istartswith=self.q)
        return qs


class UsuariosAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        usuario1 = list(Responsavel.objects.values_list('usuario'))
        usuario2 = list(Professor.objects.values_list('usuario'))
        usuarios_id = [pk[0] for pk in usuario1+usuario2]
        qs = User.objects.exclude(pk__in=usuarios_id)
        if self.q:
            qs = qs.filter(username__istartswith=self.q)
        return qs


class AnosLetivosAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        qs = AnoLetivo.objects.all()
        if self.q:
            qs = qs.filter(username__istartswith=self.q)
        return qs

class ProfessoresAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        qs = Professor.objects.all()
        if self.q:
            qs = qs.filter(nome__istartswith=self.q)
        return qs

class TurmasAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        qs = Turma.objects.all()
        if self.q:
            qs = qs.filter(nome_turma__istartswith=self.q)
        return qs