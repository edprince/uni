def personal_allowance(x):
    """Calculate personal allowance
    
   Takes integer of x, as annual salary and calculates personal allowance that
   is not taxed"""
    #Take income of x
    allowance = 10600
    i = 100000
    while x > i and i <= x and allowance > 0:
        #equivalent to taking 2 pounds for every pound above 100000
        allowance -= 1 
        i += 2
    return allowance


def income_tax(x):
    """Calculate annual income tax

    Where x is an integer passed
    """
    #Initialize constants as tuple
    LOWER, UPPER = BOUNDS = (31785, 150000)
    allowance = personal_allowance(x)
    taxableSalary = x - allowance
    if taxableSalary < 0:
        taxableSalary = 0 
    #Check with region salary lands within
    if taxableSalary > UPPER:
        overflow = taxableSalary - UPPER
        ans =  (overflow * 0.45) 
        rem = (UPPER - LOWER) * 0.4 + (LOWER * 0.2)
        return rem + ans
    elif taxableSalary < UPPER and taxableSalary > LOWER:
        overflow = taxableSalary - LOWER
        return (overflow * 0.4) + LOWER * 0.2
    else:
        return taxableSalary * 0.2
    print(taxableSalary)


def national_insurance(x):
    """Calculates weekly NHS tax
    
    Takes integer x and calculates within which bound a salary lies to
    pay tax
    """
    #Initialise constants as tuples
    LOWER, UPPER = BOUNDS = (155, 815)
    if x >= UPPER:
        overflow = x - UPPER
        return (int(round((overflow * 0.02) + ((UPPER -
            LOWER) * 0.12))))
    elif x <= LOWER:
        return 0
    elif x > LOWER and x < UPPER:
        return int((x - LOWER) * 0.12)
