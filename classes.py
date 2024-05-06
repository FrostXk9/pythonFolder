# A class is like a blueprint for creating objects. An object has properties a methods(functions) associated with it. Almost everything in python is an object

# Create class
class User:
    # constructor
    # a constructor is a function that runs when you instantiate an object from a class
    def __init__(self, name, email, age):
        # in JS we use 'this' in python we use 'self'
        self.name = name
        self.email = email
        self.age = age
        
        
    def greeting(self):
        return f"my name is {self.name} and my age is {self.age}"
    
    
    
    def has_birthday(self):
        self.age +=1
     
     
     
# Extend class
class Customer(User):   
        def __init__(self, name, email, age):
            # in JS we use 'this' in python we use 'self'
            self.name = name
            self.email = email
            self.age = age
            self.balance = 0
            
        def set_balance(self, balance):
            self.balance = balance
              
        
        def greeting(self):
            return f"my name is {self.name} and my age is {self.age} and my balance is {self.balance}"
        
        
        
        
        
# initialize user object
brandon = User("Brandidilidon", "brand@gmail.com", 20)


# initialize a customer

janet = Customer('janet jones', 'janet@gmail.com', 25)
janet.set_balance(500)
janet.greeting()



brandon.has_birthday()

print(brandon.greeting())

# extended class can still access parent calss
print(janet.greeting())