from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

class about(Tk):
	def __init__(self, parent):

		Frame.__init__(self, parent)
		top = self.top  = Toplevel(parent)
				
		top.geometry("400x200")
		top.resizable(0, 0)
		top.title("Sjavar")
		#top.call('wm', 'iconphoto', self._w, PhotoImage(file='sjavar.png'))
		
		fr = Frame(top)
		fr.pack(fill=BOTH, expand=1)
		fr.bind("<KeyRelease-Escape>", self.ok_event)
		fr.focus_set()
		
		texto = "Lorem ipsum dolor sit amet, consectetur adipiscing	elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"
		
		l = Label(fr, text=texto, wraplength=400)
		l.pack(fill=BOTH, expand=1)

		b = Button(fr, text="OK", command=self.ok)
		b.pack()

	def ok(self):
		print("close about (button)")
		self.top.destroy()
		
	def ok_event(self, event):
		print("close about (esc)")
		self.top.destroy()
	
