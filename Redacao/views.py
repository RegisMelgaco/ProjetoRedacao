from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import *
from .models import (Redacao, Proposta)

class EnviarRedacaoView(View):
	def get(self, request):
		f = SendRedacaoForm()
		ps = Proposta.objects.filter(em_uso = True)
		dic = { 'f': f, 'ps': ps}

		return render(request, 'Redacao/enviar.html', dic)
	def post(self, request):
		f = SendRedacaoForm(request.POST, request.FILES)
		if f.is_valid():
			m = f.save(user=request.user)
			messages.success(request, 'Redação enviada com sucesso!')
		else:
			messages.error(request, f.errors)

		return redirect('Redacao:enviarRedacaoUrl')

class PedirRedacaoView(View):
	def post(self, request):
		request.user.redacoes.add(Redacao.objects.filter(corrigida=False).first())
		request.user.save()

		messages.success(request, 'Pedido com Sucesso!')

		return redirect('Corretor:painelCorretorUrl')

class CorrigirView(View):
	def get(self, request):
		if request.user.is_authenticated:
			if request.user.has_perm('Usuarios.acesso_painel_corretor'):
				redacao = request.user.redacoes.get(corrigida=False)
				f = SendCorrecaoForm()

				dic = {'redacao': redacao, 'f': f}

				return render(request, 'Redacao/corrigir.html', dic)
			else:
				messages.add_message(request, messages.INFO, 'Você não tem permição de entrar no painel de corretores')
				return redirect('Visitante:infoFalhaUrl')
		else:
			messages.add_message(request, messages.INFO, 'Você não está logado')
			return redirect('Visitante:infoFalhaUrl')

	def post(self, request):
		f = SendCorrecaoForm(request.POST, request.FILES)
		if f.is_valid():
			redacao = request.user.redacoes.get(corrigida=False)
			f.save(redacao=redacao)
			messages.success(request, 'Correção enviada com sucesso!')
		else:
			messages.error(request, f.errors)
		return redirect('Corretor:painelCorretorUrl')