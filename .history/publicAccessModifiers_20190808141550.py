class BankAcct:
    def __init__(self, initBalance):
        self.Balance = initBalance
    
    def getBalance(self):
        return self.balance

def main():

    acct = BankAcct(500)

    print('current',acct.getBalance())
    acct.balance += 342524352345
    print('new', acct.getBalance()) 

main()