import string
from turtle import st
import pandas as pd

class Importador():
	def __init__(self):
		self.delimiter = ';'

	def ImportarComoCsv(self):
		data = pd.read_csv('../pessoal.csv', delimiter=';', encoding ='latin1')
		return data

	def ImportarComoHtml(self, url:string):
		return pd.read_html(url)