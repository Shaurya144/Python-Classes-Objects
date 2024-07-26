# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
    name = "";

# create an object using the Person class
John = Person()
John.name = "John James Jonason"

# The __init__() Function
# this is quite important 

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created

class AnotherPerson:
  def __init__(self, name, age): # define variables assosiated with the object
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
  
  # You can also give classse functions
  def CallName(self):
    print("Hello my name is " + self.name)


p1 = AnotherPerson("John", 36) # assign those variables a value

print(p1.name)
print(p1.age)


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string

# you can call Class functions by
Customer50124 = AnotherPerson()
Customer50124.name = "Timothy Templeton"

Customer50124.CallName()

# The self parameter is like an placeholder variable, yet to have a value assigned to it
# You can name it anything, doesn't just have to be "self"
