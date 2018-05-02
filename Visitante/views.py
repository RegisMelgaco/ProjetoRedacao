from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import StudentRegisterForm, TeacherRegisterForm, RegisterForm

class IndexView(View):
	def get(self, request):
		perm_aluno = request.user.has_perm('Usuarios.acesso_painel_aluno')
		perm_corretor = request.user.has_perm('Usuarios.acesso_painel_corretor')

		dic = {'perm_aluno': perm_aluno, 'perm_corretor': perm_corretor}

		return render(request, 'Visitante/index.html', dic)

class StudentRegisterView(View):
	def get(self, request):
		f = StudentRegisterForm()
		dic = { 'f': f }

		return render(request, 'Visitante/register.html', dic)
	def post(self, request):
		f = StudentRegisterForm(request.POST)

		if f.is_valid():
			f.save()
			messages.success(request, 'Conta criada com sucesso!')
		else:
			messages.error(request, f.errors)
		return redirect('Visitante:studentRegisterUrl')

class InfoFalhaView(View):
	def get(self, request):
		return render(request, 'Visitante/info.html')