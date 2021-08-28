print("Welcome to Bank of TK ATM")
restart = "Y"
chances = 3
balance = 100
while chances >= 0:
    pin = int(input("Please enter you 4 digit pin:"))
    if pin == 1234:
        print("You entered your pin Correctly\n")
        while restart not in ("n", "NO", "no", 'N'):
            print("Please Press 1 for Your Balance \n")
            print("Please Press 2 for withdraw \n")
            print("Please Press 3 for Pay in \n")
            print("Please Press 4 for Return Card \n")
            option = int(input("What would you like to choose?"))
            if option == 1:
                print("Your balance is ", balance, '\n')
                restart = input('would you like to go back?')
                if restart in ("n", "NO", "no", 'N'):
                    print("thank you")
                    break
            elif option == 2:
                option2 = "y"
                withdrawl = float(input("how much would you like to withdrawl "))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print('\n Your balance is now Rs.', balance)
                    restart = input("would you like to go back?")
                    if restart in ("n", "NO", "no", "N"):
                        print("thank you")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("Invalid amount, Please Re-try\n")
                    restart = 'y'
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))
            elif option == 3:
                Pay_in = float(input("How much would you like to pay in?"))
                balance = balance + Pay_in
                print('\n Your balance is Rs.', balance)
                restart = input('Would you like to go back?')
                if restart in ("n", "NO", "no", 'N'):
                    print('Thank you')
                    break
            elif option == 4:
                print('Please wait while your card is Returned....\n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number \n')
                restart = 'y'
    elif pin != '1234':
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\n No more tries')
            break
