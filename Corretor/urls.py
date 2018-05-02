from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'Corretor'

urlpatterns = [
	path('Painel-Corretor', PainelCorretorView.as_view(), name='painelCorretorUrl'),
]