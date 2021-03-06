print("%"*50)
print("Running Personal Allowance tests")
print("%"*50)
try:
    from Week4Lab1 import personal_allowance
    numbers = [9000, 36000, 100000, 115000, 121100, 121200, 121300, 1000000]
    answers = [10600, 10600, 10600, 3100, 50, 0, 0, 0]
    n = len(numbers)
    count=0
    for i in range(n):
        num = numbers[i]
        ans = personal_allowance(num)
        if ans!=answers[i]:
            print("Personal Allowance test for salary " + str(num) + " failed")
            count = count+1
    print(str(n-count) + "/" + str(n) + " personal allowance tests passed")
except ImportError:
    print("The function personal_allowance was not present in the module Week4Lab1")
print("%"*50)
print("End of Personal Allowance tests")
print("%"*50)


print("\n")


print("%"*50)
print("Running Income Tax tests")
print("%"*50)
try:
    from Week4Lab1 import income_tax
    numbers = [9000, 10600, 16000, 31785, 36000, 42385, 60000, 100000, 110000, 1000000]
    answers = [0,0,1080,4237,5080,6357,13403,29403,35403,436143]
    n = len(numbers)
    count=0
    for i in range(n):
        num = numbers[i]
        ans = income_tax(num)
        if ans!=answers[i]:
            print("Income tax test for salary " + str(num) + " failed")
            count = count+1
    print(str(n-count) + "/" + str(n) + " income tax tests passed")
except ImportError:
    print("The function income_tax was not present in the module Week4Lab1")
print("%"*50)
print("End of Income Tax tests")
print("%"*50)


print("\n")


print("%"*50)
print("Running National Insurance tests")
print("%"*50)
try:
    from Week4Lab1 import national_insurance
    numbers = [100, 155, 550, 700, 800, 815, 1000, 20000]
    answers = [0,0,47,65,77,79,83,463]
    n = len(numbers)
    count=0
    for i in range(n):
        num = numbers[i]
        ans = national_insurance(num)
        if ans!=answers[i]:
            print("National Insurance test for salary "  + str(num) + " failed")
            count = count+1
    print(str(n-count) + "/" + str(n) + " National Insurance tests passed")
except ImportError:
    print("The function national_insurance was not present in the module Week4Lab1")
print("%"*50)
print("End of National Insurance tests")
print("%"*50)
