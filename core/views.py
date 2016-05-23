from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, content="Login Efetuado com sucesso")


@login_required
def listar_disciplinas(request):
    return render(request, content="Listando disciplinas")