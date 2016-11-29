def findNearestSquare(x):
    '''Function to find the nearest perfect square less than or equal to input

    Accepts any numerical input. Efficiency O(1)'''
    #Find square root (rounded down if necessary)
    x = int(x**0.5)
    #Multiply by itself to get nearest whole square
    return x * x


def unitTest():
    proposals = [10, 20, 50, 55, 100000, 99, 4]
    answers = [9, 16, 49, 49, 99856, 81, 4]
    for i in range(len(proposals) - 1):
        print(i)
        if (findNearestSquare(proposals[i]) == answers[i]):
            print('Correct')
        else:
            print('Failed')

unitTest()

