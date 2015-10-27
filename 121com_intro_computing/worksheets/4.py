results = [0, 1]
def fib(a, b):
    """Create Fibonacci list

    appends all results up to 100,000 to a results list"""
    results.append(a + b)
    if (a + b) <= 100000:
        fib(b, results[len(results) - 1])
    return results

fib(0, 1)

term = int(input("Please enter the term of the sequence you wish to know: "))

def choose_term(r, n):
    """Pick term

    Value is returned to the user"""
    return r[n - 1]

print(choose_term(results, term))
