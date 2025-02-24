import re

# Question 1 :
# Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.

# a = int(input('enter the first number:'))
# b = int(input('enter the second number:'))
# operation = input('enter the operation:')
# match operation:
#     case "add":
#         print(a + b)
#     case "sub":
#         print(a - b)
#     case "mul":
#         print(a * b)
#     case "div":
#         print(a / b)
#     case _:
#         print("Invalid operation")

# =====================================================================================

# Question 2 :
# Write a program to filter out even numbers from a list and count how many are left.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 3, 5, 7, 9], Count = 5
# def even_number(numbers):
#     list = []
#     for i in numbers:
#         if i % 2 == 0:
#             list.append(i)
#     return list

# numbers = input('Enter the numbers separated by space:')
# numbers = list(map(int, numbers.split()))
# # print(numbers)0
# print('Even numbers:', even_number(numbers))
# print('Count:', len(even_number(numbers)))

# =====================================================================================

# Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
# password = "Pass1234"
# Expected Output: "Valid Password"

# password = input('Enter the password:')
# if len(password) >= 8 and any(i.isupper() for i in password) and any(i.isdigit() for i in password):
#     print('Valid Password')
# else:
#     print('Invalid Password')

# =====================================================================================

# Question 4: 
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}#
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)

# =====================================================================================

# Question 5: 
# takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu

# def longest_substring(s):
#     longest = current = s[0]

#     for i in range(1, len(s)):
#         if s[i] >= s[i - 1]:  
#             current += s[i]  
#         else:
#             if len(current) > len(longest):  
#                 longest = current  
#             current = s[i]  

#     if len(current) > len(longest):  
#         longest = current  

#     return longest


# s = input("Enter a string: ")
# print("Longest substring in alphabetical order is:", longest_substring(s))

# =====================================================================================

# Question 6:
# Write a program to check if a Email meets the following criteria:
# - Ensures the email follows a standard format (e.g., local@domain.com).
# - Does not check if the email actually exists or is deliverable.

# def is_valid_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return bool(re.match(pattern, email))

# email = input("Enter your email: ")
# if is_valid_email(email):
#     print("Valid email")
# else:
#     print("Invalid email")
