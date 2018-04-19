from django.shortcuts import render, redirect
from django.views import View

class PainelDasRedaçoes(View):
	def get(self, request):
		return render(request, 'Visitante/index.html')
