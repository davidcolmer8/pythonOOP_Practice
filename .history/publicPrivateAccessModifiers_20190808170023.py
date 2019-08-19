import csv

    
class Cust:
    def __init__(self,fName,lName,acctNum,balance):
        self.firstName =""
        self.lastName =""
        self.__acctNum = ""
        self.__balance = ""

    def getName(self):
        print( 'First name: '+ self.firstName,'\nLast name: ' + self.lastName + )
        print( 'First name: '+ self.firstName,'\nLast name: ' + self.lastName + )

    def getDescription(self):
        

    def __del__(self):
        pass


def main():
    
    my_Customers = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            my_Customers.append(BankAcct(row[2]))
            Cust.setName(my_Customers[0],my_Customers[1])

    Cust.getDescription()


    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    # print('aaaa', acct.getBalance()) 

main()