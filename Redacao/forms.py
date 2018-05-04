from django import forms

from .models import (Redacao, Proposta)

class SendRedacaoForm(forms.ModelForm):
	proposta = forms.ModelChoiceField(queryset = Proposta.objects.filter(em_uso = True))

	class Meta:
		model = Redacao
		fields = ('redacao',)

	def save(self, user, commit=True):
		redacao = super(forms.ModelForm, self).save(commit=False)
		redacao.proposta = Proposta.objects.get(id=self['proposta'].data)
		if commit:
			redacao.save()
			user.redacoes.add(redacao.id)
			user.save()
		return redacao

class SendCorrecaoForm(forms.ModelForm):

	class Meta:
		model = Redacao
		fields = ('nota_competencia_1', 'nota_competencia_2', 'nota_competencia_3', 'nota_competencia_4', 'nota_competencia_5', 'correcao')

	def save(self, redacao, commit=True):
		redacao.nota_competencia_1 = self['nota_competencia_1'].data
		redacao.nota_competencia_2 = self['nota_competencia_2'].data
		redacao.nota_competencia_3 = self['nota_competencia_3'].data
		redacao.nota_competencia_4 = self['nota_competencia_4'].data
		redacao.nota_competencia_5 = self['nota_competencia_5'].data
		redacao.correcao           = self['correcao'].data
		redacao.nota               = int(self['nota_competencia_1'].data) + int(self['nota_competencia_2'].data) + int(self['nota_competencia_3'].data) + int(self['nota_competencia_4'].data) + int(self['nota_competencia_5'].data)
		redacao.corrigida          = True
		if commit:
			redacao.save()
		return redacao