# %%
# Little something to try out and test the calculations for possible future incremental games 
# Press Spacebar to simulate a "click",
# "b" to buy items, "u" to see all upgrades, 
# press "X" to exit (have to press Enter to confirm the input)
# Tested on VSCode interactive mode for python 
import time as t
import threading
from IPython.display import clear_output

############# Global variables - these change the most #############
totalSum = 0
addPS = 0
clickCount = 0
item1, item2, item3, item1kps, item2kps, item3kps = 0,0,0,0,0,0

ended = False
running = True

# static (for upgrades)
clickMulti = 0
kpsMulti = 0
buyMulti = 1.7
i1baseCost = 50
i2baseCost = 1000
i3baseCost = 15000

startTime = t.perf_counter()

############# Function definitions #############

# Input switch, calls assigned functions to keys
def inputCheck():
    global ended, running, totalSum, clickCount
    while(1):
        inputKey = input('click')
        if inputKey == 'X': # EXIT
            ended = True
            break
        if inputKey == ' ': # BASIC CLICK
            clickCount += 1
            totalSum = totalSum + (1 + totalSum * clickMulti)
        if inputKey == 'u': # BUY UPGRADES
            running = False
            listUpgrades()
            running = True
        if inputKey == 'b': # BUY ITEMS
            buyItem()
        if inputKey == "help": # :^)
            print('Press Spacebar to simulate a "click", "b" to buy items,'
            ' press "X" to exit (have to press Enter to confirm the input)')

# Prints info every 1s, cleans after itself,
# calculates current total sum by adding IDLE kps every second
def printer():
    global ended, totalSum

    item1CB, item2CB, item3CB = 0, 0, 0
    while(1):
        t.sleep(1)

         # Calculations
        totalSum = totalSum + round(addPS, 2) + 2 # Total amount
        currentTime = t.perf_counter() # Total time
        item1CB = countMaxCost(item1, i1baseCost)
        item2CB = countMaxCost(item2, i2baseCost)
        item3CB = countMaxCost(item3, i3baseCost)

        if running:
            clear_output()
            print(f'Current total: {round(totalSum, 2)} koin || KPS: {addPS}kps || Total time:'
            f'{round(currentTime-startTime, 2)} s || Number of clicks: {clickCount}\n'
            '---------------------------------------------------------\n'
            f'Item1: {item1} making {item1kps} kps - [{item1CB[0]}] can buy {item1CB[1]}, costing {item1CB[2]}\n'
            f'Item2: {item2} making {item2kps} kps - [{item2CB[0]}] can buy {item2CB[1]}, costing {item2CB[2]}\n'
            f'Item3: {item3} making {item3kps} kps - [{item3CB[0]}] can buy {item3CB[1]}, costing {item3CB[2]}\n'
            , flush=True)
            if ended: 
                print('\rENDING LOOP')
                break

# Handles buying items, asks for needed input
def buyItem():
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
            addPS += round(itemAmount * 0.1, 2)
            item1kps += round(itemAmount * 0.1, 2)
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
    totalAmount = 0
    for i in range(itemAmount):
        print('hi')
        totalAmount = totalAmount + baseCost * pow(buyMulti, currentAmount)
        currentAmount += 1
    return totalAmount

# Calculations of how many items you can buy MAX based on total amount you have
def countMaxCost(currentAmount, baseCost):
    i = 1
    canBuy = ' '
    realCost = 0
    currentCost = baseCost * pow(buyMulti, currentAmount)
    while currentCost < totalSum:
        canBuy = 'x'
        realCost = currentCost
        currentCost += baseCost * pow(buyMulti, currentAmount + i)
        i += 1
    return canBuy, i - 1, realCost


def listUpgrades():
    t.sleep(1)
    print('PAUSED (only the text is not up to date)\n'
    '------------------------- UPGRADES -------------------------\n'
    '~list of upgrades~')
    input('Continue?')

############# Running the code #############
t1 = threading.Thread(target=inputCheck)
t2 = threading.Thread(target=printer)

t1.start()
t2.start()
t2.join()


 
1  # %%
