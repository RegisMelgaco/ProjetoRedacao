import os
from decouple import config
from dj_database_url import parse as dburl

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['projeto-redacao.herokuapp.com', '127.0.0.1', 'www.xn--redao-dra1a.online', '192.168.0.101']

AUTH_USER_MODEL = 'Usuarios.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'pagseguro',
    'Visitante',
    'Usuarios',
    'Redacao',
    'Pagamento',
    'Aluno',
    'Corretor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projeto_redacao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'projeto_redacao.context_processors.redacao_url'
            ],
        },
    },
]

WSGI_APPLICATION = 'projeto_redacao.wsgi.application'

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8lvbrpf06mc4',
        'USER': 'xfitpnykugkfyo',
        'PASSWORD': '2520ca2de79285253c29ecbbe43b21e78626c3fc1f29623c17463910b62e0496',
        'HOST': 'ec2-50-17-206-214.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'redacao-bucket'
AWS_REDACOES_STORAGE_BUCKET_NAME = 'redacoes-bucket'
AWS_SERVER = 's3-sa-east-1'
AWS_S3_CUSTOM_DOMAIN = '%s.amazonaws.com/%s' % (AWS_SERVER, AWS_STORAGE_BUCKET_NAME)
AWS_STATIC_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
REDACOES_URL = 'https://%s.amazonaws.com/%s/' % (AWS_SERVER, AWS_REDACOES_STORAGE_BUCKET_NAME)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

PAGSEGURO_EMAIL = config('PAGSEGURO_EMAIL')
PAGSEGURO_TOKEN = config('PAGSEGURO_TOKEN')
PAGSEGURO_SANDBOX = True
PAGSEGURO_LOG_IN_MODEL = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'Visitante:indexUrl'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')