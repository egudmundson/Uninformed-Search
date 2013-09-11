
class Node():
	def __init__(self,parent,action=None):
		if(action == None):
			self.state = parent
			self.parent = None
			self.cost = 0
			self.depth =0;
			self.action = None
		else:
			self.state = action(parent)
			self.parent = parent
			self.cost = self.parent.cost + 1
			self.depth = parent.depth +1
			self.action = action.__name__

	def __eq__(self,other):
		if isinstance(other,Node):
			return self.state == other.state
	






	

