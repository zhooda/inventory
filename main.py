'''
t: inventory system - backpak
a: zeeshan hooda
d: 04/01/2019
'''

from storageObject import lockerClass, backPackClass, pencilCaseClass
from stationary import stationaryClass, binderClass, notebookClass
from electronics import techClass

locker = lockerClass('locker')
backpack = backPackClass('orange')
pencilCase = pencilCaseClass('blue')

storageList = [locker, backpack, pencilCase]

pencilCase.addItem(stationaryClass('black pen', 1))
pencilCase.addItem(stationaryClass('blue pen', 1))
pencilCase.addItem(stationaryClass('red pen', 1))
pencilCase.addItem(stationaryClass('mechanical pencil', 1))
pencilCase.addItem(stationaryClass('eraser', 1))
pencilCase.addItem(stationaryClass('ruler', 1))

backpack.addItem(pencilCase)
backpack.addItem(techClass('laptop', 12))
backpack.addItem(techClass('calculator', 2))

backpack.addItem(notebookClass('math'))
backpack.addItem(notebookClass('physics'))
backpack.addItem(notebookClass('social'))
backpack.addItem(notebookClass('comp sci'))

locker.addItem(binderClass('english'))

def displayStored(storage):
    print(f'{storage.getName().upper()}: ')
    for i in range(len(storage.getStoredItems())):
        print(f'    {storage.getStoredItems()[i]}')
    print()

def listAll():
    displayStored(locker)
    displayStored(backpack)
    displayStored(pencilCase)

def menu():
    print('1) Move item\n2) Add item\n3) QUIT')
    choice = int(input('> '))

    if choice == 1:
        # call move item function
        pass
    elif choice == 2:
        print('    1) Binder\n    2) Notebook\n    3) Pen\n    4) Other Writing Utensil')
        addChoice = int(input('> '))
        if addChoice == 1:
            subject = input('subject: ')
            locker.addItem(binderClass(subject))
            print('Locker')

        elif addChoice == 2:
            subject = input('subject: ')
            backpack.addItem(notebookClass(subject))
            print('Backpack')

        elif addChoice == 3:
            color = input('color: ')
            pencilCase.addItem(stationaryClass(f'{color} pen', 1))
            print('Pencil Case')

        elif addChoice == 4:
            name = input('name: ')
            pencilCase.addItem(stationaryClass(name, 1))
            print('Pencil Case')
    else:
        quit()

    print()

if __name__ == '__main__':
    while True:
        listAll()
        menu()