from operator import le
from traceback import print_tb
from typing import Dict
import PySimpleGUI as sg
from click import edit
from numpy import column_stack, size
from requests import patch
from traitlets import default
import pandas as pd
from MainWindow import MainWindow
from Services.DataManager import DataManager

class FirstWindow:
    def __init__(self) -> None:
        dm = DataManager()
        sg.theme('Dark Grey 13')

        layout = [[sg.Text('Filename')],
                [sg.Input(enable_events=True, key='InputPath'), sg.FileBrowse(), sg.Button('Abrir')],
                ],
                
        window = sg.Window('City Living Lab', layout, resizable=True)

        while True:
            event, values = window.read()
            match event:
                case None:
                    break
                case 'Abrir':
                    print( f'Event called: {event}')
                    path:str = values['InputPath']

                    if len(path) == 0:
                        print('Alert: Path empty or invalid')
                    else:
                        dataFrame:pd.DataFrame  = dm.ReadFile(path)
                        fileName = path.split('/')
                        fileName = fileName[ len(fileName)-1]
                        MainWindow(f'City Living Lab - {fileName}', dataFrame).start()
                case _:
                    print(str(event)+' | '+ str(values))

        window.close()