'''PSEUDOCODE
INPUT userNumber

FUNCTION checkPrime(userNumber:INT, start:INT) DO
  start=2 by default
  IF userNumber EQUALS 2 OR counter EXCEEDS userNumber THEN
    userNumber NOT PRIME
  IF userNumber GREATER THAN counter THEN
    checkPrime(userNumber, counter + 1)
'''
def checkPrime(userNumber, counter=2):
    if (userNumber % counter == 0 or userNumber > counter):
        return 'User number is not prime'
    if (userNumber > counter):
        return checkPrime(userNumber, counter + 1)
    return 'User number is prime'

number = raw_input('Please enter a number to check (q for list): ')
if number == 'q': 
    for i in range(100):
        print(i, checkPrime(i))
else:
    print(int(number), ' - ', checkPrime(int(number)))
