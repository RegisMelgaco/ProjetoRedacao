from django.db import models
from datetime import datetime

class Redacao(models.Model):
	redacao            = models.ImageField(upload_to='Redacoes', default='Redacoes/1.jpg', null=True)
	correcao           = models.ImageField(upload_to='Correcoes', null=True)
	aluno              = models.EmailField(max_length=255, null=False)
	professor          = models.EmailField(max_length=255, null=False)
	data_pedido        = models.DateTimeField(null=True, default=datetime.now)
	corrigida          = models.BooleanField(default=False, null=False)
	nota_competencia_1 = models.IntegerField(default=0, null=True)
	nota_competencia_2 = models.IntegerField(default=0, null=True)
	nota_competencia_3 = models.IntegerField(default=0, null=True)
	nota_competencia_4 = models.IntegerField(default=0, null=True)
	nota_competencia_5 = models.IntegerField(default=0, null=True)
	nota               = models.IntegerField(default=0, null=True)
