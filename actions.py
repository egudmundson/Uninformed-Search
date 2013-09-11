from Node import Node

def left(node):
	currentState = node.state
	i = currentState.index(0)
	outputState= []
	if(i == 0 or i == 3 or i == 6):
		return None 
	for x in range(0,len(currentState)):
		if(x == i-1):
			outputState.append(0)
		if(x == i):
			pass
		else:
			outputState.append(currentState[x])
	return outputState
def right(node):
	currentState = node.state
	i = currentState.index(0)
	outputState = []
	if(i == 2 or i == 5 or i == 8):
		return None
	for x in range(0,len(currentState)):
		if(x == i):
			outputState.append(currentState[x+1])
			outputState.append(0)		
		elif(x == i+1):
			pass
		else:
			outputState.append(currentState[x])
	return outputState
def up(node):
	currentState = node.state
	i = currentState.index(0)
	outputState = []
	for x in range(0,len(currentState)):
		if(x ==i -3):
			outputState.append(0)
		elif(x == i):
			outputState.append(currentState[x-3])
		else:
			outputState.append(currentState[x])
	return outputState
def down(node):
	currentState = node.state
	i = currentState.index(0)
	outputState = []
	for x in range(0,len(currentState)):
		if(x == i +3):
			outputState.append(0)
		elif(x == i):
			outputState.append(currentState[x+3])
		else:
			outputState.append(currentState[x])
	return outputState

def getActions(node):
	count =0
	for x in node.state:
		if(x ==0):
			break
		count+=1

	if(count == 4):# block in the middle
		return [left,right,up,down]
	elif(count == 3):
		return [up,down,right]
	elif(count == 5):
		return [up,down,left]
	elif(count==0):
		return [down,right]
	elif(count == 1):
		return [down,left,right]
	elif(count == 2):
		return [down,left]
	elif(count ==6):
		return[up,right]
	elif(count == 7):
		return [up,right,left]
	elif(count ==8):
		return [up,left]
		
	

