from django.urls import path
from django.contrib.auth import views as auth_views

from Visitante.views import (
	IndexView,
	StudentRegisterView,
	TeacherRegisterView,
	)

urlpatterns = [
	path('', IndexView.as_view(), name='indexUrl'),
	path('cadastro/aluno', StudentRegisterView.as_view(), name='studentRegisterUrl'),
	path('cadastro/professor', TeacherRegisterView.as_view(), name='teacherRegisterUrl'),
	path('login', auth_views.login, {'template_name': 'Visitante/login.html'}, name='login'),
	path('logout', auth_views.logout, {'template_name': 'Visitante/index.html'}, name='logout'),
]