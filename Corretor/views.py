from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate

from Redacao.models import Proposta

class PainelCorretorView(View):
	def get(self, request):
		if request.user.is_authenticated:
			if request.user.has_perm('Usuarios.acesso_painel_corretor'):
				propostas = Proposta.objects.filter(em_uso = True)

				dic = {'propostas': propostas}
				return render(request, 'Corretor/painelCorretor.html', dic)
			else:
				messages.add_message(request, messages.INFO, 'Você não tem permição de entrar no painel de corretores')
				return redirect('Visitante:infoFalhaUrl')
		else:
			messages.add_message(request, messages.INFO, 'Você não está logado')
			return redirect('Visitante:infoFalhaUrl')