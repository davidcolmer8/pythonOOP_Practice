import balance


def main():
    currentAcct = balance.CheckingAcct(1000)
    savingsAcct = balance.SavingsAcct(500)

    print(currentAcct.show_balance())
    print(savingsAcct.show_balance())

    currentAcct.transfer(1001,currentAcct,savingsAcct)
    
    print(currentAcct.show_balance())
    print(savingsAcct.show_balance())


main()