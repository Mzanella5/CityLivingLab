from typing import Dict, List, Type
import pandas as pd
from pandas import DataFrame
import json

class Exporter():
	def __init__(self):
		pass

	def ExportAsJson(data:DataFrame | list[DataFrame]):
		data.to_json('out.json', force_ascii=True)
		return (True, 'JSON salvo em ./out.json')

	def ExportAsCSV(data:DataFrame | list[DataFrame]):
		data.to_csv('out.csv')
		return (True, 'CSV salvo em ./out.csv')
	
	def ExportAsExel(data:DataFrame | list[DataFrame]):
		data.to_excel('out.xlsx')
		return (True, 'XLSX salvo em ./out.xlsx')

