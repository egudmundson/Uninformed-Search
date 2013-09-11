from Node import *
from collections import deque
from actions import *
from hash import hashTable
class Answer():
	def __init__(self,node,expanded):
		self.node = node
		self.expanded = expanded

def BreadthSearch(start,goal):
	frontier = deque()
	expanded =hashTable()
	if(start == goal):
		return Answer(start,expanded)
	frontier.append(start)
	while(len(frontier) != 0):
		current= frontier.popleft()
		Actions = getActions(current)
		for x in Actions:
			newNode = Node(current,x)
			if(newNode == goal):
				print "Answer found"
				return Answer(newNode,expanded)
			else:
				exists = False
				exists = expanded.contains(newNode)		
				if(exists == False):
					for nodes in frontier:
						if(nodes == newNode):
							exists = True
							break
				if(exists == False):
					frontier.append(newNode)
		expanded.append(current)
def BiDirectional(start,goal):
	expanded = hashTable()
	fronteirtop = deque()
	fronteirBot = deque()
	if(start == goal):
		return Answer(goal,expanded)
	fronteirtop.append(start)
	fronteirBot.append(goal)
	while(len(fronteirtop) != 0 and len(fronteirBot)!=0):
		topNode = fronteirtop.popleft()
		if(contains(fronteirBot,topNode)):
			return createAnswer(topNode,fronteirBot)
		 


def contains(fronteir,node):
	contains = False
	for x in fronteir:
		if(x == node):
			return True
	return contains


def createAnswer(node,frontier):
	print "here"
	return "test"
