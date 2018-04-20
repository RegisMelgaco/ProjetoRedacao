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
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)

	generos = (
		('M', 'Masculino'),
		('F', 'Feminino'),
		('O', 'Outro'),
		('P', 'Esta informação é particular')
	)

	red_pontos = models.IntegerField(default=0)
	genero = models.CharField(choices=generos, max_length=1, default='P')
	nascimento = models.DateField(default=None, null=True)
	ingresso_ensino_medio = models.DateField(default=None, null=True)

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