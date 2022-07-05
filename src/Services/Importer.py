import tabula
import pandas as pd

class Importer():

	def ImportAsCSV(path:str):
		return pd.read_csv(filepath_or_buffer=path)

	def ImportAsHTML(url:str):
		return pd.read_html(url)[0]

	def ImportAsPDF(path:str):
		return tabula.read_pdf(input_path=path, pages='all')

	def ImportAsJSON(path:str):
		return pd.read_json(path)