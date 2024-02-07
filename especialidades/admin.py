from django.contrib import admin
from .models import Especialidade, Profissional, AgendamentoConsulta

# admin.site.register(DadosConsulta)
# admin.site.register(SolicitarConsulta)
# admin.site.register(PacoteConsultas)
admin.site.register(AgendamentoConsulta)
admin.site.register(Profissional)
admin.site.register(Especialidade)


# Register your models here.
