def findAscSubSequence(myList):
    '''function to find longest sequence of ascending numbers

    accepts a list of any length. Efficiency of O(n)'''
    #variable assignment
    finalList = []
    currentList = [myList[0]]
    highestLength = 0
    for count in range(1,len(myList)):
        if myList[count] > myList[count - 1]:
            currentList.append(myList[count])
        else:
            if (len(currentList) >= highestLength):
                highestLength = len(currentList)
                finalList = currentList
            currentList = [myList[count]]
        #If final pass creates the longest sequence
        if len(currentList) > len(finalList):
            finalList = currentList
    return finalList

testList = [1,3,1,11,3,4,5]
print(findAscSubSequence(testList))



