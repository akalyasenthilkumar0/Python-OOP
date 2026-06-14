#------------------------------------------------------------------------------------------------------------------
#--------------------------------------------Bank Manangement System-----------------------------------------------
#------------------------------------------------------------------------------------------------------------------

class BankAccount:
  def __init__(self,name,balance=0):
    self.name = name
    self.__balance = balance

 def deposit(self,amount):
   self.__balance += amount
   print("Amount deposited successfully")

def withdraw(self,amount):
  if amount <= self.__balance:
    self.__balance -= amount
    print("Withdrawal Successful")
  else:
    print("Insufficient Balance")

def checkbalance(self):
  print("User:",self.name)
  print("Balance:",self.__balance)

name = input("Enter Account Holder's Name :")
acc = BankAccount(name)

while True:
  print("\n====================Bank Management System========================")
  print("1.Deposit")
  print("2.Withdraw")
  print("3.CheckBalance")
  print("4.Exit")

  choice = int(input("Enter your choice:"))

  if choice == 1:
    amount = float(input("Enter amount:"))
    account.deposit(amount)

  elif choice == 2:
    amount = float(input("Enter amount:"))
    account.withdraw(amount)

  elif choice == 3:
    account.check_balance()

  elif choice == 4:
    print("Thank you for using the Bank Management System")
    break

  else:
    print("Invalid Choice!")

#---------------------------------------------------------------------------------------------------------------------
  
                         
