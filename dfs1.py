def start(myTurtle, walls, finish, cellWidth):
	myTurtle.shape('circle')	# set the shaoe of myTurtle as circle
	myTurtle.pensize(2)			# set the pen width as 2
	myTurtle.showturtle()		# make the turtle visible
	visited = []				# list of nodes that have been visited

	def dfs_path(x, y, visited):
		'''
			func: recursive func to implement dfs
			inp: x coord, y coord, visited list
			out: True (reached goal) / False 
		'''
		
		if((x,y) in finish):								# if current node is the final node
			myTurtle.pencolor('red')						# change the pen color to red
			myTurtle.goto(x,y)								# goto location
			return True 									# return True

		if((x,y) not in walls and (x,y) not in visited):	# if current node is not wall and is not visited
			visited.append((x,y))							# append in visited list
			
			myTurtle.pencolor('red')						# set the pen color as red
			myTurtle.goto(x,y)								# goto the location of current node
			myTurtle.pencolor('grey')						# set the pen color as grey

			if(dfs_path(x-cellWidth, y, visited)):			# recursive call with left neighbour
				return True 								# return True

			myTurtle.goto(x,y)								# go back to location of current node 

			if(dfs_path(x+cellWidth, y, visited)):			# recursive call with right neighbour
				return True 								# return True

			myTurtle.goto(x,y)								# go back to location of current node

			if(dfs_path(x, y-cellWidth, visited)):			# recursive call with down neighbour
				return True 								# return True

			myTurtle.goto(x,y)								# go back to location of current node

			if(dfs_path(x, y+cellWidth, visited)):			# recursive call with up neighbour
				return True 								# return True
			
			myTurtle.goto(x,y)								# go back to location of current node




	x = round(myTurtle.xcor(),1)							# current x coord
	y = round(myTurtle.ycor(),1)							# current y coord
	dfs_path(x, y, visited)									# first call with current node



