import pywriter as pw

def ATMScreen ():

    balance = 500
    active = True

    while active == True:
        menu = input("""
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. Exit

        Enter your option: """)

        if menu == "1":
            print ("Your standing balance is: £", balance)

        elif menu == "2":
            deposit = int(input("How much would you like to deposit?\n Amount: "))
            balance = balance + deposit
            print ("You deposited: ", deposit,"\nYour new balance is: ", balance)

        elif menu == "3":
            withdraw = int(input("How much would you like to withdraw?\nAmount: "))
            if withdraw > balance:
                print ("\nInsufficent Funds")
            else:
                balance = balance - withdraw
                print ("\nYou withdrew: ", withdraw, "\nYour new balance is: ", balance)

        elif menu == "4":
            ("\nATM Terminated")
            active = False

ATMScreen()

