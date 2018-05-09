from django.db import models
from datetime import datetime
from .storage_backend import RedacoesStorage
from storages.backends.s3boto3 import S3Boto3Storage

class Redacao(models.Model):
	redacao            = models.ImageField(null=True, upload_to='redacoes', storage=RedacoesStorage())
	proposta           = models.ForeignKey('Proposta',on_delete=models.SET_NULL, null=True)
	correcao           = models.ImageField(null=True, upload_to='correcoes', storage=RedacoesStorage())
	data_pedido        = models.DateTimeField(null=True, default=datetime.now)
	corrigida          = models.BooleanField(default=False, null=False)
	nota_competencia_1 = models.IntegerField(default=0, null=True)
	nota_competencia_2 = models.IntegerField(default=0, null=True)
	nota_competencia_3 = models.IntegerField(default=0, null=True)
	nota_competencia_4 = models.IntegerField(default=0, null=True)
	nota_competencia_5 = models.IntegerField(default=0, null=True)
	nota               = models.IntegerField(default=0, null=True)

	def __str__(self):
		return str(self.data_pedido)

class Proposta(models.Model):
	titulo             = models.CharField(max_length=110, null=False)
	numero             = models.IntegerField(null=False)
	imagem             = models.ImageField(null=False, upload_to='propostas', storage=S3Boto3Storage())
	em_uso             = models.BooleanField(default=False)

	def __str__(self):
		return self.titulo