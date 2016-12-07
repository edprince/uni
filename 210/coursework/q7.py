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
    if (counter == userNumber):
        return 'User number is prime'
    if (userNumber % counter == 0):
        return 'User number is not prime'
    else:
        return checkPrime(userNumber, counter + 1)

number = raw_input('Please enter a number to check (q for list): ')
if number == 'q': 
    for i in range(100):
        print(i, checkPrime(i))
else:
    print(int(number), ' - ', checkPrime(int(number)))
