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
					 count = 1
				 else:
				 	fronteirTop.append(newNode)
		botNode = fronteirBot.popleft()
		if(contains(fronteirTop,botNode)):
				return createAnswer(fronteirTop,botNode,Expanded)
		Actions = getActions(botNode)
		for x in Actions:
			newNode = Node(botNode,x)
			if (contains(fronteirTop,newNode)):
				return createAnswerBot(fronteirTop,newNode,expanded)
			else:
				if(expanded.contains(newNode)):
						count = 1
				else:
					fronteirBot.append(newNode)
		expanded.append(topNode)
		expanded.append(botNode)


def contains(fronteir,node):
	contains = False
	for x in fronteir:
		if(x == node):
			return True
	return contains


def createAnswerBot(frontier,node,Expanded):
	botstart = None
	nodes = deque()
	bot = node;
	nodes.append(bot)
	while(bot.parent != None):
		nodes.append(bot.parent)
		bot = bot.parent

	for x in frontier:
		if(node.state == x.state):
			botStart = x
			break
	if(botStart != None):
		while (botStart.parent != None):
			nodes.appendleft(botStart.parent)
			botStart = botStart.parent
	
	count = len(nodes)-1
	order = deque()
	while(count!=-1):	
		tmp = nodes[count]		
		order.appendleft(tmp)
		count -=1
	return createdAnswer(order,Expanded)


def createAnswer(frontier,node,Expanded):
	botStart = None
	nodes = deque()
	top = node
	while(top.parent != None):
		nodes.appendleft(top)
	for x in frontier:
		if(node.state == x.state):
			botStart = x
			break;
	while(botStart.parent != None):
		nodes.append(botStart)
		botStart= botStart.parent

	return createdAnswer(nodes,Expanded)
def createdAnswer(nodes,expanded):
	node = nodes.popleft()
	start = Node(node.state)
	while(len(nodes)!=0):
		start = CheckAction(nodes[0].state,start)
		tmp = nodes.popleft()
	return Answer(start,expanded)
def CheckAction(state,parent):
	actions = getActions(parent)
	for x in actions:
		if(state == x(parent)):
			return Node(parent,x)

