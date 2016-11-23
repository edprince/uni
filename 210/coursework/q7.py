def checkPrime(n):
    print(n)
    if n == 1:
        return False
    if n % checkPrime(n - 1) == 0:
        return True

checkPrime(15)
