from django.contrib import admin

from .models import Redacao

class RedacaoAdmin(admin.ModelAdmin):
	list_display = ('data_pedido', 'corrigida')
	list_filter = ('corrigida',)

	fieldsets = (
		(None, {'fields': ('corrigida', 'data_pedido')}),
		('Notas', {'fields': ('nota_competencia_1', 'nota_competencia_2', 'nota_competencia_3', 'nota_competencia_4', 'nota_competencia_5', 'nota')}),
		('Imagens', {'fields': ('redacao', 'correcao')})
	)
	search_fields = ('corrigida',)
	ordering = ('data_pedido',)


admin.site.register(Redacao, RedacaoAdmin)