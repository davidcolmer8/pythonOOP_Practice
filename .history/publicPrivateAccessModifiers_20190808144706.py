class Cust:
    def _
class BankAcct:
    def __init__(self, initBalance):
        self.__balance = initBalance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amountDep):
        self.__balance += amountDep
    def __del__(self):
        pass

def main():

    acct = BankAcct(500)
    acct.deposit(500)

    # print('current',acct.balance())
    print('new', acct.getBalance()) 
    del(acct)
    print('aaaa', acct.getBalance()) 

main()