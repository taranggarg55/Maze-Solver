from collections import deque

def start(myTurtle, walls, finish, cellWidth, maze):
	maze.color('grey')										# set the color of search square as grey
	q = deque()												# create a double ended queue
	visited = []											# create a list to store nodes which are visited
	x = myTurtle.xcor()										# current x location
	y = myTurtle.ycor()										# current y location
	path = {(x,y):None}										# create a dict to store path, key = current location, value = parent location
	q.append((x,y))											# put starting node in the queue
	while (len(q)!=0):										# loop until queue is empty 

		x,y = q.popleft()									# get the first element in the queue
		for cell in [(x-cellWidth,y), (x+cellWidth,y), (x,y+cellWidth), (x,y-cellWidth)]: # left, right, up, down
			if(cell not in walls and cell not in visited):  # if neighbour cell is not wall and is not visited 
				q.append(cell)								# put it in the queue
				path[cell] = (x,y)							# put in the path dict with parent
				if(cell not in finish):						# if neighbour is not target
					maze.goto(cell)							# move there
					maze.stamp()							# put a stamp
		
		visited.append((x,y))								# append current node in the visited list
	
	finalPath = [finish[0]]									# list containing the final path
	source = finish[0]										# using backtack so set source as final point
	while(source!=None):									# loop until source is None
		finalPath.append(source)							# put in finalPath list
		source = path[source]								# change soure to parent

	myTurtle.shape('circle')								# set the shape of turtle as circle 
	myTurtle.showturtle()									# make the turtle visible
	myTurtle.pensize(2)										# set the pen width as 2

	for i in range (len(finalPath)-1, -1, -1):				# loop through finalPath in reverse order
		x,y = finalPath[i][0], finalPath[i][1]				
		myTurtle.goto(x, y)									# goto the position
	