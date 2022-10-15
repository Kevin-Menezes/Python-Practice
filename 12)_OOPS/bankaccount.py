class Account:

    # Constructor....This is called every time an object is created
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount

    # Updating the txt file
    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


class Checking(Account):
     
    def __init__(self,filepath,fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance = self.balance-amount-self.fee

checking = Checking("12)_OOPS//bankbalance.txt",1) # Creating an object of the derived class
checking.deposit(5000)
print(checking.balance)
checking.commit()


# account = Account("12)_OOPS//bankbalance.txt") # Creating an object of Account class
# print(account.balance)

# account.withdraw(100)
# print(account.balance)

# account.commit()