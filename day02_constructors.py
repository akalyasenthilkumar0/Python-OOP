#------------------------------------------------------------------------------------------------------------------
#CONSTRUCTORS
#------------------------------------------------------------------------------------------------------------------

#1.Student class with Constructor

class Student:
  def __init__(self,name,department):
    self.name=name
    self.department=department
s1=Student("Nik","CSE")
print("Name:", s1.name)
print("Department:",s1.department)

#-------------------------------------------------------------------------------------------------------------------

#2.Book class 

class Book:
  
  def __init__(self,title,author):
    
    self.title=title
    self.author=author

b_1=Book("Physics with Fun","RajeshKumar")

print("Title:",b_1.title)
print("Author:",b_1.author)

#---------------------------------------------------------------------------------------------------------------------

#3.Employee Class with Constructor

class Employee:

  def __init__(self,name,salary):

    self.name=name
    self.salary=salary

e1=Employee("Lalith",5000000)
print("\nName:",e1.name, "\nSalary:",e1.salary)

#----------------------------------------------------------------------------------------------------------------------

#4.Area of Rectangle with Constructor and Method

class Rectangle:

  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth

  def display_area(self):
    print("Length:",self.length , "Breadth:",self.breadth)
    area = length * breadth
    print("Area of the Rectangle:", area)    

r1 = Rectangle(14,6)
r2 = Rectangle(45,9)
r3 = Rectangle(60,12)

r1.display_area()
r2.display_area()
r3.display_area()

#------------------------------------------------------------------------------------------------------------------------
