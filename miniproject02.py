#------------------------------------------------------------------------------------------------------------------
#---------------------------------------LIBRARY MANAGEMENT SYSTEM--------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

class library:
  
  def __init__(self):
    self.books = []
    
  def add_book(self,book):
    self.books.append(book)
    print("Book Added!")

  def view_books(self):
    if len(self.books) == 0 :
      print("No books available")
    else:
      print("Available Books are listed below:")
      for book in self.books:
        print(book)

   def search_book(self):
     if book in self.books:
       print("Found")
     else:
       print("Not Found")

   def remove_book(self):
     if book in self.books:
       self.books.remove(book)
       print("Boook Removed Successfully")
     else:
       print("Book Not Found")
       

lib = library()

while True:
  print("\n=====================Library Management System=========================")
  print("1.Add")
  print("2.View Book")
  print("3.Search Book")
  print("4.Remove Book")
  pritn("5.Exit")

  choice = int(input("Enter your choice:"))

  if chocie == 1:
    book = input("Enter book name:")
    library.add_book(book)

  elif choice == 2:
    library.view_books()

  elif choice == 3:
    book = input("Enter book name:")
    library.search_book(book)

  elif choice == 4:
    book = input("Enter book name:")
    library.remove_book(book)

  elif choice == 5:
    print("Thankyou for using the Library Management System")
    break

  else:
    print("------Invalid Chocie------")

#--------------------------------------------------------------------------------------------------------------------
