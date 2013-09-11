import unittest
import actions
from Node import Node

class ActionTests(unittest.TestCase):
	def testgetAcitions(self):
		state = [1,2,3,4,0,5,6,7,8]
		test = Node(state)
		#this tests the _ in the middle right position
		self.assertEqual(state,test.state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__, "left")
		self.assertEqual(action[1].__name__,"right")
		self.assertEqual(action[2].__name__,"up")
		self.assertEqual(action[3].__name__,"down")
		# test for the _ in middle left position
		state = [1,2,3,0,4,5,6,7,8]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__, "up")
		self.assertEqual(action[1].__name__,"down")
		self.assertEqual(action[2].__name__,"right")
		# Test for the _ in middle right position
		state = [1,2,3,4,5,0,6,7,8]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__, "up")
		self.assertEqual(action[1].__name__,"down")
		self.assertEqual(action[2].__name__,"left")
		# Test for the top left position
		state = [0,1,2,3,4,5,6,7,8]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__,"down")
		self.assertEqual(action[1].__name__,"right")
		# test for the top middle position
		state = [1,0,2,3,4,5,6,7,8]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__,"down")
		self.assertEqual(action[1].__name__,"left")
		self.assertEqual(action[2].__name__,"right")		
		# test for the top right position
		state = [1,2,0,3,4,5,6,7,8]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__,"down")
		self.assertEqual(action[1].__name__,"left")
		# test for the bottom left
		state = [1,2,3,4,5,6,0,7,8]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__,"up")
		self.assertEqual(action[1].__name__,"right")
		# test for the bottom middle
		state = [1,2,3,4,5,6,7,0,8]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__,"up")
		self.assertEqual(action[1].__name__,"right")
		self.assertEqual(action[2].__name__,"left")
		# test for the bottom right
		state = [1,2,3,4,5,6,7,8,0]
		test = Node(state)
		action = actions.getActions(test)
		self.assertEqual(action[0].__name__,"up")
		self.assertEqual(action[1].__name__,"left")

	def testActionLeft(self):
		state = [1,2,3,4,0,5,6,7,8]
		test = Node(state)
		newstate = actions.left(test)
		goalState = [1,2,3,0,4,5,6,7,8]
		self.assertEqual(newstate,goalState)
		test = Node(goalState)
		newstate =actions.left(test)
		self.assertEqual(newstate,None)

	def testActionRight(self):
		state = [1,2,3,0,4,5,6,7,8]
		test = Node(state)
		newstate = actions.right(test)
		goalState = [1,2,3,4,0,5,6,7,8]
		self.assertEqual(newstate,goalState)
	def testActionUp(self):
		state = [1,2,3,4,0,5,6,7,8]
		test= Node(state)
		newState = actions.up(test)
		goalState = [1,0,3,4,2,5,6,7,8]
		self.assertEqual(newState,goalState)
	def testActionDown(self):
		state = [1,0,2,3,4,5,6,7,8]
		test = Node(state)
		newState = actions.down(test)
		goalState = [1,4,2,3,0,5,6,7,8]
		self.assertEqual(newState,goalState)
unittest.main()
