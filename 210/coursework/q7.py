def checkPrime(n):
    print(n)
    if n <= 1:
        return False
    else: 
        if (n // checkPrime(n - 1)) == 0:
            print('Not prime')
        else:
            print('Prime')


def prime(n):
    if n == 0:
        answer = 0
    if n == 1:
        answer = 1
    else:
        val = n // prime(n - 1)
        if val == 0:
            answer = False
        else:
            answer = True
    return answer

print(prime(13))

