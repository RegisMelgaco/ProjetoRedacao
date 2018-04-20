from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'Visitante'

urlpatterns = [
	path('', IndexView.as_view(), name='indexUrl'),
	path('cadastro/aluno', StudentRegisterView.as_view(), name='studentRegisterUrl'),
	path('login', auth_views.login, {'template_name': 'Visitante/login.html'}, name='login'),
	path('logout', auth_views.logout, {'template_name': 'Visitante/index.html'}, name='logout'),
	path('UsoInvalido', InfoFalhaView.as_view(), name='infoFalhaUrl')
]