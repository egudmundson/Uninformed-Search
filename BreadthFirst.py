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
	fronteirTop = deque()
	fronteirBot = deque()
	if(start == goal):
		return Answer(goal,expanded)
	fronteirTop.append(start)
	fronteirBot.append(goal)
	while(len(fronteirTop) != 0 and len(fronteirBot)!=0):
		topNode = fronteirTop.popleft()
		if(contains(fronteirBot,topNode)):
			return createAnswer(topNode,fronteirBot,expanded)
		Actions = getActions(topNode)
		for x in Actions:
			 newNode =Node(topNode,x)
			 if (contains(fronteirBot,newNode)):
				return createAnswer(fronteirBot,newNode,expanded)
			 else:
				 if(expanded.contains(newNode)):
					 print "found in expanded"
				 else:
				 	fronteirTop.append(newNode)
					print "Adding To Top"
		botNode = fronteirBot.popleft()
		if(contains(fronteirTop,botNode)):
				return createAnswer(fronteirTop,botNode,Expanded)
		Actions = getActions(botNode)
		for x in Actions:
			newNode = Node(botNode,x)
			if (contains(fronteirTop,newNode)):
				return createAnswer(fronteirTop,newNode,expanded)
			else:
				if(expanded.contains(newNode)):
						print "found in expanded"
				else:
					fronteirBot.append(newNode)
					print "Added To bot"
		expanded.append(topNode)
		expanded.append(botNode)


def contains(fronteir,node):
	contains = False
	for x in fronteir:
		if(x == node):
			return True
	return contains


def createAnswer(node,frontier,Expanded):
	print "here"
	return "test"
