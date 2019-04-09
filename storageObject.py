'''
storage object class for other objects
'''

class binClass():
	'''
	storage object
	'''
	def __init__(self, name, slotsTotal, slotsFree):
		self.name = name

		# space in containter
		self.slotsTotal = slotsTotal
		self.slotsFree = slotsTotal
		self.slotsUsed = 0
		
		# list of objects stored in this object
		self.storedItems = []		
	
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.name

	def getName(self):
		return self.name
	
	def getTotalSlots(self):
		return self.slotsTotal
		
	def getUsedSlots(self):
		# reset to prevent double counting slots
		self.slotsUsed = 0
		# counting the amounts of slots needed for stored items
		for i in range(len(self.storedItems)):
			self.slotsUsed += self.storedItems[i].getSlotsNeeded()
		return self.slotsUsed

	def getFreeSlots(self):
		return self.getTotalSlots() - self.getUsedSlots()
		
	def getStoredItems(self):
		return self.storedItems
		
	def moveItem(self, item, location): 
		location.addItem(self.storedItems.pop(self.storedItems.index(item)))

class lockerClass(binClass):
	
	def __init__(self, name):
		# subclass of bin class
		binClass.__init__(self, name, 80, 80)
		
	def addItem(self, item):
		# check if item is allowed to go in locker
		if item.canGoInLocker() == True:
			# move item to locker
			self.storedItems.append(item)
			return f'{item} moved to {self.name}.'
				
class backPackClass(binClass):
	
	def __init__(self, name):
		binClass.__init__(self, f'{name} backpack', 40, 40)
	
	def addItem(self, item):
		# check if item is allowed to go in back pack
		if item.canGoInBackpack() == True and self.getFreeSlots() - item.getSlotsNeeded():
			# move item to backpack
			self.storedItems.append(item)
			return f'{item} is in {self.name}.'			
		elif item.canGoInBackpack() == False:
			return f'{item} cannot be in {self.name}'
		
			
class pencilCaseClass(binClass):
	
	def __init__(self, name):
		binClass.__init__(self, f'{name} pencil case', 10, 10)
		self.goesInLocker = True
		self.goesInBackpack = True
		self.goesInPencilCase = False
		self.slotsNeeded = 1
	
	def addItem(self, item):
		# check if item is allowed to go in pencil case
		if item.canGoInPencilCase() == True:
			# move item to pencil case
			self.storedItems.append(item)
			
	def canGoInLocker(self):
		return self.goesInLocker
		
	def canGoInBackpack(self):
		return self.goesInBackpack
		
	def canGoInPencilCase(self):
		return self.goesInPencilCase	

	def getSlotsNeeded(self):
		return self.slotsNeeded

class testItem:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return self.name
	def getName(self):
		return self.name
	def canGoInLocker(self):
		return True
	def canGoInBackpack(self):
		return True
	def canGoInPencilCase(self):
		return True
	def getSlotsNeeded(self):
		return 3
		
# TESTS
if __name__ == '__main__':
	testBackpack = backPackClass('test')
	testLocker = lockerClass('locker')

	cube = testItem('cube')
	sphere = testItem('sphere')
	pyramid = testItem('pyramid')

	testLocker.addItem(testItem('bob the builder'))
	print(testLocker.getFreeSlots())
	testLocker.addItem(cube)
	testLocker.addItem(sphere)
	testLocker.addItem(pyramid)
	print(testLocker.getFreeSlots())
	print(testLocker.getStoredItems())