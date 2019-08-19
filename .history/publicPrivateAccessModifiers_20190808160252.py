class Cust:
    def __init__(self):
        self.firstName =""
        self.lastName =""

    def setName(self, first_Name, l_Name ):
        self.firstName = first_Name
        self.lastName = l_Name

    def getName(self):
        print( 'First name: '+ self.firstName,'\nLast name: ' + self.lastName)

class BankAcct:
    def __init__(self, acctNum):
        self.__accountNumber = acctNum
    
    def getBalance(self):
        priint ( self.__balance
    
    def deposit(self, amountDep):
        self.__balance += amountDep

    def __del__(self):
        pass

def main():
    customer1 = Cust()
    customer1.setName('Victor','Davis')
    customer1.getName()

    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    # print('aaaa', acct.getBalance()) 

main()