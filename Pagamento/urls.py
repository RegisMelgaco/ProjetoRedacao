from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'Pagamento'

urlpatterns = [
	path('Terminal-Aluno/Compra', CompraView.as_view(), name='compraUrl'),
]