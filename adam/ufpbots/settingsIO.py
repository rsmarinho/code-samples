from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

import comm
import adamApp as adam

class settingsIO(adam.adamApp):
	apps = {'Settings':'settingsIO',
			'Page 01':'page01'}

	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self.controller = controller

		self.showScreen('Settings')

	def page01(self, p):
		label = Label(p, text="page 01")
		label.pack(side=TOP, fill=BOTH)

		return 1
