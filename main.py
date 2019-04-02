'''
t: inventory system - backpak
a: zeeshan hooda
d: 04/01/2019
'''

class backpack:
    """
    docstring
    """
    
    def __init__(self, name):
        self.name = name
        self.carrying = []
        self.slotsFree = 40
        self.slotsUsed = 0
        self.capacity = self.slotsFree + self.slotsUsed

    def __str__(self):
        return f'{self.name} is using {self.slotsUsed} slots and has {self.slotsFree} slots free.'


# class pencilCase:
#   def __init__(self):
#       self.carrying = []
#       self.slotsFree = 10
#       self.slotsUsed = 0
#       self.capacity = self.slotsFree + self.slotsUsed


if __name__ == '__main__':
    print('tests')
