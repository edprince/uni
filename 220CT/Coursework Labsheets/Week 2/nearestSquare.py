def findNearestSquare(x):
    x = int(x**0.5)
    return x * x

#print(findNearestSquare(int(input('Input a number: '))))

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
