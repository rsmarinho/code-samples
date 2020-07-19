from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

import adamApp as adam

class dummyEntry(adam.adamApp):
	apps = {'DummyEntry' : 'dummyEntry',
			'Page 01' : 'page01',
			'Page 02' : 'page02',
			'Page 03' : 'page03'}

	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self.controller = controller

		self.showScreen('DummyEntry')

	def page01(self, p):
		label = Label(p, text="page 01")
		label.pack(side=TOP, fill=BOTH)

		return 1

	def page02(self, p):
		label = Label(p, text="page 02")
		label.pack(side=TOP, fill=BOTH)

		return 1

	def page03(self, p):
		label = Label(p, text="page 03")
		label.pack(side=TOP, fill=BOTH)

		return 1
