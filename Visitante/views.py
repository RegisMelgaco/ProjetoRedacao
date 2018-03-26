from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from Usuarios.forms import StudentRegisterForm, TeacherRegisterForm

class IndexView(View):
	def get(self, request):
		return render(request, 'Visitante/index.html')

class StudentRegisterView(View):
	def get(self, request):
		f = StudentRegisterForm()

		dic = {
			'form': f
		}

		return render(request, 'Visitante/register.html', dic)
	def post(self, request):
		f = StudentRegisterForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully')
		else:
			messages.error(request, 'Invalid Form')
		return redirect('Visitante/cadastrar')

class TeacherRegisterView(View):
	def get(self, request):
		f = TeacherRegisterForm()

		dic = {
			'form': f
		}

		return render(request, 'Visitante/register.html', dic)
	def post(self, request):
		f = TeacherRegisterForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully')
		else:
			messages.error(request, 'Invalid Form')
		return redirect('Visitante/cadastrar')