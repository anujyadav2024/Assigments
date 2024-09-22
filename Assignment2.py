## Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus
#Display the results for each operation.
Input_First_number=int(input("Enter the First number :"))
Input_Second_number=int(input("Enter the Second number :"))
x=Input_First_number
y=Input_Second_number
Addition=x+y
Subtraction=x-y
Multiplication=x*y
Division=x/y
Modulus=x%y

print("Addition of Two Input :",Addition)
print("Subtraction of Two Input :",Subtraction)
print("Multiplication of Two Input :",Multiplication)
print("Division of Two Input :",Division)
print("Modulus of Two Input :",Modulus)

## Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.
a=int(input("Enter the First number: "))
b=int(input("Enter the Second number: "))
if (a%b==0):
    print("given number is even")
else:
    print("given number is odd")

# Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero
a=int(input("Enter the First number: "))
if (a==0):
    print("input is zero")
elif(a<0):
    print("input is negative")
else:
    print("input is positive")

# Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
#
# 90 and above: A
# 80 - 89: B
# 70 - 79: C
# 60 - 69: D
# Below 60: F
grade_student=float(input("Please enter student marks:"))
if grade_student >= 90:
        print("Student grade is A")
elif grade_student >=80:
        print("Student grade is B")
elif grade_student >= 70:
        print("Student grade is C")
elif grade_student >= 60:
        print("Student grade is D")
else:
        print("Student grade is F")

# Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.

# Creating and writing to sample.txt
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.")

# Reading and displaying the content
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)


# Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.

# Python program to print numbers from 1 to 10 using a for loop
for number in range(1, 11):
    print(number)

#8 Python program to display the multiplication table of a number entered by the user

# Get the number from the user
number = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(number, "X", i ,"=" ,number * i)

# Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.
file=open("data.txt","r")
count=0
for words in file:
    words = words.split(" ")
    count+= len(words)
file.close()
print("the number of words in the file :",count)
