from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

import adamApp as adam

from  serial.tools import list_ports
import threading
import time

import cv2
import PIL
from PIL import Image,ImageTk

import threading
import datetime

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ufpbots(adam.adamApp):
	apps = {'UFPBots':'ufpbots',
			# 'Setup':'setup',
			'Motor Test':'motorTest',
			'Camera Setup':'camera'}

	def __init__(self, parent, controller):
		super().__init__(parent, controller)
		self.controller = controller

		self.showScreen('UFPBots')

	def setup(self, p):
		a = ufpbots_setup(p, p)

	def motorTest(self, p):
		label = Label(p, text="motorTest screen")
		label.pack(side=TOP, fill=BOTH)
		return 1

	def camera(self, p):
		a = camera_settings(p, p)

class camera_settings:
	def __init__(self, parent, controller):
		self.cap = cv2.VideoCapture(0)
		self.newimg = self.cap.read()

		self.gamma  = DoubleVar()
		self.bright  = DoubleVar()
		self.contrast = DoubleVar()

		self.gamma.set(1)
		self.bright.set(0)
		self.contrast.set(1)


		self.redMin = IntVar()
		self.redMax = IntVar()
		self.greenMin = IntVar()
		self.greenMax = IntVar()
		self.blueMin = IntVar()
		self.blueMax = IntVar()

		self.redMin.set(10)
		self.redMax.set(245)
		self.greenMin.set(10)
		self.greenMax.set(245)
		self.blueMin.set(10)
		self.blueMax.set(245)

		self.parent = parent
		self.controller = controller

		self.test = True

		#######################

		self.leftFrame = Frame(parent)
		self.leftFrame.pack(side=LEFT, fill=BOTH)

		self.videoPrint = LabelFrame(self.leftFrame, text="Actual Camera Video", borderwidth=1, relief="groove")
		self.videoPrint.pack(side=TOP, fill=X)

		self.cameraFrame = Label(self.videoPrint)
		self.cameraFrame.pack(side=TOP, fill=X)
		# self.videoLoop()

		self.stopEvent = threading.Event()
		self.thread = threading.Thread(target=self.videoLoop, args=())
		self.thread.start()

		#######################

		self.videoDefinitions = LabelFrame(self.leftFrame, text="Video Control", borderwidth=1, relief="groove")
		self.videoDefinitions.pack(side=TOP, fill=BOTH, expand=1)

		#######################

		label2 = LabelFrame(self.videoDefinitions, text="Gamma")
		label2.pack(side=TOP, fill=BOTH)

		self.w = Scale(label2, variable = self.gamma, from_=0.00001, to=4.0)
		self.w.pack(side=TOP, fill=BOTH)

		#######################

		label3 = LabelFrame(self.videoDefinitions, text="Brightness")
		label3.pack(side=TOP, fill=BOTH)

		self.w1 = Scale(label3, variable = self.bright, from_=-200.0, to=200.0)
		self.w1.pack(side=TOP, fill=BOTH)

		#######################

		label4 = LabelFrame(self.videoDefinitions, text="Contrast")
		label4.pack(side=TOP, fill=BOTH)

		w2 = Scale(label4, variable = self.contrast, from_=0.0, to=3.0)
		w2.pack(side=TOP, fill=BOTH)

		####################### Color definitions

		self.rightFrame = Frame(parent)
		self.rightFrame.pack(side=LEFT, fill=BOTH, expand=1)

		self.colorLimiar = LabelFrame(self.rightFrame, text="Color Limiar Configuration", borderwidth=1, relief="groove")
		self.colorLimiar.pack(side=TOP, fill=BOTH, expand=1)

		note = Notebook(self.colorLimiar)

		tab1 = Frame(note)
		tab2 = Frame(note)
		tab3 = Frame(note)

		note.add(tab1, text = "red")

		self.redFrame = Frame(tab1)
		self.redFrame.pack(side=TOP, fill=BOTH)

		self.videoRed = LabelFrame(self.redFrame, text="Red Color Thresholding", borderwidth=1, relief="groove")
		self.videoRed.pack(side=TOP, fill=X)

		self.RedColor = Label(self.videoRed)
		self.RedColor.pack(side=TOP, fill=X)
		#thread
		self.stopEvent1 = threading.Event()
		self.thread1 = threading.Thread(target=self.videoRedColor, args=())
		self.thread1.start()

		#######################

		self.RedDefinitions = LabelFrame(self.redFrame, text="Video Control", borderwidth=1, relief="groove")
		self.RedDefinitions.pack(side=TOP, fill=BOTH)

		#######################

		self.redLabel = Label(self.RedDefinitions, text="Red")
		self.redLabel.pack(side=TOP, fill=BOTH)

		self.RedDefinitions = LabelFrame(self.redLabel, text="Minimum", borderwidth=1, relief="groove")
		self.RedDefinitions.pack(side=TOP, fill=BOTH)

		self.redThresholdMin = Scale(self.RedDefinitions, variable = self.redMin, from_=0, to=self.redMax.get(), orient=HORIZONTAL)
		self.redThresholdMin.pack(side=TOP, fill=BOTH)

		self.RedDefinitions = LabelFrame(self.redLabel, text="Maximum", borderwidth=1, relief="groove")
		self.RedDefinitions.pack(side=TOP, fill=BOTH)

		self.redThresholdMax = Scale(self.RedDefinitions, variable = self.redMax, from_=self.redMin.get(), to=255, orient=HORIZONTAL)
		self.redThresholdMax.pack(side=TOP, fill=BOTH)

		self.redLabel = Label(self.RedDefinitions, text="Green")
		self.redLabel.pack(side=TOP, fill=BOTH)

		self.RedDefinitions = LabelFrame(self.redLabel, text="Minimum", borderwidth=1, relief="groove")
		self.RedDefinitions.pack(side=TOP, fill=BOTH)

		self.redThresholdMin = Scale(self.RedDefinitions, variable = self.greenMin, from_=0, to=self.greenMax.get(), orient=HORIZONTAL)
		self.redThresholdMin.pack(side=TOP, fill=BOTH)

		self.RedDefinitions = LabelFrame(self.redLabel, text="Maximum", borderwidth=1, relief="groove")
		self.RedDefinitions.pack(side=TOP, fill=BOTH)

		self.redThresholdMax = Scale(self.RedDefinitions, variable = self.greenMax, from_=self.greenMin.get(), to=255, orient=HORIZONTAL)
		self.redThresholdMax.pack(side=TOP, fill=BOTH)

		self.redLabel = Label(self.RedDefinitions, text="Blue")
		self.redLabel.pack(side=TOP, fill=BOTH)

		self.RedDefinitions = LabelFrame(self.redLabel, text="Minimum", borderwidth=1, relief="groove")
		self.RedDefinitions.pack(side=TOP, fill=BOTH)

		self.redThresholdMin = Scale(self.RedDefinitions, variable = self.blueMin, from_=0, to=self.blueMax.get(), orient=HORIZONTAL)
		self.redThresholdMin.pack(side=TOP, fill=BOTH)

		self.RedDefinitions = LabelFrame(self.redLabel, text="Maximum", borderwidth=1, relief="groove")
		self.RedDefinitions.pack(side=TOP, fill=BOTH)

		self.redThresholdMax = Scale(self.RedDefinitions, variable = self.blueMax, from_=self.blueMin.get(), to=255, orient=HORIZONTAL)
		self.redThresholdMax.pack(side=TOP, fill=BOTH)

		note.add(tab2, text = "green")
		note.add(tab3, text = "blue")

		f = plt.Figure(figsize=(5,5), dpi=100)
		a = f.add_subplot(111)

		canvas = FigureCanvasTkAgg(f, tab3)
		canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
		a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

		note.pack(side=TOP, fill=BOTH, expand=1)

	def adjust_gamma(self):
		# build a lookup table mapping the pixel values [0, 255] to
		# their adjusted gamma values

		# print(self.gamma.get())
		invGamma = 1.0/self.gamma.get()
		table = np.array([((i / 255.0) ** invGamma) * 255
		    for i in np.arange(0, 256)]).astype("uint8")

		# apply gamma correction using the lookup table
		self.newimg = cv2.LUT(self.frame, table)

	def adjustImage(self):
		# for c in range(0,self.frame.shape[2]): newimg[:,:,c] = np.clip((self.frame[:,:,c]) + self.w.get(), 0, 255)
		self.adjust_gamma()
		self.newimg = cv2.convertScaleAbs(self.newimg, alpha=self.contrast.get(), beta=self.bright.get())

	def getFrameFromCamera(self, c):
		_, self.frame = c.read()
		self.frame = cv2.flip(self.frame, 1)

	def videoLoop(self):
		if self.test == True:
			self.getFrameFromCamera(self.cap)
			self.adjustImage()

			self.newimg = cv2.cvtColor(self.imgScaleToWindow(self.newimg), cv2.COLOR_BGR2RGBA)
			imgtk = Image.fromarray(self.newimg)
			imgtk = ImageTk.PhotoImage(imgtk)
			self.cameraFrame.imgtk = imgtk
			self.cameraFrame.configure(image=imgtk)
			self.test = False
		self.cameraFrame.after(15, self.videoLoop)

	def videoRedColor(self):
		if self.test == False:
			# img = cv2.cvtColor(self.newimg, cv2.COLOR_BGR2GRAY)
			# _, limiar = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
			img = cv2.cvtColor(self.newimg, cv2.COLOR_BGR2HSV)

			self.lowerRed = (self.redMin.get(), self.greenMin.get(), self.blueMin.get())
			self.upperRed = (self.redMax.get(), self.greenMax.get(), self.blueMax.get())

			# construct a mask for the color "red", then perform
			# a series of dilations and erosions to remove any small
			# blobs left in the mask
			mask = cv2.inRange(img, self.lowerRed , self.upperRed)
			mask = cv2.erode(mask, None, iterations=2)
			mask = cv2.dilate(mask, None, iterations=2)

			imgtk = Image.fromarray(mask)
			imgtk = ImageTk.PhotoImage(imgtk)
			self.RedColor.imgtk = imgtk
			self.RedColor.configure(image=imgtk)
			self.test = True
		self.RedColor.after(20, self.videoRedColor)
		# cv2.imwrite("image.jpg",limiar);

	def imgScaleToWindow(self, f):
		# self.cameraFrame.update()
		# self.W = self.cameraFrame.winfo_width()
		# self.H = self.videoPrint.winfo_height()

		# height, width, depth = f.shape
		# imgScale = self.W/width
		# newX,newY = f.shape[1]*imgScale, f.shape[0]*imgScale

		# Atenção para não fazer a escolha dos pontos nem nenhum tipo de
		# processamento com a imagem escalada. Utilizar sempre a imagem
		# original para os processamentos. A imagem escalada deve servir
		# apenas para o plot em tela

		# frame = cv2.resize(frame,(int(newX),int(newY)), interpolation = cv2.INTER_CUBIC)
		# frame = cv2.resize(frame,(int(newX),int(newY)), interpolation = cv2.INTER_LINEAR)
		# return cv2.resize(f,(int(newX),int(newY)), interpolation = cv2.INTER_AREA)
		return cv2.resize(f, None, fx=0.8, fy=0.8, interpolation = cv2.INTER_AREA)

