#global libraries
import turtle                    
import Tkinter as tk

# user libraries 
import maze_generator
import LHR
import RHR
import randomMouse
import dfs1
import dfs2
import bfs
import deadendFilling
import aStar


#driver function which helps in setting up maze and calling respective algorthim function
def start(width, height, lastMaze, speed, algo):

	maze_color = 'white'
	bg_color = 'black'

	def setupMaze(grid):
		for y in range(len(grid)):                       # loop through all the elements in the list(maze)
			for x in range(len(grid[y])):                
				character = grid[y][x]                   
				screen_x = -588 + (x * cellWidth)		 # calculate the position of x coordinate
				screen_y = 288 - (y * cellWidth)         # calculate the position of y coordinate

				if character == "+":                     # if wall
					maze.goto(screen_x, screen_y)        # go to location 
					maze.stamp() 						 # put stamp (make wall)
					walls.append((screen_x, screen_y))   # append in walls list

				elif character == "e":                   # if end point (target/goal)
					maze.goto(screen_x, screen_y)        # goto location
					maze.color('green')					 # make color green
					maze.stamp()						 # put stamp
					maze.color(maze_color)               # switch back to wall color
					finish.append((screen_x, screen_y))  # append in finish list

		
	grid = maze_generator.createMaze(width, height, lastMaze) # generate a maze with given width and height 
	cellWidth = row = int(  min(  700.0 / (len(grid)*1.1), 1300.0 / (len(grid[0])*1.05)  ) ) # calculate the width of each cell to fit the maze properly on screen 

	window = tk.Tk() 										# create a tkinter window
	window.title("Maze-Solver")								# put title
	window.geometry('1300x700')								# set dimension
	window.resizable(False, False)							# make it non resizeable
	wn = turtle.Canvas(window, width=1300, height=700)		# take turtle canvas
	wn.place(x=0, y=0)										# pin the canvas on the window


	maze = turtle.RawTurtle(wn)								# create a turtle object for maze
	wn['bg'] = bg_color										# set background color
	maze.shape('square')									# set shape of wall as sqaure
	maze.penup()											# put penup (no trail)
	maze.color(maze_color)									# set wall color
	maze.speed(0) # fastest									# set speed to draw maze as fastest(0)
	maze.shapesize(cellWidth/24.0)							# set the size of each cell
	maze.hideturtle()										# hide the maze turtle


	walls =[]                    							# list to store walls
	finish = []  											# list to store the end point
	setupMaze(grid)											# create the maze
	maze.speed(speed)										# set the speed given by the user
	maze.hideturtle()										# hide 

	myTurtle = turtle.RawTurtle(wn)							# create a turtle object for mover(solver)
	myTurtle.shape('turtle')								# set its shape
	myTurtle.hideturtle()									# hide the turtle
	myTurtle.color('red')									# set its color as red
	myTurtle.speed(0)										# set its speed to fastest(0)
	myTurtle.penup()										# put pen up initially (no trail)
	myTurtle.shapesize(cellWidth/24.0)						# set the size of each cell
	myTurtle.goto(-588+cellWidth, 288-cellWidth)			# move the turtle to the starting position
	myTurtle.speed(speed)									# set the speed to user given speed
	myTurtle.pendown()										# put the pen down (for trail)

	# call apt function as per the given algo
	if(algo == 'Left Hand Rule'):
		LHR.start(myTurtle, walls, finish, cellWidth)
	elif(algo == 'Right Hand Rule'):
		RHR.start(myTurtle, walls, finish, cellWidth)
	elif(algo == 'Random Mouse'):
		randomMouse.start(myTurtle, walls, finish, cellWidth)
	elif(algo == 'Depth First Search - 1'):
		dfs1.start(myTurtle, walls, finish, cellWidth)
	elif(algo == 'Depth First Search - 2')	:
		dfs2.start(myTurtle, walls, finish, cellWidth, maze)
	elif(algo == 'Breadth First Search'):
		bfs.start(myTurtle, walls, finish, cellWidth, maze)
	elif(algo == 'Dead-End Filling'):
		deadendFilling.start(myTurtle, walls, finish, cellWidth, maze)
	elif(algo == 'A* Search'):
		aStar.start(myTurtle, walls, finish, cellWidth, maze)
	window.mainloop() # prevents program from quiting 

# start(10,10,False,5,'A* Search') # used for faster debugging