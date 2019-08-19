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
        self.__acctNumber = acctNum
    
    def getBalance(self):
        print( self.__acctNumber)
    
    # def deposit(self, amountDep):
    #     self.__balance += amountDepd

    def getDescription(self):
        self.getBalance()
        Cust.getName(self)
        

    def __del__(self):
        pass


def main():
    
    my_Customers = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            my_Customers.append(Cust().setName(),BankAcct(row[2]))


    
    customer = BankAcct(10011)
    customer.setName('bob','joe')

    customer.getDescription()


    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    # print('aaaa', acct.getBalance()) 

main()