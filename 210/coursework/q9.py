import math

def binarySearch(myList, lower_bound, upper_bound):
    '''Binary search adaption function

    Accepts a list and integer bounds in which to search. Finds whether
    the list contains a number within these specified bounds'''
    first = 0
    last = len(myList) - 1
    success = False

    while (first <= last and not success):
        mid = int(math.ceil((first + last) // 2))
        if (myList[mid] >= lower_bound and myList[mid] <= upper_bound):
            success = True
        elif (myList[mid] > upper_bound):
            last = mid - 1
        else:
            first = mid + 1

    return success


def unitTest():
    '''Unit testing function

    Accepts no arguments, runs the function with a set of inputs, printing the results'''
    #Variable assignment

    testLists = [[1,2,3], [0,1,2,3,4,5,6,7], [5,6,7,8,10,15]]
    bounds = [[4,6], [1,3], [12,16]]
    for index1 in range(len(testLists)):
        print(testLists[index1]);
        for index2 in range(len(bounds)):
            print('Lower: ', bounds[index2][0])
            print('Upper: ', bounds[index2][1])
            print(binarySearch(testLists[index1], bounds[index2][0], bounds[index2][1]))

unitTest()
