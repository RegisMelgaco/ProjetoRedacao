from django.conf import settings

def redacao_url(request):
	return {'redacao_url': settings.REDACOES_URL}