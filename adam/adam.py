from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

from about import about

import re
is_comment = re.compile("(?:\#...)")

# dev variables
set_esc_to_close = True

# apps = ['ufpbots','discharge']#, 'settingsIO', 'adamConsole', 'dummyEntry']

apps = [line.rstrip('\n') for line in open('applications.conf')if not is_comment.match(line)]
# apps = [x for x in apps if not is_comment.match(x)]

modules = {}
for x in apps:
	try:
		modules[x] = getattr(__import__(x), x)
		print("Success loading", x)
	except:
		print("Oops!", sys.exc_info()[0],"occured.")
		print("Error loading", x)

globals().update(modules)

apps_dict = {}
for i in apps:
	s = modules[i]
	m = s.getNames(s)
	apps_dict.update({i:m})

def donothing():
	print("do nothing")

def ok_event(self, event):
	print("close adam (esc)")
	self.destroy()

class startScreen(Frame):
	def __init__(self, parent, controller):
		global app_name
		app_name = 'startScreen'

		Frame.__init__(self, parent, borderwidth=1, relief="groove")
		self.controller = controller
		self.pack(fill=BOTH, expand=1)

		#label = Label(self, text="start page")
		#label.pack(side=TOP, fill=X)

	def getAppName():
		return app_name

class frontFrame(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.geometry("1365x768")

		self.call('wm', 'iconphoto', self._w, PhotoImage(file='triskell.png'))
		self.title("adam")

		self.style = ttk.Style()
		#('clam', 'alt', 'default', 'classic')
		self.style.theme_use("clam")

		self.mainFrame = Frame(self)
		self.mainFrame.pack(side="top", fill="both", expand = True)
		self.mainFrame.grid_rowconfigure(0, weight=1)
		self.mainFrame.grid_columnconfigure(0, weight=1)

		self.makeMenuBar()
		self.makeAppChooser()
		self.makeWorkScreen()
		self.showAppFrame()

		if set_esc_to_close:
			self.mainFrame.bind("<KeyRelease-Escape>", lambda event: ok_event(self, event))
			self.mainFrame.focus_set()
		# Utils

	def makeMenuBar(self):
		# Menubar
		menubar = Menu(self)

		# Menus and Submenus
		filemenu = Menu(menubar, tearoff=0)
		helpmenu = Menu(menubar, tearoff=0)

		# Menu commands and subcommands
		menubar.add_cascade(label="File", menu=filemenu)
		menubar.add_cascade(label="Help", menu=helpmenu)

		# File Menus
		filemenu.add_command(label="Exit", command=self.quit)

		helpmenu.add_command(label="Help Index", command=donothing)
		helpmenu.add_command(label="About...", command = lambda: about(self))

		# Put menubar on frame
		self.config(menu=menubar)

	def makeWorkScreen(self):
		screen = Frame(self.mainFrame)
		screen.pack(side=LEFT, fill=BOTH, expand=1)
		screen.grid_rowconfigure(0, weight=1)
		screen.grid_columnconfigure(0, weight=1)

		self.appFrames = {}
		self.appFrames['startScreen'] = startScreen(screen, self)
		self.appFrames['startScreen'].grid(row=0, column=0, sticky=W+E+N+S)

		for F in apps_dict.keys():
			func = globals()[F]
			fr = func(screen, self)
			fr.grid(row=0, column=0, sticky=W+E+N+S)
			self.appFrames[list(apps_dict[F].keys())[0]] = fr

		self.screenFrame = self.appFrames['startScreen']

	def makeAppChooser(self):
		screen = Frame(self.mainFrame, borderwidth=1, relief="groove")
		screen.pack(side=LEFT, fill=Y, expand=0)

		self.tree = ttk.Treeview(screen)
		# insert format -> insert(parent, index, iid=None, **kw)
		# reference: https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview

		# Create menu from (global) apps variable
		for F in apps_dict.keys():
			for S in apps_dict[F].keys():
				if F != apps_dict[F][S]:
					self.tree.insert(aux, 'end', text=S, values=apps_dict[F][S])
				else:
					self.tree.insert('', 'end', S, text=S, values=apps_dict[F][S])
					aux = S

		self.tree.bind("<ButtonRelease-1>", lambda event, t = self.tree: self.OnSingleClickL(event, t))
		#self.tree.bind("<Double-1>", lambda event, t = self.tree: self.OnDoubleClickL(event, t))

		self.tree.pack(side=TOP, fill=Y, expand=True)

	def OnSingleClickL(self, event, tree):
		item_iid = tree.selection()[0]
		parent = tree.parent(item_iid)
		if parent != '':
			p = tree.item(parent)['text']#[0]
			scr = tree.item(item_iid)['text']#[0]
			self.appFrames[p].showScreen(scr)
			self.screenFrame = self.appFrames[parent]
		else:
			self.appFrames[item_iid].showScreen(item_iid)
			self.screenFrame = self.appFrames[item_iid]
		self.showAppFrame()

	def OnDoubleClickL(self, event, tree):
		item = tree.selection()[0]
		#item = tree.focus()
		self.screenFrame = self.appFrames[appsDict[tree.item(item,"text")].__name__]
		self.showAppFrame()

	def showAppFrame(self):
		self.screenFrame.tkraise()

def main():
	try:
		app = frontFrame()
		app.mainloop()
		# app.style = Style()
		# #('clam', 'alt', 'default', 'classic')
		# app.style.theme_use("clam")
	except KeyboardInterrupt:
		print('close')

if __name__ == '__main__':
	main()
