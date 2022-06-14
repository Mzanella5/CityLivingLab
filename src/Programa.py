from Services.Exportador import Exportador
from Services.Importador import Importador

class Programa():
	def __init__(self):
		url1 = 'https://remuneracoes.caxias.rs.gov.br/2022/05/01/mensal'
		url2 = 'https://www.w3schools.com/html/html_tables.asp'
		dados = Importador.ImportarComoCsv(self, path='../pessoal.csv')
		#dados = Importador.ImportarComoHtml(self, url=url2)
		#dados = Importador.ImportarComoPdf(self, '../salario.pdf')
		Exportador.ExportarComoJson(self, dados)
		print('Feito!')


if __name__ == "__main__":
    Programa()