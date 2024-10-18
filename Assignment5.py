#Assignment 1: Static Methods
#Create a class MathOperations that contains:
#A static method add_numbers that takes two arguments and returns their sum.
#A static method multiply_numbers that takes two arguments and returns their product.

class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

# Example usage:
sum_result = MathOperations.add_numbers(5, 3)
product_result = MathOperations.multiply_numbers(5, 3)

print(f"Sum: {sum_result}")
print(f"Product: {product_result}")

#Assignment 2: Class Methods
#Create a class Person that keeps track of the number of people created. The class should have:
#A class variable count to count instances of the class.
#A class method get_count that returns the current count.


class Person:
    # Class variable to keep track of the number of instances
    count = 0

    def __init__(self):
        # Increment the count each time a new Person instance is created
        Person.count += 1

    @classmethod
    def get_count(cls):
        # Return the current count of Person instances
        return cls.count

# Example usage:
p1 = Person()
p2 = Person()
p3 = Person()

print(f"Number of people created: {Person.get_count()}")  # Output: Number of people created: 3

#Assignment 3: Using Both Static and Class Methods
#Create a class TemperatureConverter with the following:
#A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
#A class method info that returns a message about temperature conversions.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @classmethod
    def info(cls):
        """Return information about temperature conversions."""
        return "This class provides methods for converting temperatures between Celsius and Fahrenheit."

# Example usage:
temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)
info_message = TemperatureConverter.info()

print(f"25°C is {temp_in_fahrenheit}°F")
print(info_message)

#Assignment 4: Single Inheritance
#Create two classes:
#Animal with a method sound that prints "Animal sound".
#Dog that inherits from Animal and overrides the sound method to print "Bark".

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Example usage:
generic_animal = Animal()
generic_animal.sound()  # Output: Animal sound

dog = Dog()
dog.sound()  # Output: Bark

#Assignment 5: Multiple Inheritance
#Create two classes:
#Bird with a method fly that prints "Flying".
#Fish with a method swim that prints "Swimming".
#A class Duck that inherits from both Bird and Fish.

class Bird:
    def fly(self):
        print("Flying")

class Fish:
    def swim(self):
        print("Swimming")

class Duck(Bird, Fish):
    pass

# Example usage:
duck = Duck()
duck.fly()    # Output: Flying
duck.swim()   # Output: Swimming


#Assignment 6: Abstract Class
#Use the abc module to create an abstract class Shape that contains:
#An abstract method area().
#Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method.
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of the circle: {circle.area():.2f}")  # Output: Area of the circle: 78.54
print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of the rectangle: 24

#Assignment 7: Encapsulation
#Create a class BankAccount that uses encapsulation:
#Private attributes _balance.
#Public methods deposit() and withdraw() that modify _balance safely.

class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self._balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self._balance

# Example usage:
account = BankAccount(100)  # Initial balance of 100
account.deposit(50)         # Deposit 50, new balance 150
account.withdraw(30)        # Withdraw 30, new balance 120
print(f"Current balance: {account.get_balance()}")  # Output: Current balance: 120

#Assignment 8: Polymorphism with Method Overriding
#Create two classes Cat and Dog with a method speak().
#The Dog class should implement speak() to print "Woof".
#The Cat class should implement speak() to print "Meow"

class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

# Example usage:
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

#Assignment 9: Polymorphism with Method Overloading
#Create a class Calculator with a method add() that:
#Can accept 2 or 3 arguments and returns their sum.
#Hint: Use default parameters to handle method overloading in Python.

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Example usage:
calc = Calculator()

# Add two numbers
result_2_args = calc.add(10, 5)
print(f"Sum of 10 and 5: {result_2_args}")

# Add three numbers
result_3_args = calc.add(10, 5, 3)
print(f"Sum of 10, 5, and 3: {result_3_args}")

#Assignment 10: Multilevel Inheritance
#Create three classes:
#LivingBeing with a method breathe() that prints "Breathing".
#Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
#Human that inherits from Mammal and adds a method think() that prints "Thinking".

class LivingBeing:
    def breathe(self):
        print("Breathing")

class Mammal(LivingBeing):
    def walk(self):
        print("Walking")

class Human(Mammal):
    def think(self):
        print("Thinking")

# Example usage:
human = Human()

# Calling methods from all levels of the inheritance hierarchy
human.breathe()
human.walk()
human.think()
