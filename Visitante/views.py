from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import StudentRegisterForm, TeacherRegisterForm, RegisterForm

class IndexView(View):
	def get(self, request):
		return render(request, 'Visitante/index.html')

class StudentRegisterView(View):
	def get(self, request):
		f = StudentRegisterForm()
		dic = { 'f': f }

		return render(request, 'Visitante/register.html', dic)
	def post(self, request):
		m = StudentRegisterForm(request.POST)

		if m.is_valid():
			m.save()
			messages.success(request, 'Conta criada com sucesso!')
		else:
			messages.error(request, f.errors)
		return redirect('Visitante:studentRegisterUrl')

class InfoFalhaView(View):
	def get(self, request):
		return render(request, 'Visitante/info.html')