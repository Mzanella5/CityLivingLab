from typing import Dict, List, Type
import pandas as pd
from pandas import DataFrame
import json

class Exporter():
	def __init__(self):
		pass

	def ExportAsJson(data:DataFrame | list[DataFrame]):
		dic = dict()

		if isinstance(data, DataFrame):
			print('entrou')
			dic = data.to_dict('records')
		else:
			for fragmento in data:
				dic = dic | fragmento.to_dict()
			
		string = json.dumps(dic, ensure_ascii=False)
		f = open("../out.json", "w")
		f.write(string)
		f.close()

	def ExportAsCSV(data:DataFrame | list[DataFrame]):
		data.to_csv('out.csv')
