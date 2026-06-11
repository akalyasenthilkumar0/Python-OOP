#------------------------------------------------------------------------------------------------------------------
#Polymorphism 
#------------------------------------------------------------------------------------------------------------------

#1.Method Overriding with a single child class

class Animal:
  def sound(self):
    print("Sound of an animal")

class Dog(Animal):
  def sound(self):
    print("Dog Barks")

d = Dog()
d.sound()

#--------------------------------------------------------------------------------------------------------------------

#2.Method Overriding with multiple child class

class Employee:
  def work(self):
    print("Works good")

class Manager(Employee):
  def work(self):
    print("Manages all the activities.")

class Tester(Employee):
  def work(self):
    print("Tests the products before manufacturing.")

m = Manager()
t = Tester()

m.work()
t.work()

#--------------------------------------------------------------------------------------------------------------------

#3.Payment System 

class Payment:
  def pay(self):
    print("Payment in process")

class creditcard(Payment):
  def pay(self):
    print("Payment done by using Creditcard.")

class UPI(Payment):
  def pay(self):
    print("Payment done by using UPI.")

c = creditcard()
a = UPI()

c.pay()
a.pay()

#---------------------------------------------------------------------------------------------------------------------

#4.Onile shopping

class shopping_onile:
  def usage(self):
    print("The rate of Online shopping increased gardually.")

class male_users(shopping_online):
  def usage(self):
    print("70% of men prefers Online shopping.")

class female_users(shopping_online):
  def usage(self):
    print("90% of women prefers to shop online.")

ob1 = male_users()
ob2 = female_users()

ob1.usage()
ob2.usage()

#-----------------------------------------------------------------------------------------------------------------------

    
