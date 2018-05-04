from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'Redacao'

urlpatterns = [
	path('Terminal-Aluno/Enviar-Redacao', EnviarRedacaoView.as_view(), name='enviarRedacaoUrl'),
	path('Painel-Corretor/pedir-redacao', PedirRedacaoView.as_view(), name='pedirRedacaoUrl'),
	path('Painel-Corretor/corrigir', CorrigirView.as_view(), name='corrigirUrl')
]
