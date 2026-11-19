#4. Bank Account System (Class, Object, Constructor) 
#A bank wants to manage customer accounts. Create a BankAccount class with a constructor to initialize account number and balance. Implement methods to deposit, 
#withdraw, and display balance. 





class BankAccount:
    def __init__(self,ac_num,balance):
        self.ac_num=ac_num
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposited Amount",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Withdraw Amount:",amount)
        else:
            print("Insufficient Balance")
    def display_balance(self):
        print("Account Number:",self.ac_num)
        print("Balance:",self.balance)
a1=BankAccount(3215678,60000)
a2=BankAccount(4328762,40000)
print("Account Details")
a1.display_balance()
a2.display_balance()
a3.display_balance()
a1.deposit(3000)
a1.display_balance()
a2.withdraw(4000)
a2.display_balance()
