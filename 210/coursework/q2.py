def countTrailingZeros(myNumber):
    '''Calculates the number of trailing zeros in the factorial of given number

    Takes any integer value, calvulates the number of 5 + 2 factors'''
    i = 1
    total = 0
    while myNumber >= i:
        i *= 5
        total += myNumber / i
    return total

#Unit Tests
tests = [0,1,2,3,4,5,6,7,8,9,10]
results = [0,0,0,0,0,1,1,1,1,1,2]
testResults = [countTrailingZeros(n) for n in tests]
print(testResults)
print(results)
if testResults == results:
    print('Passed all tests')
