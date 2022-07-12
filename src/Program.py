from ast import arg
from inspect import ArgSpec
import PySimpleGUI as sg
import sys
from FirstWindow import FirstWindow

from Services.DataManager import DataManager 

class Program():
	def __init__(self):
		self.StartWindow()

	def StartWindow(self):
		FirstWindow()

if __name__ == "__main__":
	Program()