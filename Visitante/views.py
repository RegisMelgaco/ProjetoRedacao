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

		dic = {
			'f': f
		}

		return render(request, 'Visitante/register.html', dic)
	def post(self, request):
		f = StudentRegisterForm(request.POST)

		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully')
		else:
			messages.error(request, f.errors)
		return redirect('Visitante:studentRegisterUrl')

class InfoFalhaView(View):
	def get(self, request):
		return render(request, 'Visitante/info.html')