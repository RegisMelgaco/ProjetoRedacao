from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'Aluno'

urlpatterns = [
	path('Painel-Aluno', PainelAlunoView.as_view(), name='painelAlunoUrl'),
	path('Painel-Aluno/Perfil', PerfilView.as_view(), name='perfilUrl')
]