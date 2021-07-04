def start(myTurtle, walls, finish, cellWidth, maze):
	maze.color('grey') 												# set the color of maze turtle as grey 

	path = []														# list for path to final node
	visited = []													# list for visited nodes

	def dfs_path(x, y, path, visited):
		'''
			func: recursive func to implement dfs
			inp: x coord, y coord, visited list
			out: True (reached goal)/ False 
		'''
		if((x,y) in finish):										# if current node is the final node
			path.append((x,y)) 										# append final node in path list
			return True 											# return True

		if((x,y) not in walls and (x,y) not in visited):			# if current node is not a wall and is not visited
			visited.append((x,y))									# put the node in visited list
			maze.goto(x,y)											# goto the current node
			maze.stamp()											# put a stamp (grey square)
			
			if(dfs_path(x-cellWidth, y, path, visited)):			# recursive call with left neighbour
				path.append((x,y))									# put the node is path list
				return True 										# return True

			if(dfs_path(x+cellWidth, y, path, visited)):			# recursive call with right neighbour
				path.append((x,y))									# put the node is path list
				return True 										# return True

			if(dfs_path(x, y-cellWidth, path, visited)):			# recursive call with down neighbour
				path.append((x,y))									# put the node is path list
				return True 										# return True

			if(dfs_path(x, y+cellWidth, path, visited)):			# recursive call with up neighbour
				path.append((x,y))									# put the node is path list
				return True 										# return True

		
	x = round(myTurtle.xcor(),1)									# current x coord
	y = round(myTurtle.ycor(),1)									# current y coord
	dfs_path(x, y, path, visited)									# first call with current node
	
	myTurtle.shape('circle')										# set the shape of turtle as circle
	myTurtle.showturtle()											# make the turtle visible
	myTurtle.pensize(2)												# set the pen width as 2
	for i in range(len(path)-1, -1, -1):							# loop through path list in reverse order
		myTurtle.goto(path[i])										# goto the coordinate 

	


