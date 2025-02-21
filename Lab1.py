import math
# Question 1
# Remove the first occurance of 20

# a = [10, 20, 30, 20, 40, 50]
# a.remove(20)
# print(a)

# ===========================================================

# Question 2
# Remove element at index 1 and return its value in val

# a = [ 20, 30, 20, 40, 50]
# val = a.pop(0)
# print(val)

# ===========================================================

# Question 3
# Removes elements from index 1 to index 3 (which are 20, 30, 40)
# a = [10, 20, 30, 40, 50, 60, 70]
############# Directlry modify the array (Solution 1) #############
# del a[0:3]
# print(a)
############# Creating filtered list instead (Solution 2) ############# 
# x = a[0:3]
# filtered = []
# for n in a:
#     if n not in x:
#         filtered.append(n)
# print(filtered)

# ===========================================================

# Question 4
# Remove all elements
# a = [10, 20, 30, 40, 50, 60, 70]
# a.clear() #first method
# del a[:] #second method
# print(a)

# ===========================================================

# Write a program that prints the number of times the substring 'iti' occurs in a string
s = 'iti'
# num = 0
# for c in s:
#     if c == 'i':
#         num+=1
# print(f"count 'i' in iti is: {num}") # solution 1

# print(f"count 'i' in iti is: {s.count('i')}") #solution 2

# ===========================================================

# application to take a number in binary form from the user, and print it as a decimal
# while True:
#     try:
#         x = input('enter a number: ')
#         print(float(x))
#         break
#     except ValueError:
#         print('enter a valid number')

# ===========================================================

# write a code take a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"

# def check(num):
#     if num % 5  == 0 and num % 3 == 0:
#         return('FizzBuzz')
#     elif num % 3 == 0:
#         return('fizz')
#     elif num % 5 == 0:
#         return('buzz')
#     else:
#         return('wrong number')

# x = int(input('enter a number: '))
# print(check(x))

# ===========================================================

# Ask the user to enter the radius of a circle print its calculated area and circumference

# radius = float(input('enter radius: '))

# print(f'Circumference: {radius * math.pi * 2}')
# print(f'Area: {math.pi * radius **2}')

# ===========================================================

# Ask the user for his name then confirm that he has entered his name (not an empty string/integers).then proceed to ask him for his email and print all this data

name = input('enter your name: ')
email = input('enter your email: ')

while True:
    if name == '' or name.isdigit():
        name = input("Please enter a valid name: ")
    else:
        break

print('Name: ', name)
print('Email: ', email)