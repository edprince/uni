m1 = [[1,2,3],
      [3,4,4],
      [5,6,5],
      [7,8,6]]
m2 = [[7,8,7],
      [9,10,8],
      [11,12,9],
      [13,14,10]]

def add(m1, m2):
    '''Matrix addition function

    Accepts two matrix's in the form of embedded lists providing they are of the
    same dimensions and performs an addition of them. Efficiency O(N^2)'''
    if (checkLength(m1,m2)):
        return "Matrix's must be of the same length."
    result = m1
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] + m2[i][j]

    return result


def subtract(m1, m2):
    '''Matrix subtraction function

    Accepts two matrix's in the form of embedded lists providing they are of the
    same dimensions and performs a subtraction of them'''
    if (checkLength(m1,m2)):
        return "Matrix's must be of the same length."
    result = m1
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] - m2[i][j]

    return result

def multiply(m1, m2):
    if (type(m1) == int):
        multiplyInt(m1, m2)
    elif (type(m2) == int):
        multiplyInt(m2, m1)

    #Compute standard multiplication





def multiplyInt(integer, matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = integer * matrix[i][j]

    return result


def checkLength(m1, m2):
    if (len(m1) != len(m2)):
        return False

print(add(m1, m2))
