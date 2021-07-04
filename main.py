from tkinter import *
from tkinter.ttk import Combobox
import random

import driver


class Menu:
	def __init__(self, win):
		self.lb_algo = Label(win, text="Algorithm")
		self.lb_algo.place(x=70,y=50)

		self.algoDefault = StringVar()
		self.algoDefault.set('A* Search')
		self.algoList = ['A* Search', 'Depth First Search - 1', 'Depth First Search - 2', 'Breadth First Search', 'Dead-End Filling', 'Left Hand Rule', 'Right Hand Rule', 'Random Mouse']
		self.algo=Combobox(win, values=self.algoList, text=self.algoDefault)
		self.algo.place(x=150, y=50)
		
		self.lb_rows = Label(win, text="Rows")
		self.lb_cols = Label(win, text="Cols")
		self.lb_rows.place(x=10,y=100)
		self.lb_cols.place(x=10,y=150)

		self.cols=Entry()
		self.rows=Entry()
		self.rows.place(x=50, y=150)
		self.cols.place(x=50, y=100)

		self.lb_or = Label(win, text="OR")
		self.lb_or.place(x=240, y=125)

		self.lastMazeVar = IntVar()
		self.lastMaze = Checkbutton(window, text = "Last Maze", variable = self.lastMazeVar)
		self.lastMaze.place(x=275, y=125)

		self.lb_speed = Label(win, text="Speed")
		self.lb_speed.place(x=70, y=200)
		
		self.speedDefault = StringVar()
		self.speedDefault.set("Normal")
		self.speed=Combobox(win, values=['Slowest', 'Slow', 'Normal', 'Fast', 'Fastest'], text=self.speedDefault)
		self.speed.place(x=150, y=200)
		
		self.b1=Button(win, text='Visualize', command=self.visualize)
		self.b1.place(x=150, y=250)
	

	def visualize(self):
		algo = self.algo.get()
		rows = self.rows.get()
		lastMaze = self.lastMazeVar.get()
		cols = self.cols.get()
		speed = self.speed.get()

		if(rows == ''):
			rows = random.randint(10,20)*2+1
		else:
			rows = int(rows)
		
		if(cols==''):
			cols = random.randint(10,20)*2+1
		else:
			cols = int(cols)

		if(speed == ''):
			speed = 5
		elif(speed == 'Slowest'):
			speed = 1
		elif(speed == 'Slow'):
			speed = 3
		elif(speed == 'Normal'):
			speed = 5
		elif(speed == 'Fast'):
			speed = 10
		elif(speed == 'Fastest'):
			speed = 0

		if(algo != ''):
			try:
				driver.start(rows, cols, lastMaze, speed, algo)
			except:
				pass
	
window=Tk()
menu=Menu(window)
window.title('Maze Settings')
window.geometry("400x500")
window.mainloop()
