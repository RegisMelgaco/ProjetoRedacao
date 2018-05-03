from django import forms

from .models import (Redacao, Proposta)

class SendRedacaoForm(forms.ModelForm):
	proposta = forms.ModelChoiceField(queryset = Proposta.objects.filter(em_uso = True))

	class Meta:
		model = Redacao
		fields = ('redacao',)