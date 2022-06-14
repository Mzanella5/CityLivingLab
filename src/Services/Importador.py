import tabula
import pandas as pd

class Importador():
	def __init__(self):
		self.delimiter = ';'

	def ImportarComoCsv(self, path:str):
		return pd.read_csv(filepath_or_buffer=path, delimiter=';', encoding ='latin1')

	def ImportarComoHtml(self, url:str):
		return pd.read_html(url)[0]

	def ImportarComoPdf(self, path:str):
		return tabula.read_pdf(input_path=path, pages='all')