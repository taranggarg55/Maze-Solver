def start(myTurtle, walls, finish, cellWidth):
	myTurtle.showturtle()							# make the turtle visible
	while(True):									# loop
		x = round(myTurtle.xcor(),0)				# current x coord
		y = round(myTurtle.ycor(),0)				# current y coord
		heading = myTurtle.heading()				# current direction (0-360)

		if ((x, y) in finish):  					# if current node is final node
			break									# break while loop
		
		if(heading==0):								# turtle facing right on screen
			if( (x, y-cellWidth) in walls ):		# check if wall on the right of turtle
				if( (x+cellWidth, y) not in walls):	# if no wall in front
					myTurtle.forward(cellWidth)		# move one step forward
				else:								# wall in front
					myTurtle.left(90)				# turn left
			else:									# no wall on left side
				myTurtle.right(90)					# turn right
				myTurtle.forward(cellWidth)			# move one step forward

		
		if(heading==90):							# turtle facing up on screen
			if( (x+cellWidth, y) in walls ):       	# check if wall on the right of turtle
				if( (x, y+cellWidth) not in walls):	# if no wall in front
					myTurtle.forward(cellWidth)		# move one step forward
				else:								# wall in front 
					myTurtle.left(90)				# turn left
			else:									# no wall on left side
				myTurtle.right(90)					# turn right 
				myTurtle.forward(cellWidth)			# move one step forward
		
		if(heading==180):							# turtle facing left on screen
			if( (x, y+cellWidth) in walls ):       	# check if wall on the right of turtle
				if( (x-cellWidth, y) not in walls):	# if no wall in front
					myTurtle.forward(cellWidth)		# move one step forward
				else:								# wall in front
					myTurtle.left(90)				# turn left 
			else:									# no wall on left side
				myTurtle.right(90)					# turn right
				myTurtle.forward(cellWidth)			# move one step forward
		
		if(heading==270):							# turtle facing down on screen
			if( (x-cellWidth, y) in walls ):       	# check if wall on the right of turtle
				if( (x, y-cellWidth) not in walls):	# if no wall in front
					myTurtle.forward(cellWidth)		# move one step forward
				else:								# wall in front
					myTurtle.left(90)				# turn left
			else:									# no wall on left side
				myTurtle.right(90)					# turn right
				myTurtle.forward(cellWidth)			# move one step forward



