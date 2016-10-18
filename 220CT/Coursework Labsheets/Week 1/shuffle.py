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

    print(array)
#Input list of numebrs from user
while proceed == False:
    result = input('Enter a number (q to stop): ')
    if result == 'q':
        break
    myArray.append(int(result))
      
shuffle(myArray)




    
