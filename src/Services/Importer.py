import tabula
import pandas as pd

class Importer():

	def ImportAsCSV(path:str):
		df = pd.read_csv(filepath_or_buffer=path)
		for column in df.columns:
			df[column] = df[column].map(str)
		return df

	def ImportAsExel(path:str):
		df = pd.read_excel(path)
		for column in df.columns:
			df[column] = df[column].map(str)
		return df

	def ImportAsHTML(url:str):
		df = pd.read_html(url)[0]
		for column in df.columns:
			df[column] = df[column].map(str)
		return df

	def ImportAsPDF(path:str):
		listDf = tabula.read_pdf(input_path=path, pages='all')
		dataframe = listDf[39]

		for df in listDf:
			dataframe = dataframe.append(df, ignore_index=True)

		for column in dataframe.columns:
			dataframe.loc[column] = dataframe[column].map(str)

		return dataframe

	def ImportAsJSON(path:str):
		df = pd.read_json(path)
		for column in df.columns:
			df[column] = df[column].map(str)
		return df
