class BankAccount:
    """Stores info about an account

    Holds information such as names, addresses and balances of different bank
    accounts"""

    bankName = 'Natwest'
    __count = 0

    def __init__(self, N, A):
        self.name = N
        self.address = A
        self.__balance = 0
        BankAccount.__count += 1

    def withdraw(self, x):
        if (self.__balance - x < 0):
            raise ValueError('You do not have sufficient funds for this transaction')
        else:
            self.__balance -= x

    def deposit(self, x):
        self.__balance += x


    def get_balance(self):
        return(self.__balance)

    def display(self):
        print(self.name + ' - ' + str(self.__balance))

    def transfer(self, destination, amount):
        if (self.__balance - amount < 0):
            raise ValueError('Insufficient funds')
        else:
            try:
                self.__balance -= amount
                destination.__balance += amount
            except:
                raise ValueError('Cannot find destination')

    def __add__(self, other):
        if type(other) == int:
            self.__balance += other
        else:
            try:
                #self.name = (self.name, other.name)
                #self.address = (self.address, other.address)
                self.__balance += other.__balance
                other.__balance = 0
            except:
                pass

bank1 = BankAccount('Ed Prince', '4 Stockghyll Brow')
bank2 = BankAccount('Dan Prince', 'Somewhere, Himalayas, India')

bank1.display()

bank1.deposit(12)
bank2.deposit(100000)
print(bank1.get_balance())

bank_merge = (bank2 + bank1)
print(bank_merge)
print(bank1.get_balance())
print(bank2.get_balance())
print(bank2.display())

bank3 = BankAccount('Ambrose', 'Australia')
bank2.get_balance()

bank1.display()
