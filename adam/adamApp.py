from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

class adamApp(Frame, object):
	#apps = {'adam':'adam'}

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller = controller

		if len(self.apps) > 1:
			self.tabs = Notebook(self)
			self.nb = {}
			for tab in self.apps.keys():
				if tab != list(self.apps.keys())[0]:
					self.nb[tab] = Frame(self.tabs)
					self.tabs.add(self.nb[tab], text="{}".format(tab))
			self.tabs.pack(side=TOP, fill=BOTH, expand=1)
			self.tabs.enable_traversal()

		self.appFrames = {}
		for F in self.apps.keys():
			if F != list(self.apps.keys())[0]:
				fr = self.createScreen(self.apps[F], self, controller)
				fr.config(text=F)
				self.appFrames[F] = fr
			else:
				self.appFrames[F] = self

	@staticmethod
	def getNames(self):
		return self.apps

	def showScreen(self, s):
		for F in self.appFrames.keys():
			#print("showScreen::forget: ", self.appFrames[F])
			self.appFrames[F].pack_forget()
		if len(self.apps) == 1:
			self.appFrames[s].grid()
		# root case
		elif s == list(self.apps.keys())[0]:
			self.tabs.pack(side=TOP, fill=BOTH, expand=1)
			ll = set(self.appFrames.keys()).difference(set([s]))
			for k in ll:
				self.appFrames[k].pack(side=TOP, fill=BOTH, expand=1, in_=self.nb[k])
		# not root case
		else:
			self.tabs.pack_forget()
			self.appFrames[s].pack(side=TOP, fill=BOTH, expand=1)
		#print("showScreen::update: ", self.appFrames[s])
		self.update()

	def createScreen(self, s, parent, controller):
		frameScreen = LabelFrame(parent)
		frameScreen.pack(side=TOP, fill=BOTH, expand=1)

		if s != self.apps[list(self.apps.keys())[0]]:
			eval('self.' + s + '(frameScreen)')

		return frameScreen
