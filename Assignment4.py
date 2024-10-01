# #1-Write a Python program to create a class named Car.
# # Define attributes like brand, model, and year.
# # Create an object of the class and display the details of the car
#
# #Define the Car Class
# class Car:
# # Defining the Constructor
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
# # Defining a Method to Display Car Details
#     def display_details(self):
#         print(f"Car Details:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}")
#
# # Create an object of the Car class
# my_car = Car("Toyota", "Corolla", 2024)
#
# # Display the details of the car
# my_car.display_details()
#
# #2.Create a class Student with attributes name, roll_number, and marks.
# # Define a constructor to initialize these attributes and a method display_info() to print the student's details
#
# #define a class
# class Student:
#  #Defining the Constructor
#     def __init__(self,name,roll_number,marks):
#         self.name=name
#         self.roll_number=roll_number
#         self.marks=marks
#
#  # Defining a Method to Display student Details
#     def Student_Details(self):
#         print(f"Student Details:\nName: {self.name}\nRoll Number: {self.roll_number}\nMarks: {self.marks}")
# # Create an object of the Student  class
# student1=Student("Anuj",12,91)
# # Display the details of the Student
# student1.Student_Details()
#
# #3.Create a class Rectangle with attributes length and breadth.
# # Include methods to calculate the area and perimeter of the rectangle.
# # Create multiple objects and display the area and perimeter for each
#
# # Define the Rectangle class
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#
# # Method to calculate the perimeter of the rectangle
#     def perimeter(self):
#         return 2*(self.length+self.breadth)
#
# # Method to calculate the area of the rectangle
#
#     def area(self):
#         return self.length*self.breadth
#
#     # Method to display the area and perimeter
#
#     def display(self):
#         print(f"Rectangle with Length: {self.length} and Breadth: {self.breadth}")
#         print(f"Area: {self.area()}")
#         print(f"Perimeter: {self.perimeter()}")
#         print("-" * 30)
# # Create multiple objects of the Rectangle class
# rect1 = Rectangle(5, 3)
# rect2 = Rectangle(10, 2)
# rect3 = Rectangle(7, 4)
#
# # Display area and perimeter for each rectangle
# rect1.display()
# rect2.display()
# rect3.display()

##4.Write a class Circle with an attribute radius and methods get_area() and get_circumference().
# These methods should return the area and circumference of the circle, respectively

# Define the Circle class
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
# # Defining the method
#     def get_area(self):
#         pi = 3.14
#         return pi*self.radius**2
#
#     # Defining the method
#     def get_circumference(self):
#         pi = 3.14
#         return 2*pi*self.radius
#
# # Create a circle with a radius of 5
# circle = Circle(10)
# # Get the area
# print("Area:", circle.get_area())
#
# # Get the circumference
# print("Circumference:", circle.get_circumference())

##5.Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

# #Define the Account class
# class Account:
#     def __init__(self, account_no, balance=0):
#         self.account_no = account_no
#         self.balance = balance
#
#     def credit(self, amount):
#         """Adds the specified amount to the account balance."""
#         if amount > 0:
#             self.balance += amount
#             print(f"Amount credited: {amount}")
#         else:
#             print("Invalid amount. Please enter a positive number.")
#
#     def debit(self, amount):
#         """Subtracts the specified amount from the account balance if sufficient funds are available."""
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Amount debited: {amount}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Invalid amount. Please enter a positive number.")
#
#     def print_balance(self):
#         """Prints the current account balance."""
#         print(f"Current balance for account {self.account_no}: {self.balance}")
#
# # Creating an Account object
# account1 = Account(account_no=12345, balance=100000)
# account2 = Account(account_no=50162841, balance=500000)
# # Adding 500 to the account
# account1.credit(55000)
# account2.credit(55000)
# account1.debit(50000)
# account2.debit(50000)
# # Printing the balance
# account1.print_balance()
# account2.print_balance()

#6.Create a class Employee with an attribute employee_count (class variable)
# and a class method increment_employee_count()
# to increase the count whenever a new employee object is created.
# Show the updated employee count after creating new objects.

#Creating Class Employee
# class Employee:
#     # Class variable to track the number of employees
#     employee_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         # Increment the employee count when a new object is created
#         Employee.increment_employee_count()
#
#     @classmethod
#     def increment_employee_count(cls):
#         """Class method to increment the employee count."""
#         cls.employee_count += 1
#
#     @classmethod
#     def get_employee_count(cls):
#         """Class method to retrieve the current employee count."""
#         return cls.employee_count
# # Initial employee count
# print("Initial employee count:", Employee.get_employee_count())
#
# # Create new employees
# employee1 = Employee("John")
# print("Employee count after adding John:", Employee.get_employee_count())
#
# employee2 = Employee("Jane")
# print("Employee count after adding Jane:", Employee.get_employee_count())
#
# employee3 = Employee("Alice")
# print("Employee count after adding Alice:", Employee.get_employee_count())
#
# #7.Create a class Book with attributes title, author, and price.
# # Write a constructor that allows the user to either initialize all three attributes or
# # just the title and author (in which case the price should be set to a default value).
# # Display the details of the book using an instance method
#
# #Create Class Book
# class Book:
#     def __init__(self, title, author, price=0):
#         """Constructor to initialize the book's title, author, and optionally, price."""
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def display_details(self):
#         """Displays the details of the book."""
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: ${self.price}")
# # Create a book with all three attributes
# book1 = Book(title="1984", author="George Orwell", price=9.99)
# book1.display_details()
#
# # Create a book with only the title and author (price will default to 0)
# book2 = Book(title="To Kill a Mockingbird", author="Harper Lee")
# book2.display_details()

