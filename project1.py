#! /usr/bin/python
from Node import Node
from BreadthFirst import *
from time import time
from Depth import depthFirstSearch
from collections import deque
if __name__ == "__main__":
	print "Welcome to the Uninformed search Project"
	fname =raw_input("please enter the file name of initial config:")
	fileIn = open(fname,'r')
	state = []
	for  line in fileIn:
		print line
		line = line.strip();
		for x in line:
			if(x !='_'):
				 state.append(int(x))
			else:
				state.append(0)
	start = Node(state)
	goal = Node([0,1,2,3,4,5,6,7,8])
	print "select from the following:"
	print "B for Breadth"
	print "D for depth First"	
	print "DL for Depth Limited"
	print "I for Iterative "
	print "BD for Bi-Directional"
	usrchoice = raw_input("Selections:")	
	usrchoice = usrchoice.lower()
	if(usrchoice == 'b' or usrchoice == 'B'):
		t0 = time()
		answer = BreadthSearch(start,goal)
		t1 = time()
		print "Response: Time:  %f" %(t1-t0)
		print len(answer.expanded)
	elif(usrchoice == 'd' or usrchoice == 'D'):
		t0 = time()
		answer = depthFirstSearch(start,goal,-1)
		t1= time()
	elif(usrchoice == 'dl'):
		limit = raw_input("Please enter a depth limit:")
		limit = int(limit)
		t0 = time()
		answer = depthFirstSearch(start,goal,limit)
		t1 = time()
	elif(usrchoice == 'i'):
		limit = 0
		answer = None
		t0 = time()
		while(1):
			print "Trying Depth level: "+str(limit)
			answer = depthFirstSearch(start,goal,limit)
			if(answer != None):
				break;
			else:
				limit+=1
	
		t1 = time()
	elif(usrchoice == 'bd'):
		t0= time()
		answer = BiDirectional(start,goal)
		t1 = time()
	if(answer != None):
		Moves = deque()	
		print "Response: Time:  %f" %((t1-t0)*1000)
		print "Expanded Nodes = " + str(len(answer.expanded))
		answer = answer.node
		while(answer.parent != None):
			Moves.appendleft(answer.action)
			answer = answer.parent
		print "Moves to get to Answer: " 
		if (len(Moves) <= 100):
			for x in Moves:
				print x
		else:
			start = len(Moves) - 100
			for x in range(start,start+100):
				print Moves[x]
	
