import csv

    
class Cust:
    def __init__(self,fName,lName,acctNum,balance):
        self.firstName =fName
        self.lastName =lName
        self.acctNum = acctNum
        self.balance = balance

    def getDescription(self):
        print( 'First name: '+ self.firstName,'\nLast name: ' + self.lastName + self.balance())

        
    def __del__(self):
        pass


def main():
    
    my_Customers = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            my_Customers.append(Cust(row[0],row[1],row[2],row[3]))
            print(type(Cust))
            
            print(my_Customers)
            


    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    # print('aaaa', acct.getBalance()) 

main()