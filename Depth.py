from Node import *
from BreadthFirst import Answer
from actions import *
from collections import deque
from hash import hashTable

def depthFirstSearch(start,goal,limit):
	frontier = deque()
	expanded = hashTable()
	if(start == goal):
		return "already found"
	frontier. append(start)
	while(len(frontier) != 0):
		current = frontier.pop()
		Actions = getActions(current)
		if(current.depth == limit):
			continue
		else:
			for x in Actions:
				newNode = Node(current,x)
				if(newNode == goal):
					print "Answer Found"
					return Answer(newNode,expanded)
				else:
					exists = False
					exists = expanded.contains(newNode)
					if(exists == False):
						for x in frontier:
							if(x == newNode):
								exists = True
								break
					if(exists == False):
						frontier.append(newNode)
			expanded.append(current)
					

