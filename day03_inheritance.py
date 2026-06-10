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

class Food:
    def eating(self):
        print("I'm Eating my favorite food.")
class Healthy_Food(Food):
    def eating_1(self):
        print("Eating healthy is good.")
class Fruits(Healthy_Food):
    def eating_2(self):
        print("I like to eat fruits")
grape=Fruits()
grape.eating()
grape.eating_1()
grape.eating_2()

#--------------------------------------------------------------------------------------------------------------------

#4.Hierarchical Inheritance 

class shape:
    def shape_name(self):
        print("Shapes:")
class twodim(shape):
    def shape_1(self):
        print("2 Dimensional Shape")
class threedim(shape):
    def shape_2(self):
        print("3 Dimensional Shape")
s1=twodim()
s2=threedim()
s1.shape_name()
s1.shape_1()
s2.shape_2()

#--------------------------------------------------------------------------------------------------------------------

#5.Hybrid Inheritance 

class games:
    def display(self):
        print("My hobby is playing."
        print("Games are classified into two types.")
class indoorgames(games):
    def chess(self):
        print("Chess is an indoor game.")
class outdoorgames(games):
    def football(self):
        print("Football is an outdoor game.")
class nationalgame(outdoorgames,games):
    def hockey(self):
        print("Hockey is our national game.")
sports=nationalgame()
sports.display()
sports.football()
sports.hockey()

#--------------------------------------------------------------------------------------------------------------------