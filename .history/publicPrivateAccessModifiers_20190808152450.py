class Cust:
    def __init__(self):
        self.__firstName 
        self.__lastName

    def setName(self, firstName, lastName ):
        self._Cust__firstName = firstName
        self._Cust__lastName = lastName

    def getName(self):
        return 

class BankAcct:
    def __init__(self, acctNum):
        self.__accountNumber = acctNum
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amountDep):
        self.__balance += amountDep

    def __del__(self):
        pass

def main():
    customer1 = Cust()
    customer1.setName('Victor','Davis')

    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    print('aaaa', acct.getBalance()) 

main()