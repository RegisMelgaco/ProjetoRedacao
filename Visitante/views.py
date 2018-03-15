from django.shortcuts import render

def index(request):
	return render(request, 'Visitante/index.html')

def cadastrar(request):
	return render(request, 'Visitante/cadastrar.html')