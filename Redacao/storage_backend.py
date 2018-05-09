from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class RedacoesStorage(S3Boto3Storage):
	file_overwrite = False
	bucket_name = 'redacoes-bucket'
