'''
electronics objects
'''

class techClass:

	def __init__(self, name, slotsNeeded):
		self.name = name
		self.slotsNeeded = slotsNeeded
		self.goesInBackpack = True
		self.goesInLocker = True
		self.goesInPencilCase = False

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def canGoInLocker(self):
		return self.goesInLocker

	def canGoInBackpack(self):
		return self.goesInBackpack
		
	def canGoInPencilCase(self):
		return self.goesInPencilCase

	def getSlotsNeeded(self):
		return self.slotsNeeded
		