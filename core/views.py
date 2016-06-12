from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context import RequestContext

from .autocomplete_views import * # importando Autocompletes

@login_required
def home(request):
    user_group = request.user.groups.first()
    if user_group.name == "pais":
        return render(request, "core/index_responsaveis.html")
    elif user_group.name == "professores":
        return redirect(reverse("escolher_disciplina",urlconf="core.urls"))
    elif user_group.name == "Administrador":
        return redirect("/paada_admin")


@login_required
def escolher_disciplina(request):
    professor = request.user.professor
    disciplinas = professor.disciplinas.all()
    context = RequestContext(request,{'disciplinas': disciplinas})
    return render(request, "core/escolher_disciplina.html", context)
