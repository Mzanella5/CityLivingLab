import pandas as pd
import json

class Exportador():
	def __init__(self):
		pass

	def ExportarComoJson(self, dados: pd.DataFrame):
		dic = dados.to_dict('records')
		string = json.dumps(dic, ensure_ascii=False)
		f = open("../out.json", "w")
		f.write(string)
		f.close()