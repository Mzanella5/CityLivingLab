from Services.Exportador import Exportador
from Services.Importador import Importador


class Programa():
	def __init__(self):

		#dados = Importador.ImportarComoCsv(self)
		dados = Importador.ImportarComoHtml(self, url = "https://www.w3schools.com/html/html_tables.asp")
		Exportador.ExportarComoJson(self, dados[0])
		print('Feito!')


if __name__ == "__main__":
    Programa()