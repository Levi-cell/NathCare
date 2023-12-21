from django.db import models
from django.contrib.auth.models import User
from cpf_field.models import CPFField
# Create your models here.


class Especialidade(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    CPF = CPFField()
    especialidades = models.ForeignKey(Especialidade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class AgendamentoConsulta(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Profissional = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)
    Data = models.DateTimeField()

    def __str__(self):
        return f'{self.usuario} | {self.Data}'

