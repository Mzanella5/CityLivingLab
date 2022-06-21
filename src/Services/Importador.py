import tabula
import pandas as pd

class Importador():

	def ImportarComoCsv(path:str):
		return pd.read_csv(filepath_or_buffer=path, delimiter=';', encoding ='latin1')

	def ImportarComoHtml(url:str):
		return pd.read_html(url)[0]

	def ImportarComoPdf(path:str):
		return tabula.read_pdf(input_path=path, pages='all')