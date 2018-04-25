from django import forms

from .models import Redacao

class SendRedacaoForm(forms.ModelForm):
	redacao = forms.ImageField(label='Selecione a imagem da sua redação',
        help_text='Tamanho maximo não estipulado')

	class Meta:
		model = Redacao
		fields = ()