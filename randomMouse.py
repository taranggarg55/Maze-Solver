import random

def start(myTurtle, walls, finish, cellWidth):
	myTurtle.showturtle()						# make the turtle visible
	while(True):								# loop
		x = round(myTurtle.xcor(),0)			# current x coord
		y = round(myTurtle.ycor(),0)			# current y coord
		options = []							# list containing possible moves

		if((x,y) in finish):					# if current node is final node
			break								# break

		if(myTurtle.heading()==0): 				# turtle facing right on screen
			if((x+cellWidth,y) not in walls): 	# no wall in front
				options.append('f')				# put front in options
			if((x,y+cellWidth) not in walls): 	# no wall in left 
				options.append('l')				# put left in options
			if((x, y-cellWidth) not in walls): 	# no wall on right
				options.append('r')				# put right in options
		
		elif(myTurtle.heading()==90): 			# turtle facing up on screen
			if((x,y+cellWidth) not in walls): 	# no wall in front
				options.append('f')				# put front in options
			if((x-cellWidth,y) not in walls): 	# no wall in left
				options.append('l')				# put let in options
			if((x+cellWidth, y) not in walls): 	# no wall in right
				options.append('r')				# put right in options
		
		elif(myTurtle.heading()==180): 			# turtle facing left on screen
			if((x-cellWidth,y) not in walls): 	# no wall in front
				options.append('f')				# put front in options
			if((x,y-cellWidth) not in walls): 	# no wall in left
				options.append('l')				# put left in options
			if((x, y+cellWidth) not in walls): 	# no wall in right
				options.append('r')				# put right in options
		
		elif(myTurtle.heading()==270): 			# turtle facing down on screen
			if((x,y-cellWidth) not in walls): 	# no wall in front
				options.append('f')				# put front in options
			if((x+cellWidth,y) not in walls): 	# no wall in left
				options.append('l')				# put left in options
			if((x-cellWidth, y) not in walls): 	# no wall in right
				options.append('r')				# put right in options

		if(len(options)==0):					# if at deadend 
			myTurtle.right(180)					# turn back
		else:									# not at deadend
			choice = random.choice(options)		# select a direction randomly
			if(choice=='f'):					# if front
				myTurtle.forward(cellWidth)		# move one step forward
			elif(choice=='l'):					# if left
				myTurtle.left(90)				# turn left
				myTurtle.forward(cellWidth)		# move one step forward
			elif(choice=='r'):					# if right
				myTurtle.right(90)				# turn right
				myTurtle.forward(cellWidth)		# move one step forward
		