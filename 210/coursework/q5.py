'''PSEUDOCODE
ADDING

IF LENGTH OF matrix1 IS NOT EQUAL TO LENGTH OF matrix2 THEN
    OUTPUT 'Matrix must be of same size'
    BREAK
ELSE
    FOR EACH vertical element IN matrix1 DO
        FOR EACH horizontal element IN matrix1 DO
            #vertical element = ve
            #Horizontal element = he
            resultant[ve][he] -> 
            matrix1[ve][he] + matrix2[ve][he]


SUBTRACTING

Exactly the same at addition but subtracting the ve and he


MULTIPLYING

INPUT matrix1
INPUT matrix2

IF matrix1 OR matrix 2 EQUAL INTEGER THEN
    FOR EACH ve IN matrix DO
        FOR EACH he IN matrix DO
            resultantMatrix[ve][he] -> matrix[ve][he] * INTEGER
    RETURN resultantMatrix

ELSE
    FOR EACH ve IN he IN matrix2 DO
        FOR EACH ve IN he IN matrix1 DO
            MULTIPLY ve BY FIRST ELEMENT IN matrix2
            add to value in corresponding column of resultant matrix

'''
def add(m1, m2):
    '''Matrix addition function

    Accepts two matrix's in the form of embedded lists providing they are of the
    same dimensions and performs an addition of them. Efficiency O(N^2)'''
    print(m2)
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
    '''Takes two matrices and multiplies

    Accepts two matrices only in the form of nested lists or
    one integer and one matrix'''
    #If either argument is an integer
    if (type(m1) == int):
        return multiplyInt(m1, m2)
    elif (type(m2) == int):
        return multiplyInt(m2, m1)

    #Compute standard multiplication
    zipped_b = zip(*m2)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zipped_b] for row_a in m1]

def multiplyInt(integer, matrix):
    #Set resultant matrix to the correct size
    result = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = integer * matrix[i][j]

    return result


def checkLength(m1, m2):
    if (len(m1) != len(m2)):
        return True

B = [[1,2,3],
      [4,5,6],
      [7,8,9],
      [10,11,12]]
C = [[1,2,3],
      [1,2,4],
      [1,2,4],
      [3,4,5]]
print(subtract(multiply(B, C), multiply(2,add(B, C))))
