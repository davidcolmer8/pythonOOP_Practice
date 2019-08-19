import csv

    
class Cust:
    def __init__(self):
        self.firstName =""
        self.lastName =""

    def setName(self, first_Name, l_Name ):
        self.firstName = first_Name
        self.lastName = l_Name

    def getName(self):
        print( 'First name: '+ self.firstName,'\nLast name: ' + self.lastName)

class BankAcct(Cust):
    def __init__(self, acctNum):
        self.__balance = acctNum
    
    def getBalance(self):
        print( self.__balance)
    
    # def deposit(self, amountDep):
    #     self.__balance += amountDepd

    

    def __del__(self):
        pass

def main():
   customer= BankAcct(10011)
   customer.setName('bob','joe')

   customer.getBalance()
   customer.getName()


    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    # print('aaaa', acct.getBalance()) 

main()