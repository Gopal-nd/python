class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\n Balence = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\n '{self.name}' Balence = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance+=amount
        print('\n Deposit Completed')
    
    def viableTrax(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n Sorry ,account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self,amount):
        try:
            self.viableTrax(amount)
            self.balance-=amount
            print("\n Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def Transfer(self,amount,account):
        try:
            print('\n*********** \n\n Biginning Transfer...🚀')
            self.viableTrax(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transaction completed ✅')
        except BalanceException as error:
            print(f'\n transfer interrupted : {error}')


class IntrestReward(BankAccount):
    def deposit(self, amount):
       self.balance += (amount *1.05) 
       print("\n Deposit Completed")
       self.getBalance()