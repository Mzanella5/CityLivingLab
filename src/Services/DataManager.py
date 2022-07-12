from itertools import count
from operator import index
from this import d
from turtle import st
from pandas import DataFrame
import pandas as pd

from Services.Exporter import Exporter
from Services.Importer import Importer


class DataManager():
    def __init__(self):
        pass

    def Find(self, dataFrame:DataFrame, searchString:str, columnName:str=None):
        if columnName != 'Todos':
            a = dataFrame[columnName].str.contains(searchString, case=False)
            return dataFrame.loc[a]

        max = 0
        coll = None
        for column in dataFrame.columns:
            cc = dataFrame[column].str.contains(searchString, case=False)
            c = self.CountB(self, cc)
            if c >= max:
                max = c
                coll = cc


        return dataFrame.loc[coll]

    def CountB(self, li:list):
        count = 0
        for l in li:
            if l:
                count=+1
        return count

    def DoAll(self, path:str):
        extencao = path.split('.')
        extencao = extencao[ len(extencao)-1]
        if extencao == 'csv':
            dados = Importer.ImportAsCSV(path=path)
            dados = self.StrangerFind(dados)
            Exporter.ExportAsCSV(dados)
            print('\nGerado de:' + path + '\n')
        elif extencao == 'pdf':
            dados = Importer.ImportAsPDF(path=path)
            dados = self.StrangerFind(dados)
            Exporter.ExportAsCSV(dados[0])
            print('\nGerado de:' + path + '\n')
        elif extencao == 'json':
            dados = Importer.ImportAsJSON(path=path)
            dados = self.StrangerFind(dados)
            Exporter.ExportAsCSV(dados)
            print('\nGerado de:' + path + '\n')
        elif path.startswith("http://",0,7) or path.startswith("https://",0,8):
            dados = Importer.ImportAsHTML(path)
            dados = self.StrangerFind(dados)
            Exporter.ExportAsCSV(dados)
            print('\nGerado de:' + path + '\n')
        else:
            print('Formato não suportado')

    def ReadFile(self, paths:str):

        path = str(paths)

        extencao = path.split('.')
        extencao = extencao[ len(extencao)-1]
        if path.startswith('https://',0,8):
            extencao = 'https:'
        if path.startswith('http://',0,7):
            extencao = 'http:'
        if path.startswith('www.',0,4):
            extencao = 'www.'
        match extencao:
            case 'csv':
                dados = Importer.ImportAsCSV(path=path)
                print('\nImportado de:' + path + '\n')
                return dados
            case 'xlsx':
                dados = Importer.ImportAsExel(path=path)
                print('\nImportado de:' + path + '\n')
                return dados
            case 'pdf':
                dados = Importer.ImportAsPDF(path=path)
                print('\nImportado de:' + path + '\n')
                return dados
            case 'json':
                dados = Importer.ImportAsJSON(path=path)
                print('\nImportado de:' + path + '\n')
                return dados
            case 'https:':
                print(path)
                dados = Importer.ImportAsHTML(path)
                print('\nImportado de:' + path + '\n')
                return dados
            case 'http:':
                dados = Importer.ImportAsHTML(path)
                print('\nImportado de:' + path + '\n')
                return dados
            case 'www.':
                dados = Importer.ImportAsHTML(path)
                print('\nImportado de:' + path + '\n')
                return dados
            case _: 
                print('Formato não suportado')
                return None

    def WriteFile(self, dataFrame: DataFrame):
            Exporter.ExportAsCSV(dataFrame)
            print('Exportado out.csv')
    
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
