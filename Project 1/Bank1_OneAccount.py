# Non-OOP
# Bank Version 1
# Single Account

accountName = "Joe"
accountBalance = 100
accountPassword = "soup"

while True:
    print()
    print("Press b to get the balance")
    print("press d to make a deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action = input("What do you want to do? ")
    action = action.lower()  # Force lowercase
    action = action[0]
    print()

    if action == "b":
        print("Get Balance:")
        userPassword = input("Please enter the password: ")
        if userPassword != accountPassword:
            print("Incorrect password")
        else:
            print(f"Your balance is {accountBalance}")

    elif action == "d":
        print("Deposit:")
        userDepositAmount = input("Please enter amount to deposit: ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enter the password: ")

        if userDepositAmount < 0:
            print("You cannnot deposit a negative amount!")

        elif userPassword != accountPassword:
            print("Incorrect Password")

        else:
            accountBalance = accountBalance + userDepositAmount
            print(f"Your new balance is {accountBalance}")

    elif action == "s":
        print("Show: ")
        print(f"Name,{accountName}")
        print(f"Balance, {accountBalance}")
        print(f"Password, {accountPassword}")
        print()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")

        userWithdrawAmount = input("Please enter the amount to withdraw: ")
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input("Please Enter Password: ")

        if userWithdrawAmount < 0:
            print("You cannot withdraw a negative amount")

        elif userPassword != accountPassword:
            print("Incorrect Password for this account")

        elif userWithdrawAmount > accountBalance:
            print("You cannot withdraw more than you have in your account")

        else:
            accountBalance = accountBalance - userWithdrawAmount
            print(f"Your new balance is {accountBalance}")
print("Done")
