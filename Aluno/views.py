from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate

from .forms import *
from Redacao.models import (Proposta, Redacao)

class PainelAlunoView(View):
	def get(self, request):
		if request.user.is_authenticated:
			if request.user.has_perm('Usuarios.acesso_painel_aluno'):
				propostas = Proposta.objects.filter(em_uso = True)
				redacoes  = request.user.redacoes.all()
				f = CompraForm()

				dic = {'propostas': propostas, 'redacoes': redacoes,'f': f}

				return render(request, 'Aluno/painelAluno.html', dic)
			else:
				messages.add_message(request, messages.INFO, 'Você não tem permição de entrar no painel de alunos')
				return redirect('Visitante:infoFalhaUrl')
		else:
			messages.add_message(request, messages.INFO, 'Você não está logado')
			return redirect('Visitante:infoFalhaUrl')

class PerfilView(View):
	def get(self, request):
		if request.user.is_authenticated:
			if request.user.has_perm('Usuarios.acesso_terminal_aluno'):
				f = ModifyUserForm()
				dic = { 'f': f }

				return render(request, 'Aluno/perfil.html', dic)
			else:
				messages.add_message(request, messages.INFO, 'Você não tem permição de entrar no terminal de alunos')
				return redirect('Visitante:infoFalhaUrl')
		else:
			messages.add_message(request, messages.INFO, 'Você não está logado')
			return redirect('Visitante:infoFalhaUrl')
	def post(self, request):
		if request.user.is_authenticated:
			if request.user.has_perm('Usuarios.acesso_terminal_aluno'):
				f = ModifyUserForm(request.POST)

				if f.is_valid():
					f.save(user=request.user)
					messages.success(request, 'Informações alteradas com sucesso!')
				else:
					messages.error(request, f.errors)
				return redirect('Aluno:perfilUrl')
			else:
				messages.add_message(request, messages.INFO, 'Você não tem permição de entrar no terminal de alunos')
				return redirect('Visitante:infoFalhaUrl')
		else:
			messages.add_message(request, messages.INFO, 'Você não está logado')
			return redirect('Visitante:infoFalhaUrl')