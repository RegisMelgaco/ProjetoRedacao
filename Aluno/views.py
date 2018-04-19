from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate

from Visitantes.views import 

class TerminalAlunoView(View):
	def get(self, request):
		if authenticate(aluno=True):
			return render(request, 'Aluno/index.html')
		else:
			return redirect('Visitantes:indexUrl')