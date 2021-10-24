import os

# Global variables
names = []
presents = []
prices = []
numPeople = int(input("How many people do you want to buy for? "))
exit = False


#Max price
def findMax():
    max = prices[0]
    maxIndex = 0
    for i in range(0, numPeople):
        if(prices[i]>max):
            max = prices[i]
            maxIndex = i
    print("Most expensive item is for ", names[maxIndex], " and is a ", presents[maxIndex], " and costs ", max)
    pause()
#End max

#Min price
def findMin():
    min = prices[0]
    minIndex = 0
    for i in range (0,numPeople):
        if(prices[i]<min):
            min = prices[i]
            minIndex = i   
    print("Least expensive item is for ", names[minIndex], " and is a ", presents[minIndex], " and costs ", min)
    pause()
#End min

#Count how many of inputted items you need to buy
def countOccurences():
    occurrences = 0
    item = input("Enter the item you want to search for: ")
    for i in range (0, numPeople):
        if (item == presents[i]):
            occurrences+=1
    print("You are buying ", occurrences, " people ", item)
    pause()
#End buy

#Total cost of items
def findTotalCost():
    totalCost = 0
    for i in range (0, numPeople):
        totalCost = totalCost + prices[i]
    print("Total cost of items is ", totalCost)
    pause()
#End total

#methods
def printLists():
    print(names)
    print(presents)
    print(prices)
    pause()

#clearscreen
def clearScreen():
    os.system("cls")

#pauses
def pause():
    print("")
    input("Press enter to continue")

#Main menu
def printMenu():
    clearScreen()
    print("Christmas List Manager")
    print("======================")
    print("1 - Find most expensive item")
    print("2 - Find cheapest item")
    print("3 - Find occurrences of particular item")
    print("4 - Find total cost of shopping")
    print("5 - Print list of items")
    print("6 - Exit program")
    print("")
    valid = False
    while(not valid):
        choice = int(input("Enter your choice (1-6): "))
        if (choice<1 or choice>6):
            print("Invalid input - please enter a number between 1 and 6")
        else:
            valid = True
    return choice

# Main program

#list appending with name, item and budget
for i in range(0,numPeople):
    name = input("Enter the name of the person you want to buy for:  ")
    item = input("What do you want to buy them? ")
    cost = float(input("What is your budget?"))
    names.append(name)
    presents.append(item)
    prices.append(cost)

#Menu Options
while (not exit):
    menuOption = printMenu()
    if (menuOption == 1):
        findMax()
    elif(menuOption == 2):
        findMin()
    elif(menuOption == 3):
        countOccurences()
    elif(menuOption == 4):
        findTotalCost()
    elif(menuOption == 5):
        printLists()
    elif(menuOption == 6):
        print("Exiting program")
        exit = True
    else:
        print("Invalid input - please enter a number from 1-6")
