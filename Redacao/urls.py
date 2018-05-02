from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'Redacao'

urlpatterns = [
	path('Terminal-Aluno/Enviar-Redacao', EnviarRedacaoView.as_view(), name='enviarRedacaoUrl'),
]


"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""