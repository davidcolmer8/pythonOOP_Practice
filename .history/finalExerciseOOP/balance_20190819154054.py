class Balance:
    def __init__(self,initial_balance):
        self.__balance = initial_balance
    
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        self.__balance += amount
    def show_balance(self):
        return init