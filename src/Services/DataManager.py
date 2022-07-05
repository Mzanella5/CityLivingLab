from operator import index
from this import d
from turtle import st
from pandas import DataFrame
import pandas as pd

from Services.Exporter import Exporter
from Services.Importer import Importer


class DataManager():
    def __init__(self, indicators:list):
        self.indicators = indicators

    def Find(self, dataFrame:DataFrame):
        value = self.indicators
        columns = dataFrame.columns
        query = ''
        for i in range(0,len(value)):
            if(query == ''):
                query += f"'{value[i]}' <= {columns[i]} <= '{value[i]}~'"
            else:
                query += f" and '{value[i]}' <= {columns[i]} <= '{value[i]}~'"

        return dataFrame.query(query)
    
    def ReadFile(self, path:str):
        extencao = path.split('.')
        extencao = extencao[ len(extencao)-1]
        if extencao == 'csv':
            dados = Importer.ImportAsCSV(path=path)
            dados = self.Find(dados)
            Exporter.ExportAsCSV(dados)
            print('\nGerado de:' + path + '\n')
        elif extencao == 'pdf':
            dados = Importer.ImportAsPDF(path=path)
            dados = self.Find(dados)
            Exporter.ExportAsCSV(dados[0])
            print('\nGerado de:' + path + '\n')
        elif extencao == 'json':
            dados = Importer.ImportAsJSON(path=path)
            dados = self.Find(dados)
            Exporter.ExportAsCSV(dados)
            print('\nGerado de:' + path + '\n')
        elif path.startswith("http://",0,7) or path.startswith("https://",0,8):
            dados = Importer.ImportAsHTML(path)
            dados = self.Find(dados)
            Exporter.ExportAsCSV(dados)
            print('\nGerado de:' + path + '\n')
        else:
            print('Formato não suportado')
    
    def RepeatRows(self, dataFrame: DataFrame, columnName:str):
        z = 0
        while z < len(dataFrame):
            serie = dataFrame[z]
            if len(serie <= 1):
                z += 1
                continue
            listCels:list = []
            celName = ''
            count = 0

            for cel in serie[columnName]:
                if not pd.isna(cel):
                    if len(celName) > 0:
                        celName = f'{celName} {cel}'
                    else:
                        celName = cel
                else:
                    if celName != '':
                        n = len(listCels)
                        if n > 0:
                            listCels[n-1][1] = count        
                            count = 0
                        listCels.append([celName, count])
                        celName = ''

                count += 1
            listCels[len(listCels)-1][1] = count

            list = []
            for cel in listCels:
                for i in range(0,cel[1]):
                    list.append(cel[0])

            serie.update({columnName:list})
            z += 1
