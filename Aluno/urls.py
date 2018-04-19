from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'Aluno'

urlpatterns = [
	path('Terminal-Aluno', TerminalAlunoView.as_view(), name='terminalAlunoUrl')
]