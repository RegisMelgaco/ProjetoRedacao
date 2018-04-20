from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate

class TerminalAlunoView(View):
	def get(self, request):
		if request.user.is_authenticated:
			if request.user.student:
				return render(request, 'Aluno/painelAluno.html')
			else:
				print("não é estudante")
		else:
			print("não está autenticado")