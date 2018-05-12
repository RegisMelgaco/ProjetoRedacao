from django import forms

from django.utils import timezone

from Usuarios.models import User

class ModifyUserForm(forms.Form):
	email             = forms.EmailField(max_length=255, required=False)
	password1         = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False, max_length=128)
	password2         = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput, required=False, max_length=128)
	primeiro_nome     = forms.CharField(required=False, max_length=20)
	segundo_nome      = forms.CharField(required=False, max_length=60)
	cep               = forms.CharField(required=False, max_length=9)

	def save(self, user, commit=True):
		if self['email'].data:
			user.email = self['email'].data
		if self['password1'].data:
			user.set_password(self.cleaned_data["password1"])
		if self['primeiro_nome'].data:
			user.primeiro_nome = self['primeiro_nome'].data
		if self['segundo_nome'].data:
			user.segundo_nome = self['segundo_nome'].data
		if self['cep'].data:
			user.cep = self['cep'].data

		if commit:
			user.save()
		return user

class CompraForm(forms.Form):
	quantidade        = forms.IntegerField()
