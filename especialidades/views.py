from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Especialidade, Profissional
from django.core.serializers import serialize
# from .models import StatusConsulta


@login_required()
def solicitar_consultas(request):
    if request.method == "GET":
        especialidades = Especialidade.objects.all()
        return render(request, 'solicitar_consultas.html', {'especialidades': especialidades})


def solicitar_profissionais(request):
    if request.method == "GET":
        profissionais = Profissional.objects.all()
        dados_profissionais = []

        for profissional in profissionais:
            dados_profissional = {
                'nome': profissional.nome,
                'especialidades': profissional.especialidades.id
            }
            dados_profissionais.append(dados_profissional)
        
        return JsonResponse(dados_profissionais, safe=False)


# Create your views here.
