# name = input("whats your name? ")
# color = input("whats your fav color? ")
# print(name + " Likes " + color)

# birth_year = input("whats your age? ")
# age = 2024 - int(birth_year)
# fuck_you = "what the hell does that supposed to mean? "
# print(age)
# print(type(birth_year))

# weight = input("whats your weight? ")
# weight_in_kg = float(weight) * 0.453592
# print(weight_in_kg)

# String Techniques:
# course = "Python for beginners"
# print(course[0:3]) #this technique will return the string character inlcuding the first index defined but the excluded the character on second index and but default their value are [0:last character of the string]

# Formatted Strings
# First_name = 'Yasir'
# Last_Name = 'Khan'
#Now there are two ways to print this
# message = First_name + ' [ ' + Last_Name + ' ] ' + 'is the best coder in the world'
# print(message)
# #Or we use formatted string that starts with f with is more simple and understandable
# msg = f'{First_name} [{Last_Name}] is the best coder in the world'
# print(msg)

# STRING METHOD ,RUN THE FOLLOWING PROGRAM TO UNDERSTAND
# Remeber all of the mention methods are case sensitive
# message = "How are you"
# print(len(message))
# print(message.upper())
# print(message.lower())
# print(message.find('How'))
# print(message.replace('are', 'my'))
# # in operator is special boolean operator that finds a word in a string and return boolean value lets see(it is also case sensitive
# print('you' in message)

# Some tricky new arth operators
# # float division
# print(10 / 3)
# #Integar division
# print(10 // 3)
# #Power operator
# print(10 ** 3)
# import math
# # Some Math Functions
# number = 2.9
# print(round(2.9))
# [print(abs(-2.9))] #absolute function of calculas always return a postiive value
# print(abs(2.9))
# # Importing math module (to see more of maths fucnction type python 3 math module in google)
# print(math.ceil(2.9))
# print(math.floor(2.9))

# If else statement in Python
# price_house = 1000000
# credit = int(input('Whats your credit score'))
#
# if credit > 500000 :
#     down_payment = 0.1 * price_house #Remember to look at the indentation as there are no brackets in python and an indentation means its within the statement body
# else:
#     down_payment = 0.2 * price_house
#
# print(down_payment)

#WEIGHT CALCULATOR FROM KG TO POUNDS AND POUNDS TO KG
# weight = float(input('Please input your age? '))
# unit = (input('Select the unit? ')).lower()
# if unit == 'kg':
#     weight_kg = weight * 2.20462
#     print(weight_kg)
# else:
#     weight_pounds = weight / 2.20462
#     print(weight_pounds)

# Guessing the number game using while loop
# lucky_number = 8
# i = 0
# j = 3
# while i < 3 :
#     guessed_number = int(input('Guess the lucky Number: '))
#     if lucky_number == guessed_number:
#         print('You have won')
#         break
#     else:
#         j -= 1
#         print(f'Wrong , Try Again, you have {j} more chances')
#         i +=1
#
#
# else:
#  print('All the tries are over')

# Car Game Without graphics
#
# while True:
#     command = input('Press "P" to start the game or "T" to terminate from the game: ').lower()
#     if command == 'p':
#         print('Press "S" to start the car.')
#         print('Press "C" to stop the car.')
#         print('Press "E" to exit the current game.')
#
#         car_started = False  # State variable to track if the car is started or stopped
#
#         while True:
#             start_command = input().lower()
#             if start_command == 's':
#                 if car_started:
#                     print('Car is already started!')
#                 else:
#                     print('Car is started.')
#                     car_started = True
#             elif start_command == 'c':
#                 if not car_started:
#                     print('Car is already stopped!')
#                 else:
#                     print('Car is stopped.')
#                     car_started = False
#             elif start_command == 'e':
#                 print('You have exited the game.')
#                 break
#             else:
#                 print("I don't understand that command.")
#     elif command == 't':
#         print('Hope you enjoyed the game.')
#         break
#     else:
#         print("Sir, please press 'P'.")

# For Loops
# for item in ['john','Yasir','shahab']:
#     print(item[0:1])
# # Range function in Python returns numbers in its range and we can also specify  the range and also in which manner should the counting be done
# #general syntax Range(starting-point,Ending-point,incrementation-count)
# for item in range(5,25,4):
#     print(item)

# for items in range(5):
#     if items == 0 or items == 2:
#         print("*" * 5)
#     else:
#         print('*' * 2)

# number = [5,2,5,2,2]
# for item in range(5):
#     count = ''
#     for item in range(number[item]):
#         count += "x"
#     print(count)
# #Prints L
# number_L = [1, 1, 1, 1, 5]
# for item in range(5):
#     count = ''
#     for item in range(number_L[item]):
#         count += "x"
#     print(count)

# Finding greatest number in list
# numbers = [5, 8, 9, 4, 5]
# greatest_number = numbers[0]
#
# for num in numbers:
#     if num > greatest_number:
#         greatest_number = num
#
# print(greatest_number)

# 2D Lists
# matrix = [
#     [2,3,4],
#     [4,5,6],
#     [9,0,8]
# ]

# List Methods
#Program to remove duplicate number from the list
# First method generally used
# lis = [2,4,5,8,9,8,0,8,8,9,4,5,7]
# unique_items = []
# for items in lis:
#     if items not in unique_items:
#         unique_items.append(items)
#
#
# print(unique_items)
# Second Method by me
# for items in lis:
#     occurance = lis.count(items)
#     if occurance > 1:
#         lis.pop(lis.index(items))
#
#
# print(lis)

# Unpacking Concept in Python
# coordinate = (1,2,3) # a list with circular brackets is called tuples which is just const list
# x= coordinate[0]
# y= coordinate[1]
# z= coordinate[2]
# x,y,z = coordinate #above three lines and this have the same meaning
# print(x , y , z)

# Dictionaries in python
# phone_number = input("Phone: ")  # Take input as a string to preserve each digit
# phone = {
#     '0': "zero",
#     '1': "one",
#     '2': "two",
#     '3': "three",
#     '4': "four",
#     '5': "five",
#     '6': "six",
#     '7': "seven",
#     '8': "eight",
#     '9': "nine"
# }
#
# alphabet = ''
# for digit in phone_number:
#     alphabet += phone[digit] + ' '
#
# print(alphabet.strip())

#Creating emoji converter
input_taken  = input(">")
words = input_taken.split(" ")
emojis = {
    ":)" : "😁",
    ":(" : "😢",
    ";)" : "😉",
}
output = ''
for each in words:
  output +=  emojis.get(each,each) + " "

print(output)

#exception in python
# while True:
#     try:
#         x = int(input("What is the value of x? "))
#
#     except ValueError:
#         print("x is not an integar")
#     else:
#         break
# print(f'the value of x is {x}')

# Functions in py
# def main():
#     x = get_int()
#     print(x)
#
#
# def get_int():
#     while True:
#        try:
#            return int(input("whats the value of x? "))
#        # except ValueError:
#        #     print("x is not an integar") Or
#        except ValueError:
#            pass
#
#
#
#
# main()

