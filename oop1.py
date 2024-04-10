from opp import *

Dave = BankAccount(1000,"Dave")
Sara = BankAccount(1000,"Sara")

# Dave.getBalance()
# Dave.getBalance()
# Sara.getBalance()
# Sara.getBalance()
# Dave.deposit(100)
# Sara.deposit(12)
# Dave.getBalance()
# Sara.getBalance()
# Dave.withdraw(10)


# Dave.Transfer(10,Sara)

jim = IntrestReward(1000,'jim')

# jim.getBalance()
# jim.deposit(100)
# jim.Transfer(100,Dave)

joy = BankAccount(9842,'joy')
joy.getBalance()
joy.deposit(100)
joy.Transfer(100,jim)
joy.withdraw(100)