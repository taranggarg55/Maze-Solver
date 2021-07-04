class Node():
	# creating a node class
	def __init__(self, parent=None, position=None, g=0, h=0, f=0):
		self.parent = parent		# parent node
		self.position = position 	# (x,y) coordinate
		self.g = g 					# g cost (actual cost)
		self.h = h 					# h cost (heuristic cost)
		self.f = f 					# f cost (total cost)

	def __eq__(self, other): 		# overiding equivalence
		return self.position == other.position


def start(myTurtle, walls, finish, cellWidth, maze):
	maze.color('grey')			# set the color for search squares as grey
	
	start = Node(None, (myTurtle.xcor(), myTurtle.ycor())) 	# set the initial (start) node
	end = Node(None, finish[0])								# set the final (end) node

	opened = []			# list containing all node whose neighbours are yet to be explored
	closed = []			# list of nodes whose neighbours are fully explored
	path = []			# list containing the final path from start to end

	opened.append(start)							# putting the start node in the opened list
	while(len(opened) > 0): 						# loop until opened list is empty 
		current = opened[0]							# set the current node
		currIndex = 0								# set index as 0
		for index, item in enumerate(opened):		# loop through nodes in opened to get one with min cost
			if item.f < current.f:					# choose if cost is less than current
				current = item
				currIndex = index

		opened.pop(currIndex)						# remove node from open list
		closed.append(current)						# put in closed list

		if(current == end):							# if node is the final node (target)
			while(current != None):					# loop unitl parent is none
				path.append(current.position)		# put position of current in path list
				current = current.parent			# move to parent node
			break									# break the while loop

		children = []								# list of all the neighbours
		for neighbour in [(0, -1*cellWidth), (0, 1*cellWidth), (-1*cellWidth, 0), (1*cellWidth, 0)]: # left, right, down, up
			node_position = (current.position[0] + neighbour[0], current.position[1] + neighbour[1]) # find position of neighbour
			
			if(node_position[0]>end.position[0] or node_position[1]<end.position[1]): # if neighbour is below end of maze -> skip
				continue
			if(node_position[0]<start.position[0] or node_position[1]>start.position[1]): # if neighbour is above start of maze -> skip
				continue
			if node_position in walls: # if neighbour is a walls -> skip
				continue

			new_node = Node(current, node_position) 					# create new node and set parent
			children.append(new_node)									# put in children list

		for child in children:											# loop through all the children
			hasFlag = False												# helps to skip if node already in closed
			for closed_node in closed:									# loop through all the closed nodes
				if(child == closed_node):								# if node in closed
					hasFlag = True
					break												# break
			if(hasFlag):												# if node already in closed -> skip
				continue

			child.g = current.g + 1										# increase actual cost by one
			child.h = ((child.position[0] - end.position[0]) ** 2) + ((child.position[1] - end.position[1]) ** 2) # calc heuristic cost as euclidian distance to target
			child.f = child.g + child.h 								# total cost = actual cost + heuristic cost
			if(child.position != end.position):							# put a stamp is not final node
				maze.goto(child.position[0], child.position[1])
				maze.stamp()

			hasFlag = False												# helps to skip if node already in opened
			for opened_node in opened:									# loop through all the opened nodes
				if(child == opened_node and child.g > opened_node.g):	# if in opened with lesser cost
					hasFlag = True
					break												# break
			if(hasFlag):												# if node in opened with lesser cost -> skip
				continue

			opened.append(child)										# put neighbour in opened list

	myTurtle.shape('circle')											# set the shape of turtle as circle
	myTurtle.showturtle()												# make the turtle visible
	myTurtle.pensize(2)													# set pen width as 2
	for i in range(len(path)-1, -1, -1):								# loop through path list in reverse order
		myTurtle.goto(path[i])											# goto node (trail is on)