from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, password):
		user = self.create_user(
			email,
			password=password,
		)
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
			email,
			password=password,
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user

	def create_student(self, email, password, genero, idade, ingresso_ensino_medio):
		user = self.create_user(
			email,
			password=password,
		)
		user.student = True
		user.save(using=self._db)
		
		return user

	def create_teacher(self, email, password):
		user = self.create_user(
			email,
			password=password,
		)
		user.teacher = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
		verbose_name='email',
		max_length=255,
		unique=True,
		null=False
	)
	active = models.BooleanField(default=True, null=False)
	staff  = models.BooleanField(default=False, null=False)
	admin  = models.BooleanField(default=False, null=False)

	generos = (
		('M', 'Masculino'),
		('F', 'Feminino'),
		('O', 'Outro'),
		('P', 'Esta informação é particular')
	)

	primeiro_nome         = models.CharField("primeiro Nome", max_length=12, null=False)
	segundo_nome          = models.CharField("segundo Nome", max_length=30, null=False)
	cep                   = models.CharField("CEP", max_length=9, null=True)

	red_pontos            = models.IntegerField(default=0, null=False)
	red_feitas            = models.IntegerField(default=0, null=False)
	genero                = models.CharField("genero", choices=generos, max_length=1, default='P', null=True)
	nascimento            = models.DateField("data de nascimento", default=None, null=True)
	ingresso_ensino_medio = models.DateField("ingresso no ensino médio", default=None, null=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] # Email & Password are required by default.

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def get_red_pontos(self):
		return self.red_pontos

	def get_genero(self):
		return self.genero

	def get_idade(self):
		return self.idade

	def get_ingresso_ensino_medio(self):
		return self.ingresso_ensino_medio

	def __str__(self):
		return self.email

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active

	@property
	def is_student(self):
		return self.active

	@property
	def is_teacher(self):
		return self.active

	objects = UserManager()