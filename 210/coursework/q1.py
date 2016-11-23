from random import randint
proceed = False
myArray = []

def shuffle(array):
    """Function rearrange list of numbers

    Accepts a list of user-defined integers before swapping"""
    #Iterates through list, swapping number with random number in the list
    for i in range(0, len(array) - 1):
       rand = randint(0, len(array) - 1)
       array[i], array[rand] = array[rand], array[i] 

    return array

#Input list of numebrs from user
'''
while proceed == False:
    result = input('Enter a number (q to stop): ')
    if result == 'q':
        break
    myArray.append(int(result))
      
shuffle(myArray)
'''

#Unit tests
testArrays = [[1,2,3,4,5], [0,1], [], [10,9,8,7,6,5,4,3,2,1,0], [3,4,6,6,3,2,6,4,3,2,5,6], [3,3,3,3,1]]

def unitTest(array):
    print(array)
    print(shuffle(array))


[unitTest(array) for array in testArrays]


    
