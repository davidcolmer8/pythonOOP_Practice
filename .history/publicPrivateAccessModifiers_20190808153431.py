class Cust:
    def __init__(self, fName,lName):
        self.__firstName = fName
        self.__lastName = lName

    def setName(self, first_Name, l_Name ):
        self.__firstName = first_Name
        self.__lastName = l_Name

    def getName(self,firstName, lastName):
        return self._Cust__firstName,self._Cust__lastName

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
    print(customer1.getName())

    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    # print('aaaa', acct.getBalance()) 

main()