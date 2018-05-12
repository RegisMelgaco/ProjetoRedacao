from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
from pagseguro.api import PagSeguroItem, PagSeguroApi
from decouple import config

from Aluno.forms import CompraForm
from .servicos import Red_Pontos

class CompraView(View):
	def post(self, request):
		f = CompraForm(request.POST)

		item = PagSeguroItem(id=Red_Pontos.id, description=Red_Pontos.description, amount=Red_Pontos.get_preco(f['quantidade'].data), quantity=str(f['quantidade'].data))

		pagseguro_api = PagSeguroApi(email=config('PAGSEGURO_EMAIL'), token=config('PAGSEGURO_TOKEN'))
		pagseguro_api.add_item(item)
		data = pagseguro_api.checkout()

		return redirect(data['redirect_url']) 