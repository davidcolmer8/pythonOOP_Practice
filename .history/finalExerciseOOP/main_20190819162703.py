import balance


def main():
    currentAcct = finalExerciseOOP.balance.CheckingAcct(1000)
    savingsAcct = finalExerciseOOP.balance.SavingsAcct(500)

    print(currentAcct.show_balance)
    print(savingsAcct.show_balance)

    currentAcct.transfer(100,currentAcct,savingsAcct)
    
    print(currentAcct.show_balance)
    print(savingsAcct.show_balance)


main()