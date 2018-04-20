from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate

class TerminalAlunoView(View):
	def get(self, request):
		if request.user.is_authenticated:
			if request.user.has_perm('Usuarios.acesso_terminal_aluno'):
				return render(request, 'Aluno/painelAluno.html')
			else:
				messages.add_message(request, messages.INFO, 'Você não tem permição de entrar no terminal de alunos')
				return redirect('Visitante:infoFalhaUrl')
		else:
			messages.add_message(request, messages.INFO, 'Você não está logado')
			return redirect('Visitante:infoFalhaUrl')