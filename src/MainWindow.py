import PySimpleGUI as sg
from matplotlib.pyplot import cla
from pandas import DataFrame
from Services.DataManager import DataManager

from Services.Exporter import Exporter

class MainWindow():
    def __init__(self, windowName, dataFrame:DataFrame):
        self.windowName = windowName
        self.dataFrame = dataFrame
        self.currDataFrame = dataFrame
        self.dt = DataManager
        self.indicator = 'Todos'
        self.searchString = ''

    def start(self):
        data = self.dataFrame.values.tolist()
        layout = [[sg.Text('',key='Alert', justification='c', expand_x=True)],
                [sg.Button('Exportar CSV'), sg.Button('Exportar XLSX'), sg.Button('Exportar JSON')],
                [[sg.Text('Pesquisar em: Todos',key='Pesquisar')], sg.Input(key='InputSearch',enable_events=True)],
                [sg.Listbox(values=['Todos', *self.dataFrame.columns], expand_y=True, expand_x=True, key='Indicators', enable_events=True),
                 sg.Table(values=data, headings=[*self.dataFrame.columns],vertical_scroll_only=False, key='ThisTable', size=(50,50), expand_x=True, expand_y=True)]
                ],

        window = sg.Window(title=self.windowName, layout=layout, resizable=True, size=(1000,600))
        alert = window['Alert']
        while True:
            event, values = window.read()
            alert.update(value='')
            match event:
                case None:
                    break
                case 'Exportar JSON':
                    print( f'Event called: {event}')
                    (torf, message) = Exporter.ExportAsJson(self.currDataFrame)
                    if torf:
                        alert.update(value=message)
                case 'Exportar XLSX':
                    print( f'Event called: {event}')
                    (torf, message) = Exporter.ExportAsExel(self.currDataFrame)
                    if torf:
                        alert.update(value=message)
                case 'Exportar CSV':
                    print( f'Event called: {event}')
                    (torf, message) = Exporter.ExportAsCSV(self.currDataFrame)
                    if torf:
                        alert.update(value=message)       
                case 'InputSearch':
                    self.searchString = values[event]
                    self.currDataFrame = self.dt.Find(self.dt, self.dataFrame, self.searchString, self.indicator)
                    table = window['ThisTable']
                    table.update(values=self.currDataFrame.values.tolist())
                case 'Indicators':
                    print( f'Event called: {event}')
                    indicator = values[event].pop()
                    self.indicator = indicator
                    window['Pesquisar'].update(value=f'Pesquisar em: {indicator}')
                    self.currDataFrame = self.dt.Find(self.dt, self.dataFrame, self.searchString, self.indicator)
                    table = window['ThisTable']
                    table.update(values=self.currDataFrame.values.tolist())
                case _:
                    print(str(event)+' | '+ str(values))
            
        window.close()