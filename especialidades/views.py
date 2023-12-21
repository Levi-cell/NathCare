from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Especialidade
# from .models import StatusConsulta


@login_required()
def solicitar_consultas(request):
    if request.method == "GET":
        especialidades = Especialidade.objects.all()
        return render(request, 'solicitar_consultas.html', {'especialidades': especialidades})

# Create your views here.
