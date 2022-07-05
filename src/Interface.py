import platform
import PySimpleGUIQt as sg
from Services.DataManager import DataManager

class Listbox(sg.Listbox):

    def dragEnterEvent(self, e):
        e.accept()

    def dragMoveEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        #data = window['LISTBOX'].get_list_values()
        #print(data)
        # items = [str(v) for v in e.mimeData().text().strip().split('\n')]
        # print(items)
        # data.extend(items)
        # print(data)
        data = e.mimeData().text().strip().split('\n')
        if platform.system() == "Windows":
            data[0] = data[0].replace('file:///', '')
        else:
            data[0] = data[0].replace('file://', '')
        window['LISTBOX'].update(data)
        window.refresh()
        dataManager = DataManager()
        dataManager.ReadFile(data[0])

    def enable_drop(self):
        # Called after window finalized
        self.Widget.setAcceptDrops(True)
        self.Widget.dragEnterEvent = self.dragEnterEvent
        self.Widget.dragMoveEvent = self.dragMoveEvent
        self.Widget.dropEvent = self.dropEvent

layout = [[Listbox([], size=(50, 4), enable_events=True, key='LISTBOX')]]

window = sg.Window("Title", layout, finalize=True)
window['LISTBOX'].enable_drop()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break



window.close()