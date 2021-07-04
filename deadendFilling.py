from collections import deque


def wallCount(walls, filled, x, y, cellWidth):
	'''
		func: gives the number of walls/ untraversible cells around given cell
		inp: list of walls, list of cells which are filled, x coord of current cell, y coord of current cell, cellWidth
		out: count of neighbouring cells which are untraversible 
	'''
	left = (x-cellWidth, y) 					# left neighbour
	right = (x+cellWidth, y) 					# right neighbour
	up = (x, y+cellWidth)						# up neighbour
	down = (x, y-cellWidth)						# down neighbour

	count = 0									# set count to 0 initially
	if(left in walls or left in filled):		# check for left neighbour
		count+=1								# increase count
	if(right in walls or right in filled):		# check for right neighbour
		count+=1								# increase count
	if(up in walls or up in filled):			# check for up neighbour
		count+=1								# increase count
	if(down in walls or down in filled):		# check for down neighbour
		count+=1								# increase count
	
	return count 								# return the count

def start(myTurtle, walls, finish, cellWidth, maze):
	maze.shape('circle')						# set the shape of maze turtle as circle (will be used to mark deadend)
	maze.color('red')							# set the color as red
	maze.shapesize(cellWidth/48.0)				# set the size 
	q = deque()									# create a double ended queue
	visited = []								# list cointaing nodes which are visited
	filled = []									# list cointaing nodes which are blocked (greyed)
	deadendList = []							# list of nodes that are deadends
	x = myTurtle.xcor()							# current x coord
	y = myTurtle.ycor()							# current y coord
	q.append((x,y))								# put current coord in queue
	
	# following while loop executes bfs on the maze to look for deadends
	while (len(q)!=0):

		x,y = q.popleft()									# remove the first entry from the queue
		left = (x-cellWidth, y)								# coord of left neighbour
		right = (x+cellWidth, y)							# coord of right
		up = (x, y+cellWidth)								# coord of up neighbour
		down = (x, y-cellWidth)								# coord of down neighbour
		
		if(left not in walls and left not in visited):		# left is not a wall and has not been visited
			q.append(left)									# put in queue 
		if(right not in walls and right not in visited):	# right is not a wall and has not been visited
			q.append(right)									# put in queue
		if(up not in walls and up not in visited):			# up is not a wall and has not been visited
			q.append(up)									# put in queue
		if(down not in walls and down not in visited):		# down is not a wall and has not been visited
			q.append(down)									# put in queue
		visited.append((x,y))								# put current node in visited list 

		if(wallCount(walls, filled, x, y, cellWidth)==3 and (x,y) not in finish): # if node is covered from 3 sides and is not the final node 
			deadendList.append((x,y))						# put in the deadend list
			maze.goto(x,y)									# goto that node
			maze.stamp()									# put astemp (red circle)
			
	maze.shapesize(cellWidth/24.0)							# reset the size of the maze turtle 
	maze.shape('square')									# reset shape to square
	maze.color('grey')										# reset color to grey
	visited = []											# list of all the visited nodes
	filled = []												# list of all the filled nodes
	finish.append((myTurtle.xcor(), myTurtle.ycor())) 		# adding the starting coordinate in finish to avoid blocking it
	for i in range (len(deadendList)):						# loop through deadend list
		x,y = deadendList[i][0], deadendList[i][1]			# set x,y as node's position
		while(True):										# loop
			 
			if( wallCount(walls, filled, x, y, cellWidth)==3 and (x,y) not in finish): 	# if node covered from 3 sides and is not the final node 
				visited.append((x,y))						# put node in visited list
				filled.append((x,y))						# put node in filled list
				maze.goto(x, y)								# goto the node's position
				maze.stamp()								# put a stamp (grey square)
				
				left = (x-cellWidth, y)						# left neighbour
				right = (x+cellWidth, y)					# right neighbour
				up = (x, y+cellWidth)						# up neighbour
				down = (x, y-cellWidth)						# down neighbour
				
				if(left not in walls and left not in visited):		# check if left is traversible  
					x, y = left[0], left[1]							# update x,y as left neighbour's position
				if(right not in walls and right not in visited):	# check if right is traversible
					x, y = right[0], right[1]						# update x,y as right neighbour's position
				if(up not in walls and up not in visited):			# check if up is traversible
					x, y = up[0], up[1]								# update x,y as up neighbour's position
				if(down not in walls and down not in visited):		# check if down is traversible
					x, y = down[0], down[1]							# update x,y as down neighbour's position
			else:											# if current cell is not blocked from 3 sides
				break										# break the while loop
