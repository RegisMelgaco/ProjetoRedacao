from django import forms

from django.utils import timezone

from Usuarios.models import User

class ModifyUser(forms.ModelForm):
	email = forms.EmailField(required=False)
	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False)
	password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput, required=False)
	nascimento = forms.DateField(label='Nascimento', widget=forms.SelectDateWidget(years=[y for y in range(timezone.now().year, timezone.now().year - 100, -1)]), required=False)
	ingresso_ensino_medio = forms.DateField(label='Ingresso no Ensio Médio', widget=forms.SelectDateWidget(years=[y for y in range(timezone.now().year, timezone.now().year - 50, -1)]), required=False)
	genero = forms.ChoiceField(widget=forms.RadioSelect, required=False, choices=(
		('M', 'Masculino'),
		('F', 'Feminino'),
		('O', 'Outro'),
		('P', 'Esta informação é particular')
	))
	class Meta: 
		model = User
		fields = ('email',)

	def save(self, user, commit=True):
		if self['email'].data:
			user.email = self['email'].data
		if self['password1'].data:
			user.set_password(self.cleaned_data["password1"])
		if self['nascimento'].data:
			user.nascimento = self.cleaned_data['nascimento']
		if self['ingresso_ensino_medio'].data:
			user.ingresso_ensino_medio = self.cleaned_data['ingresso_ensino_medio']
		if self['genero'].data:
			user.genero = self.cleaned_data['genero']	

		if commit:
			user.save()
		return user