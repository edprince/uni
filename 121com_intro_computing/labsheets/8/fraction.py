class Fraction:
    def __init__(self, n ,d):
        if type(n) != int or type(d) != int:
            raise TypeError('One of the values entered was not an integer')
        
        if d == 0:
            raise ValueError('Cannot have zero as the denominator')

        if d < 0:
            self.n = n * -1
            self.d = d * -1


        self.n = n
        self.d = d

    def __str__(self):
        result = (str(self.n) + '/' + str(self.d))
        return result

    def __add__(self, other):
        result = Fraction(self.n * other.d + other.n * self.d, (self.d * other.d))
        return result

    def __sub__(self, other):
        result = Fraction(self.n * other.d - other.n * self.d, self.d * other.d)
        return result

    def __mul__(self, other):
        result = Fraction(self.n * other.n, self.d * other.d)
        return result

    def __truediv__(self, other):
        result = Fraction(self.n * other.d, self.d * other.n)
        if result.n == result.d:
            return 1
        else:
            return result

    def __eq__(self, other):
        if (self.n / self.d == other.n / other.d):
            return True
        else: 
            return False

    def simplify(self):
        def recur(d, n):
            for i in range(2, 1000):
                if ((n / i).is_integer()
                        and (d / i).is_integer()):
                    self.n = n / i
                    self.d = d / i
                    recur(self.n, self.d)
        recur(self.d, self.n)
        return Fraction(int(self.n), int(self.d))

my_fraction = Fraction(1, 2)
fraction2 = Fraction(1, 4)
print(Fraction.simplify(fraction2 - my_fraction))
