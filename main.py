#!/usr/bin/env python

import json

'''
FriendRank
Author: Sean Behan
Inspired by an idea from Terri Dobbins
'''

def loadSave():
    data = {}
    try:
        with open('save.json', 'r') as fp:
            data = json.load(fp)
    except:
        pass
    return data

def saveDict(personDict):
    with open('save.json', 'w') as fp:
        json.dump(personDict, fp)
    return

def getPersonInfo():
    print("What's their name?")
    name = input()
    print("What's their rank?")
    rank = convertToInt(input())
    return [name, rank]

def addNewPerson(personDict, name, rank):
    personDict[name] = rank
    return personDict

def showSaved(personDict):
    output = ''
    dictLength = 0
    for element in personDict:
        dictLength += 1
    if dictLength == 0:
        output += "\nNo names in name list!\n"
        return output
    output += "\n----------------------------\n"
    output += "Name\t\tRank"
    output += "\n"
    for name in personDict:
        output += ('\n%-*s\t%s' % (10, name, personDict[name]))
    output += "\n----------------------------"
    return output

def convertToInt(number):
    try:
        intInput = int(number)
        if intInput not in range(11):
            raise ValueError('Not in the range of numbers that we have programmed for')
        return intInput
    except:
        print("This is not valid input, please try again.")

def prompt():
    output = ('''
    You can do a few things here :)

    Type a number to choose.

    1. Show saved people
    2. Add a new person
    3. Set an existing persons rank

    4. Quit program
        ''')
    return output

def addPerson(name, rank, thedict):
    thedict[name] = rank

def main():
    print('''
Welcome to FriendRank!
    ''')

    personDict = loadSave()
    weAreListeningForMoreNames = True
    # Initialize some variables

    while weAreListeningForMoreNames:
        print(prompt())
        userInput = input("Selection: ")
        userInputInt = convertToInt(userInput)

        '''
        print('userInput: ', list(userInput))
        print('userInputInt: ', list(str(userInputInt)))
        '''

        if (userInputInt == 1):
            print(showSaved(personDict))
        elif (userInputInt in [2, 3]):
            newPersonInfo = getPersonInfo()
            personDict = addNewPerson(personDict, newPersonInfo[0], newPersonInfo[1])
            print(showSaved(personDict))
            saveDict(personDict)
        elif (userInputInt == 4):
            print("Bye :)")
            quit()

if  __name__ =='__main__':main()
