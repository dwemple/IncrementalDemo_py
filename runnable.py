# Little something to try out and test the calculations for possible future incremental games 
# Press Spacebar to simulate a "click",
# "b" to buy items, press "X" to exit (have to press Enter to confirm the input)
# Tested on VSCode interactive mode for python 
import time as t
import threading
from IPython.display import clear_output

############# Global variables - these change the most #############
totalSum = 0
addPS = 0
item1, item2, item3, item1kps, item2kps, item3kps = 0,0,0,0,0,0
ended = False

# static (for upgrades)
clickMulti = 0
kpsMulti = 0
buyMulti = 1.7

startTime = t.perf_counter()

############# Function definitions #############

# Input switch, calls assigned functions to keys
def inputCheck():
    global ended, totalSum, clickMulti
    while(1):
        inputKey = input('click')
        if inputKey == 'X': # EXIT
            ended = True
            break
        if inputKey == ' ': # BASIC CLICK
            totalSum = totalSum + (1 + totalSum * clickMulti)
        if inputKey == 'b': # BUY ITEMS
            buyItem()
        if inputKey == "help": # :^)
            print('Press Spacebar to simulate a "click", "b" to buy items,'
            ' press "X" to exit (have to press Enter to confirm the input)')

# Prints info every 1s, cleans after itself,
# calculates current total sum by adding IDLE kps every second
def printer():
    global ended, totalSum, item1, item2, item3, item1kps, item2kps, item3kps, addPS
    while(1):
        t.sleep(1)
        clear_output()
        totalSum = totalSum + addPS
        currentTime = t.perf_counter()
        print(f'Current total: {round(totalSum, 2)} koin || KPS: {addPS}kps || Total time:'
        f'{round(currentTime-startTime, 2)}  s\nItem1: {item1} making {item1kps} kps\n'
        f'Item2: {item2} making {item2kps} kps\nItem3: {item3} making {item3kps} kps', flush=True)
        if ended: 
            print('\rENDING LOOP')
            break

# Handles buying items, asks for needed input
def buyItem():
    i1baseCost = 50
    i2baseCost = 1000
    i3baseCost = 15000
    global item1, item2, item3, item1kps, item2kps, item3kps, addPS, totalSum
    totalCost = 0

    itemNumber = int(input('What item (number 1-3)'))
    itemAmount = int(input('Amount to buy'))
    if itemNumber == 1:
        totalCost = countTotalCost(i1baseCost, itemAmount, item1)
    elif itemNumber == 2:
         totalCost = countTotalCost(i2baseCost, itemAmount, item2)
    elif itemNumber == 3:
         totalCost = countTotalCost(i3baseCost, itemAmount, item3)
    else: 
        print('Wrong input!')
        return
    confirm = input(f'Costs {totalCost}, y?')
    if confirm == 'y':
        totalSum = totalSum - totalCost
        if itemNumber == 1:
            item1 += itemAmount
            addPS += itemAmount * 0.1
            item1kps += itemAmount * 0.1
        elif itemNumber == 2:
            item2 += itemAmount
            addPS += itemAmount
            item2kps += itemAmount
        elif itemNumber == 3:
            item3 += itemAmount
            addPS += itemAmount * 15
            item3kps += itemAmount * 15
    else:
        print('nvm!')

# Calculation of the total Koin needed to buy items
def countTotalCost(baseCost, itemAmount, currentAmount):
    global buyMulti
    totalAmount = 0
    for i in range(itemAmount):
        print('hi')
        totalAmount = totalAmount + baseCost * pow(buyMulti, currentAmount)
        currentAmount += 1
    return totalAmount

############# Running the code #############
t1 = threading.Thread(target=inputCheck)
t2 = threading.Thread(target=printer)
t1.start()
t2.start()
t1.join() 
t2.join()


