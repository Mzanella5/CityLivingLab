
from Services.Exportador import Exportador
from Services.Importador import Importador


class Gestor():
	def __init__(self):
		pass

	def LerArquivo(path:str):
		extencao = path.split('.')
		extencao = extencao[ len(extencao)-1]
		if extencao == 'csv':
			dados = Importador.ImportarComoCsv(path=path)
			Exportador.ExportarComoCSV(dados)
			print('\nGerado de:' + path + '\n')
		elif extencao == 'pdf':
			dados = Importador.ImportarComoPdf(path=path)
			Exportador.ExportarComoCSV(dados[0])
			print('\nGerado de:' + path + '\n')
		elif extencao == 'json':
			dados = Importador.ImportarComoJSON(path=path)
			Exportador.ExportarComoCSV(dados)
			print('\nGerado de:' + path + '\n')
		elif path.startswith("http://",0,7) or path.startswith("https://",0,8):
			dados = Importador.ImportarComoHtml(path)
			Exportador.ExportarComoCSV(dados)
			print('\nGerado de:' + path + '\n')
		else:
			print('Formato não suportado')
