#------------------------------------------------------------------------------------------------------------------
#Inheritance 
#------------------------------------------------------------------------------------------------------------------

#1.Sinlge Inheritance

class Vehicle:
  def move(self):
    print("Vehicle started moving")

class Car(Vehicle):
  def start(self):
    print("Car started to move")

v1 = Car()
v1.move()
v1.start()

#-------------------------------------------------------------------------------------------------------------------

#2.Multiple Inheritance 

class Zoo:
  def name(self):
    print("Name of the Zoo is ZIGZAG")

class Animal:
  def ani(self):
    print("This Zoo contains more than 50 animals")

class WildAnimal(Zoo,Animal):
  def wildani(self):
    print("Count of wild animals:30")

ob = WildAnimal()
ob.name()
ob.ani()
ob.wildani()

#--------------------------------------------------------------------------------------------------------------------

#3. Multilevel Inheritance




