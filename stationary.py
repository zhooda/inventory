'''
stationary objects
'''

class stationaryClass:
	
	def __init__(self, name, slotsNeeded):
		self.name = name
		self.slotsNeeded = slotsNeeded
		self.goesInBackpack = False
		self.goesInLocker = False
		self.goesInPencilCase = True

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

class binderClass:

	def __init__(self, subject):
		self.name = f'{subject} binder'
		self.slotsNeeded = 9
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

class notebookClass:

	def __init__(self, subject):
		self.name = f'{subject} notebook'
		self.slotsNeeded = 6
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