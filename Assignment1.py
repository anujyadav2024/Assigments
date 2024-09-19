# 1.Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.

# Define variables as Integer, Float and String
int_var = 1       # Integer
float_var = 1.0   # Float
string_var = '1'  # String
print("int_var :", (int_var,type(int_var)),"float_var :",
      (float_var,type(float_var)),"string_var :", (string_var,type(string_var))) #o/p

# 2.Define a variable as Integer(2) ,Float(2.0) and String(‘2’) and print and return the value and type of variable.

# # Define variables as Integer, Float and String
int_var = 2       # Integer
float_var = 2.0   # Float
string_var = '2'  # String
print("int_var :", (int_var,type(int_var)),"float_var :",
      (float_var,type(float_var)),"string_var :", (string_var,type(string_var))) #o/p

# 3.Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c.

a=b=c=10
print(a,b,c)

# 4. Assign two variables a and b as integer and print the sum of a+b.


# Assign two variables
a = 10
b = 20

# Print the sum of a and b
print("The sum of a and b is:", a + b)

# 5.Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?

# # Create a list of five fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the list of fruits
print(fruits)

#6. How do you access the second and fourth elements from the list.

second_fruits=fruits[1]
fourth_fruits=fruits[3]
print(second_fruits)
print(fourth_fruits)

# 7.Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.

list_numbers = [10, 20, 30, 40, 50]
print(list_numbers)
list_numbers[2]=35
print(list_numbers)

#Tupple#

# 1.How do you create a tuple with the following elements: "red", "green", "blue"?

Tuple_elements=("red", "green", "blue")
print(Tuple_elements)

# Elements in a Tuple:How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?

tuple_colors = ("red", "green", "blue", "yellow")

first_element = tuple_colors [0]  # This will be Red
last_element = tuple_colors [-1]   # This will be yellow

print("First element:", first_element)
print("Last element:", last_element)

# Immutable Nature of Tuples:What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?

tuple_colors = ("red", "green", "blue")
print(tuple_colors)
#tuple_colors[1] = "yellow"
#print(tuple_colors[1])#TypeError: 'tuple' object does not support item assignment

# Tuple Unpacking:Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.

coordinates = (10, 20, 30)

# Unpacking the tuple into three variables
x, y, z = coordinates

print("x:", x)
print("y:", y)
print("z:", z)

# Check Element in Tuple:Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").

element=("red", "green", "blue")
# Check if "blue" is in the tuple
print(element)
if "blue" in element:
    print("Yes, 'blue' is present in the element")
else:
   print("No, 'blue' is not present in the element")

#Tuple Length:Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").

tuple_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(tuple_days)
# Find the length of the tuple
length_of_tuple = len(tuple_days)
print("The length of the tuple is:", length_of_tuple)

# Dictionary

# Create a Dictionary:Create a dictionary where the keys are student names and the values are their grades. For example:

#{"Alice": 85,"Bob": 90,"Charlie": 78}

# Create a dictionary with student names and grades
student_names_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Print the dictionary
print(student_names_grades)

# Access Dictionary Values:How do you access Bob's grade from the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}?

student_names_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
print(student_names_grades)
# Access Bob's grade
bobs_grade = student_names_grades["Bob"]

# Print Bob's grade
print("bobs_grade is", bobs_grade)

# Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary

student_name_grades = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78
}
print(student_name_grades)

#Add new student "David"
student_name_grades["David"] = 92
print(student_name_grades)#Print total Student

# Remove "Charlie" from the dictionary
del student_name_grades["Charlie"]

# Print the updated dictionary
print(student_name_grades)

#Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
student_name_grades = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78
}
print(student_name_grades)
# Update Bob's grade to 95
student_name_grades ["Bob"] = 95

# Print the updated dictionary
print(student_name_grades )

# # Check if "Alice" is a key in the dictionary
if "Alice" in student_name_grades:
    print("Alice is a key in the dictionary.")
else:
    print("Alice is not a key in the dictionary.")

# Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

student_name_grades = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78
}
print(student_name_grades)
# Find the number of key-value pairs
num_pairs = len(student_name_grades)

# Print the result
print("The number of key-value pairs in the dictionary is:", num_pairs)