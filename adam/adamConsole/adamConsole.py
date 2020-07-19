from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

import adamApp as adam

class adamConsole(adam.adamApp):
	apps = {'Console':'adamConsole'}

	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self.controller = controller

		self.showScreen('Console')

	def page01(self, parent):

		return 1
