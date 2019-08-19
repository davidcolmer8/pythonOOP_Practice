class Cust:
    def __init__(self, fName, lName):
        self.__firstName =  fName
        self.__lastName = lName
    def getName():
        return _Cust__firstName, _Cust__lastName

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
    customer1 = Cust('Vicotor', 'Davis')
    acct = BankAcct(500)
    acct.deposit(500)

    # print('current',acct.balance())
   
    print('aaaa', acct.getBalance()) 

main()