# Non-OOP
# Bank 2
# Single account

accountName = ""
accountBalance = 0
accountPassword = ""


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print(f"Name, {accountName}")
    print(f"Balance, {accountBalance}")
    print(f"Password, {accountPassword}")
    print()


def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print("Incorrect Password")
        return None
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print("You cannont deposit a negative amount")
        return None

    if password != accountPassword:
        print("Incorrect Password")
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print("You cannot withdraw a negative amount")
        return None

    if password != accountPassword:
        print("Incorrect password for this account!")
        return None

    if amountToWithdraw > accountBalance:
        print("You cannot withdraw more than you have in your account")
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


newAccount("Joe", 100, "soup")  # create an account

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action = input("What do you want to do?")
    action = action.lower()  # force lowercase
    action = action[0]
    print()

    if action == "b":
        print("Get balance:")
        userPassword = input("Please enter the password: ")
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print(f"Your balance is: {theBalance}")

    elif action == "d":
        print("Deposit: ")
        userDepositAmount = input("Please enter amount to deposit: ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enter the password: ")

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print(f"Your new balance is: {newBalance}")

    elif action == "s":
        print("Show: ")
        print(f"Name,{accountName}")
        print(f"Balance, {accountBalance}")
        print(f"Password, {accountPassword}")
        print()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw: ")
        userWithdrawAmount = input("Please how much do you want to withdraw: ")
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input("Please enter your password: ")

        if userWithdrawAmount < 0:
            print("Please you can't withdraw negative amount: ")

        elif userPassword != userPassword:
            print("Incorrect password")

        elif userWithdrawAmount > accountBalance:
            print("You can't withdraw more than you have in your account")

        else:
            accountBalance = accountBalance = userWithdrawAmount
            print(f"Your new balance is: {accountBalance} ")
