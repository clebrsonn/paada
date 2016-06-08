from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, "core/index.html")

@login_required
def listar_disciplinas(request):
    return render(request, content="Listando disciplinas")