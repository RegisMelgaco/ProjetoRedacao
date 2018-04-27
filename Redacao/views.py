from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import *
from .models import Redacao

class EnviarRedacaoView(View):
	def get(self, request):
		f = SendRedacaoForm()
		dic = { 'f': f }

		return render(request, 'Redacao/enviar.html', dic)
	def post(self, request):
		f = SendRedacaoForm(request.POST, request.FILES)
		if f.is_valid():
			m = f.save(commit=False)
			m.aluno = request.user.email
			m.save()
			messages.success(request, 'Redação enviada com sucesso!')
		else:
			messages.error(request, f.errors)

		return redirect('Redacao:enviarRedacaoUrl')