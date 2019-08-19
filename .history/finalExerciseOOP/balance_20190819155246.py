class Balance:
    def __init__(self,initial_balance):
        self.__balance = initial_balance
    
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        self.__balance += amount
    def show_balance(self):
        return self.__balance  
    def transfer(self, amount):
        

class CheckingAcct(Balance):
    
    def __init__(self, inital_balance):
        Balance.__init__(self, inital_balance)

class SavingsAcct(Balance):
    
    def __init__(self, inital_balance):
        Balance.__init__(self, inital_balance)