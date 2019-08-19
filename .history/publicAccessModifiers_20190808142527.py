class BankAcct:
    def __init__(self, initBalance):
        self.__balance = initBalance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amountDep):
        self.__balance += amountDep

def main():

    acct = BankAcct(500)

    # print('current',acct.balance())
    acct.balance += 500
    print('new', acct.getBalance()) 

main()