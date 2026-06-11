#------------------------------------------------------------------------------------------------------------------
#Abstarction
#------------------------------------------------------------------------------------------------------------------

#1.Basic Abstarction 

from abc import ABC, abstarctmethod

class Vehicle(ABC):
  @abstarctmethod 
  def start(self):
    pass

class Car(Vehicle):
  def start(self):
    print("Car Started")

c = Car()
c.start()

#----------------------------------------------------------------------------------------------------------------

#2.Employee class with Abstarction 

from abc import ABC, abstractmethod

class Employee(ABC):
  @abstarctmethod
  def work(self):
    pass

class Software_developer(Employee):
  def work(self):
    print("Builds the Software.")

class Hardware_developer(Employee):
  def work(self):
    print("Builds the Hardware.")

s = Software_developer()
h = Hardware_developer()
s.work()
h.work()

#---------------------------------------------------------------------------------------------------------------

  
  
