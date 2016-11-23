def factorial(n):
    """Function to calculate the factorial of a number

    Accepts an integer, before recursively finding it's factorial"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#Turn result into string ready to count zeros

def getZeros(n):
    result = str(factorial(n))
    totalZeros = 0
    #Work backwards through the string until a non-zero is found
    for i in range(len(result) - 1, 0, -1):
        if result[i] == '0':
            totalZeros += 1
        else:
            break
        print(totalZeros)
        return totalZeros


userNumber = int(input('Enter a number: '))
print('There are: ', getZeros(userNumber), ' trailing zeros')


#Unit Tests
tests = [0,1,2,3,4,5,6,7,8,9,10]
results = [0,0,0,0,0,1,1,1,1,1,2]
testResults = [getZeros(n) for n in tests]
print(testResults)
print(results)
