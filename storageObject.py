'''
storage object class for other objects
'''

class binClass:
	'''
	docstring
	'''
	
	def __init__(self, name, slotsTotal, slotsFree):
		self.name = name
		self.slotsTotal = slotsTotal
		self.slotsUsed = slotsFree
		self.slotsUsed = 0
		self.storedObj = []
		
	def getName(self):
		return self.name
	
	def getTotalSlots(self):
		return self.slotsTotal
		
	def getUsedSlots(self):
		self.slotsFree = getTotalSlots - 
		return len(self.storedObj)
		
	def getFreeSlots(self):
				