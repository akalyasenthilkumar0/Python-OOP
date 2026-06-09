#------------------------------------------------------------------------------------------------------------------
# classes and objects
#------------------------------------------------------------------------------------------------------------------

#1. Car class with methods

class Car:
  
  def start(self):
    print("Car Started.")

c1 = Car()
c1.start()

#------------------------------------------------------------------------------------------------------------------

#2.Student class with attributes

class Student:

s1 = Student()

s1.name = "Sid"
s1.age = 19

print("Name:", s1.name)
print("Age:", s1.age)

#------------------------------------------------------------------------------------------------------------------

#3.Book class

class Books:
  
  def details(self, name, author, price):
    self.name = name
    self.author = author
    self.price = price
    
b1 = Books()
b2 = Books()

b1.details("Mountains and Rivers","Willey",500.00)
b2.details("Next to you","Harry", 750.00)

print("\nTitle:", b1.name, "\nAuthor:", b1.author, "\nPrice:", b1.price)
print("\nTitle:", b2.name, "\nAuthor:", b2.author, "\nPrice:", b2.price)

#--------------------------------------------------------------------------------------------------------------------

#4. Rectangle class

class Rectangle:
  
  def area(self,length,breadth):
    self.length = length
    self.breadth = breadth 
    
  def show_area(self):
    print("\nLength=", self.length, "\nBreadth=", self.breadth)
    res = self.length * self.breadth
    print("Area of the Rectangle:",res)
    
R1 = Rectangle()
R2 = Rectangle()

R1.area(12, 3)
R2.area(50,25)

R1.show_area()
R2.show_area()




    

