class BankAcct:
    def __init__(self, initBalance):
        self.__balance = initBalance
    
    def getBalance(self):
        return self.balance

def main():

    acct = BankAcct(500)

    print('current',acct.getBalance())
    acct.balance += 500
    print('new', acct.getBalance()) 

main()