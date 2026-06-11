#------------------------------------------------------------------------------------------------------------------
#Encapsulation
#------------------------------------------------------------------------------------------------------------------

#1.Public class variable 

class Employee:
  def __init__(self):
    self.name = "Harish"

e = Employee()
print(e.name)

#-------------------------------------------------------------------------------------------------------------------

#2.Private class variable

class Employee:
  def __init__(self):
    self._name = "Harish"

e = Employee()
print(e._name)

#--------------------------------------------------------------------------------------------------------------------

#3.Protected class variable 

class Employee:
  def __init__(self):
    self.__name = "Harish"
  def display(self):
    print(self.__name)

e = Employee()
e.display()

#--------------------------------------------------------------------------------------------------------------------

#4.Bank Deposit

class BankAccount:
  def __init__(self):
    self.__balance = 50500
  def deposit(self,amount):
    self.__balance += amount
  def show_balance(self):
    print("Balance:" ,self.__balance)

b = BankAccount()
b.deposit(2200)
b.show_balance()

#---------------------------------------------------------------------------------------------------------------------