# ufpbot model classes
class ufpbots_setup:
	def __init__(self, parent, controller):
		self.parent = parent
		self.controller = controller

		self.ports = []
		self.tlock = threading.Lock()

		# self.t1 = threading.Thread(target=self.list_ports)
		# self.t1.daemon = True
		# self.t1.start()

		self.t2 = threading.Thread(target=self.serial_comm)
		self.t2.daemon = True
		self.t2.start()

		# self.t3 = threading.Thread(target=self.serial_choose)
		# self.t3.daemon = True
		# self.t3.start()

		self.ports = ['None']
		self.port = self.ports[0]
		self.var = StringVar()

		self.option = OptionMenu(self.parent, self.var, self.ports)
		self.option.pack()


	def serial_choose(self):
		while True:
			self.tlock.acquire()
			try:
				self.port = self.option.focus()
				self.var.set(self.port)
			finally:
				self.tlock.release()
			time.sleep(0.5)

	def serial_comm(self):

		oldlist = self.ports
		while True:
			self.tlock.acquire()
			self.ports = sorted([port.device for port in list_ports.comports()])
			try:
				if self.ports == oldlist:
					# self.port = self.option.focus()
					pass
				elif self.ports != oldlist:
					m = self.option['menu']
					m.delete(0, END)
					for val in self.ports:
					    m.add_command(label=val, command=lambda v=self.var,l=val:v.set(l))
					pass
				elif self.option.focus():
					self.port = self.option.focus()
			finally:
				self.tlock.release()
			time.sleep(0.5)

	def list_ports(self):
		while True:
			self.tlock.acquire()
			try:
				self.ports = sorted([port.device for port in list_ports.comports()])
				# print('t1: ')
			finally:
				self.tlock.release()
			time.sleep(0.5)
