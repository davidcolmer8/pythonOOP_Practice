import csv

    
class Cust:
    def __init__(self,fName,lName,acctNum,balance):
        self.firstName =fName
        self.lastName =lName
        self.__acctNum = acctNum
        self.__balance = balance

    def getDescription(self):
        print("First Name:" +self.firstName, self.lastName , self.__acctNum, self.__balance)

        
    def __del__(self):
        pass


def main():
    
    my_Customers = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            my_Customers.append(Cust(row[0],row[1],row[2],row[3]))
           
            print(my_Customers[0].getDescription())
            


    # acct = BankAcct(500)
    # acct.deposit(500)

    # print('current',acct.balance())
   
    # print('aaaa', acct.getBalance()) 

main()