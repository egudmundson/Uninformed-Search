from Node import Node

class hashTable():
	def __init__(self):
		self.dictionary = {}
		for count in range(0,9):
			self.dictionary[count] = []

	def contains(self,node):
		state = node.state
		searchTable = self.dictionary[state[0]]
		exists = False
		for x in searchTable:
			if(state == x.state):
				exists = True
				break
		return exists
	def append(self,node):
		state = node.state
		searchTable = self.dictionary[state[0]]
		exists = False
		for x in searchTable:
			if(state == x.state):
				exists = True
				break
		if(exists == False):
			searchTable.append(node)

	def __len__(self):
		total = 0
		for x in self.dictionary.keys():
			total += len(self.dictionary[x])
		return total


		


