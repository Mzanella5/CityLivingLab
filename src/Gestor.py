
from Services.Exportador import Exportador
from Services.Importador import Importador


class Gestor():
	def __init__(self):
		pass

	def LerArquivo(path:str):
		extencao = path.split('.')[1]
		if extencao == 'csv':
			dados = Importador.ImportarComoCsv(path=path)
			Exportador.ExportarComoCSV(dados)
			print('\nGerado de:' + path + '\n')
		elif extencao == 'pdf':
			dados = Importador.ImportarComoPdf(path=path)
			Exportador.ExportarComoCSV(dados)
			print('\nGerado de:' + path + '\n')
		elif extencao == 'html':
			pass
		else:
			print('Formato não suportado')