from django.db import models
from datetime import datetime

class Redacao(models.Model):
	redacao            = models.ImageField(upload_to='Redacoes/%Y/%m/%d/', null=True)
	proposta           = models.IntegerField(null=False)
	correcao           = models.ImageField(upload_to='Correcoes/%Y/%m/%d/', null=True)
	data_pedido        = models.DateTimeField(null=True, default=datetime.now)
	corrigida          = models.BooleanField(default=False, null=False)
	nota_competencia_1 = models.IntegerField(default=0, null=True)
	nota_competencia_2 = models.IntegerField(default=0, null=True)
	nota_competencia_3 = models.IntegerField(default=0, null=True)
	nota_competencia_4 = models.IntegerField(default=0, null=True)
	nota_competencia_5 = models.IntegerField(default=0, null=True)
	nota               = models.IntegerField(default=0, null=True)
