from django import forms

from .models import Redacao

class SendRedacaoForm(forms.ModelForm):
	class Meta:
		model = Redacao
		fields = ('redacao', 'proposta')