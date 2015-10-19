def personalAllowance(x):
    """function takes integer x and calculates the non-taxable allowance due to a given salary (x)"""
    #Take income of x
    allowance = 10600
    i = 100000
    while x > i and i <= x and allowance > 0:
        #equivalent to taking 2 pounds for every pound above 100000
        allowance -= 0.5 
        i += 1
    return allowance

def incomeTax(x):
    """function calculates taxable salary for a given annual salary (x (integer))"""
    allowance = personalAllowance(x)
    print("Allowance: " + str(allowance))
    taxableSalary = x - allowance

    #Check with region salary lands within
    if taxableSalary < 0:
        taxableSalary = 0 
    print(taxableSalary)
    if taxableSalary <= 31785:
        return taxableSalary * 0.2
    elif taxableSalary < 150000:
        return taxableSalary * 0.4
    elif taxableSalary >= 150000:
        return taxableSalary * 0.45

def nationalInsurance(x):
    if x <= 155:
        return x * 0
    elif x < 815:
        return x * 0.12
    else:
        return x * 0.02
