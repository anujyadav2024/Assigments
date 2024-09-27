# 1.Write a Python function to find the maximum of three numbers

# def find_maximum(a, b, c):
#   return max(a, b, c)
# num1 = 10
# num2 = 20
# num3 = 30
# print("The maximum number is:", find_maximum(num1, num2, num3))

# def find_maximum():
#   # Taking input from the user and converting it to float for flexibility
#   a = float(input("Enter the first number: "))
#   b = float(input("Enter the second number: "))
#   c = float(input("Enter the third number: "))
#
#   # Finding the maximum using the built-in max() function
#   maximum = max(a, b, c)
#
#   # Displaying the result
#   print("The maximum number is:", maximum)
#
# # Call the function
# find_maximum()


# 2.Write a Python function to multiply all the numbers in a list

# def multiply_all(numbers):
#     result = 1  # Start with 1 since it is the multiplicative identity
#     for number in numbers:
#         result *= number  # Multiply each number in the list
#     return result
#
# # Sample list
# sample_list = [8, 2, 3, -1, 7]
#
# # Call the function and print the result
# print("The result of multiplying all the numbers in the list is:", multiply_all(sample_list))

# 3.Write a Python program to reverse a string.
# def reverse_string(str):
#     # Using slicing to reverse the string(the slice statement [::-1] means start at the end of the string and end at position 0,
#     # move with the step -1, negative one, which means one step backwards.)
#     return str[::-1]
#
# # Sample string
# sample_string = "1234abcd"
#
# # Call the function and print the reversed string
# print("The reversed string is:", reverse_string(sample_string))


# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def fact(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#A ValueError in Python indicates that there is a problem with the program typed that you tried to assign the incentive to
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)  # Recursive call
# number = float(input("Enter the user input ="))
# print(f"The factorial of {number} is: {fact(number)}")

# 5.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample
# List:[1, 2, 3, 3, 3, 3, 4, 5]
# Unique List :[1, 2, 3, 4, 5]

# def distinct_elements(lst):
#     return list(set(lst)) # Convert the list to a set to remove duplicates, then back to a list
# #set(lst) removes duplicates from the list because sets do not allow duplicate elements.
# #set() method is used to convert any of the iterable to a sequence of iterable elements with distinct elements, commonly called Set.
# # Sample list
# sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
#
# # Call the function and print the result
# print("List with distinct elements:", distinct_elements(sample_list))

# sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
# print("List with distinct elements:", set(sample_list))

#6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# def is_prime(num):
#     if num <= 1:
#         return False  # Numbers less than or equal to 1 are not prime
#     for i in range(2, num):
#         if num % i == 0:
#             return False  # If divisible by any number, it is not prime
#     return True  # If no divisors were found, it's prime
#
# number = int(input("Enter the number :"))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# 7.Write a Python program to print the even numbers from a given list.Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# Sample list
# Sample_List=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Loop through the list and print even numbers
# for number in Sample_List:
#     if number % 2 ==0 :
#         print(number)

# # Sample list
# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Using list comprehension to find even numbers
# even_numbers = [number for number in sample_list if number % 2 == 0]
#
# # Print the result
# print(even_numbers)

# Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox',
# Expected Output :
# No. of Upper case characters : 3,
# No. of Lower case Characters : 12


# def count_upper_lower(string):
#     upper_count = 0
#     lower_count = 0
#
#     # Loop through each character in the string
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#
#     # Print the result
#     print(f"No. of Upper case characters : {upper_count}")
#     print(f"No. of Lower case Characters : {lower_count}")
#
#
# # Sample String
# sample_string = 'The quick Brow Fox'
#
# # Call the function with the sample string
# count_upper_lower(sample_string)


# def count_upper_lower(string):
#     upper_count = 0
#     lower_count = 0
#     for char in string:
#         if char.isupper():
#             upper_count+= 1
#         elif char.islower():
#             lower_count+= 1
#     print(f"No. of Upper case characters :{upper_count}")
#     print(f"No. of Lower case characters :{lower_count}")
# Sample_String ='The quick Brow Fox'
# count_upper_lower(Sample_String)

# 9.Write a Python function to sum all the numbers in a list.
# Sample List: (8, 2, 3, 0, 7),
# Expected Output: 20

# def sum_all_the_numbers(numbers):
#     return(sum(numbers))
# Sample_List=[8, 2, 3, 0, 7]
# result=sum_all_the_numbers(Sample_List)
# print(result)

# 10.Write a  Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run

# def is_palindrome(strings):
#     # Remove spaces and convert to lowercase
#     cleaned_string =strings.replace(" ", "").lower()
#     # Check if the cleaned string is the same when reversed
#     return cleaned_string == cleaned_string[::-1]
# # Sample Strings
# sample_string1 = "madam"
# sample_string2 = "nurses run"
#
# # Check if the strings are palindromes
# print(is_palindrome(sample_string1))  # True
# print(is_palindrome(sample_string2))  # True


















