accountNamesList = []
accountBalanceList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalanceList, accountPasswordsList
    accountNamesList.append(name)
    accountBalanceList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalanceList, accountPasswordsList
    print(f"Account:{accountNumber}")
    print(f"Name: {accountNamesList[accountNumber]}")
    print(f"Balance: {accountBalanceList[accountNumber]}")
    print(f"Password: {accountPasswordsList[accountNumber]}")
    print()


def getBalance(accountNumber, password):
    global accountNamesList, accountsBalanceList, accountPasswordsList

    if password != accountPasswordsList[accountNumber]:
        print("Incorrect Password")
        return None
    return accountBalanceList[accountNumber]


def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountsBalanceList, accountPasswordsList
    if amountToDeposit < 0:
        print("You cannot deposit a negative amount.")
        return None

    if password != accountPasswordsList[accountNumber]:
        print("Incorrect Password")
        return None

    accountBalanceList[accountNumber] = accountBalanceList[accountNumber] + \
        amountToDeposit
    return accountBalanceList[accountNumber]


def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList

    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountBalanceList[accountNumber]:
        print('You cannot withdraw more than you have in your account')
        return None

    accountBalanceList[accountNumber] = accountBalanceList[accountNumber] - \
        amountToWithdraw
    return accountBalanceList[accountNumber]

# Create two sample accountss


print(f"Joe's account number is:", len(accountNamesList))
newAccount("Joe", 100, "soup")

print("Mary's accout number is:", len(accountNamesList))
newAccount("Mary", 12345, "nuts")

while True:
    print()
    print("Press b to get the balance")
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == "b":
        print("Get balance: ")

    userAccountNumber = input("Please enter your account number: ")
    userAccountNumber = int(userAccountNumber)
    userPassword = input("Please enter the password: ")
    theBalance = getBalance(userAccountNumber, userPassword)

    if theBalance is not None:
        print(f"Your balance is: {theBalance}")

    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(
            userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input(
            'What is the amount of your initial deposit? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input(
            'What password would you like to use for this account? ')

        userAccountNumber = len(accountNamesList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':  # show all
        print('Show:')
        nAccounts = len(accountNamesList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(
            userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

print('Done')
