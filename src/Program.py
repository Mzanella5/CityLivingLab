from ast import arg
from inspect import ArgSpec
import PySimpleGUI as sg
import sys

from Services.DataManager import DataManager 

class Program():
	def __init__(self):
		self.StartWindow()

	def StartWindow(self):
		municipio = 'Carlos Barbosa'
		dimencao = 'Intelig'
		indicador = 'IFDM'
		args = sys.argv
		print(args)
		path = args[1]
		args.remove(args[0])
		args.remove(args[0])
		print(args)
		string = ''
		for s in sys.argv:
			if string == '':
				string = s
			else:
				string += f' {s}'
		indicators = string.split(',')
		print(indicators)
		dm = DataManager(indicators)
		dm.ReadFile(path)

if __name__ == "__main__":
	Program()