#8.Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius)
# that takes a temperature in Celsius and returns its Fahrenheit equivalent.
# Create an object of the class and use the method to convert various temperatures
#Creating Class TemperatureConverter

# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         """Converts Celsius to Fahrenheit."""
#         fahrenheit = (celsius * 9/5) + 32
#         return fahrenheit
# # Create an object of the TemperatureConverter class
# converter = TemperatureConverter()
#
# # Convert various temperatures
# temp1 = 0  # Celsius
# temp2 = 25  # Celsius
# temp3 = 100  # Celsius
#
# # Using the method to convert temperatures
# fahrenheit1 = converter.celsius_to_fahrenheit(temp1)
# fahrenheit2 = converter.celsius_to_fahrenheit(temp2)
# fahrenheit3 = converter.celsius_to_fahrenheit(temp3)
#
# # Display the results
# print(f"{temp1}°C is {fahrenheit1}°F")
# print(f"{temp2}°C is {fahrenheit2}°F")
# print(f"{temp3}°C is {fahrenheit3}°F")

#9.Create a class Time with attributes hours and minutes.
# Add a method add_time() that takes another Time object,
# adds its values to the current object, and returns a new Time object with the resulting sum.

#Creating Class Time
# class Time:
#     def __init__(self, hours=0, minutes=0):
#         """Constructor to initialize hours and minutes."""
#         self.hours = hours
#         self.minutes = minutes
#         self.normalize_time()  # Normalize the time to ensure proper formatting
#
#     def normalize_time(self):
#         """Normalize the time to ensure minutes are less than 60."""
#         if self.minutes >= 60:
#             extra_hours = self.minutes // 60
#             self.hours += extra_hours
#             self.minutes = self.minutes % 60
#
#     def add_time(self, other_time):
#         """Adds another Time object to the current Time object and returns a new Time object."""
#         total_hours = self.hours + other_time.hours
#         total_minutes = self.minutes + other_time.minutes
#         return Time(total_hours, total_minutes)
#
#     def __str__(self):
#         """Return a string representation of the Time object."""
#         return f"{self.hours} hours and {self.minutes} minutes"
#
# # Create two Time objects
# time1 = Time(1, 45)  # 1 hour and 45 minutes
# time2 = Time(2, 30)  # 2 hours and 30 minutes
#
# # Add the two time objects
# result_time = time1.add_time(time2)

# # Display the results
# print(f"Time 1: {time1}")  # Output: Time 1: 1 hours and 45 minutes
# print(f"Time 2: {time2}")  # Output: Time 2: 2 hours and 30 minutes
# print(f"Result Time: {result_time}")  # Output: Result Time: 4 hours and 15 minutes

#10.Create a class EmployeeSalary with class variables basic_salary and bonus_percentage.
# Write a class method set_bonus_percentage() to change the bonus percentage for all employees.
# Create an instance method calculate_total_salary() to calculate and return
# the total salary (basic + bonus) for a specific employee

#Creating Class EmployeeSalary
class EmployeeSalary:
    # Class variables
    basic_salary = 30000  # Default basic salary
    bonus_percentage = 10  # Default bonus percentage

    @classmethod
    def set_bonus_percentage(cls, new_percentage):
        """Set a new bonus percentage for all employees."""
        cls.bonus_percentage = new_percentage

    def calculate_total_salary(self):
        """Calculate and return the total salary for the employee."""
        bonus_amount = (EmployeeSalary.basic_salary * EmployeeSalary.bonus_percentage) / 100
        total_salary = EmployeeSalary.basic_salary + bonus_amount
        return total_salary

# Example Usage:
# Create an instance of EmployeeSalary
employee1 = EmployeeSalary()

# Calculate total salary with default bonus percentage
print(f"Total Salary (Default Bonus): {employee1.calculate_total_salary()}")  # Output: 33000.0

# Change the bonus percentage
EmployeeSalary.set_bonus_percentage(15)

# Calculate total salary after changing the bonus percentage
print(f"Total Salary (After Bonus Change): {employee1.calculate_total_salary()}")  # Output: 34500.0

# Create another instance to demonstrate the change in bonus for a new employee
employee2 = EmployeeSalary()
print(f"Total Salary for Employee 2: {employee2.calculate_total_salary()}")  # Output: 34500.0
