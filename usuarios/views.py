from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        if any(letra.isdigit() for letra in primeiro_nome):
            messages.add_message(request, constants.ERROR, message="Nome não pode conter números.")
            return redirect("/usuarios/cadastro")

        if any(letra.isdigit() for letra in ultimo_nome):
            messages.add_message(request, constants.ERROR, message="Sobrenome não pode conter números.")
            return redirect("/usuarios/cadastro")

        if not len(cpf) == 11 or not cpf.isdigit():
            messages.add_message(request, constants.ERROR, message="CPF inválido, use apenas números")
            return redirect("/usuarios/cadastro/")

        if '@' not in email or not any(ext in email for ext in [".com", ".br", ".org"]):
            messages.add_message(request, constants.ERROR, message="Email inválido, use '@' e .com ou .br ou .org")
            return redirect("/usuarios/cadastro/")

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas não são iguais.")
            return redirect('/usuarios/cadastro/')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "A senha tem menos que 6 caracters.")
            return redirect('/usuarios/cadastro/')

        user = User.objects.filter(email=email).exists()

        if user:
            messages.add_message(request, constants.ERROR, message="Email já cadastrado")
            return redirect('/usuarios/cadastro/')


        try:

            # Username deve ser único!
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=cpf,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso')
        except:
            messages.add_message(request, constants.ERROR, 'CPF já cadastrado, para mais dúvidas contate o suporte.')
            return redirect('/usuarios/cadastro/')
            
        return HttpResponse('/usuarios/cadastro/')


def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')

    # if request.method == "POST":
    #     cpf = request.POST.get('cpf')
    #     senha =

    elif request.method == "POST":
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        user = authenticate(username=cpf, password=senha)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, "Username ou senha inválidos.")
            return redirect('/usuarios/login')







# Create your views here.
