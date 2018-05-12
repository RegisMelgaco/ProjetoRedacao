class Red_Pontos:
	id = '0001'
	description = 'com este ponto se compra uma correçao na nossa plataforma'
	preco = 10
	tabela_desconto = {
		'numero_red_pontos': {10: 0.80, 5: 0.90, 3: 0.95}
	}

	@staticmethod
	def get_preco(quantidade):
		quantidade = int(quantidade)
		descontos = [1]

		''' calculo do desconto '''
		desconto_quantidade = 1
		for i in Red_Pontos.tabela_desconto['numero_red_pontos'].keys():
			if i <= quantidade:
				desconto_quantidade = Red_Pontos.tabela_desconto['numero_red_pontos'][i]
				break

		descontos.append(desconto_quantidade)
		descontos = min(descontos)

		return "%.2f" % (Red_Pontos.preco * descontos)
