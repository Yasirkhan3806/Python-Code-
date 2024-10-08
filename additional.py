# here we will discuss some additional concepts like:
# 1. SETS , a datatype that eliminates duplicates and save only distinct values
# arr = [2,110,4,6,8,113,9,112,110,3,5,3]

# set1 = set()
# for i in arr:
#     set1.add(i)

# print(sorted(set1))

# 2.GLOBAL variables
# to make a variable global we have to use keyword global like 
# global balance  if we didnt define it global this program will show unboundLocalError

# def main():
#     global balance
#     balance = 1000
#     print(f"initial balance: {balance}")
#     deposit(500)
#     withdraw(200)
#     print(f"final balance: {balance}")

# def deposit(amount):
#     global balance
#     balance += amount
    
# def withdraw(amount):
#     global balance
#     if balance >= amount:
#         balance -= amount
#     else:
#         print("Insufficient funds")

# if __name__ == "__main__":
#     main()

# 3.Constants
# in python the constants are represented by capital letter which is a convention and not enforced by the language itself so a variable like MEOW = 3 is by convention a constant and anyone who reads this code will not touch it by any means

#     n other programming languages, one expresses explicitly what variable type you want to use.
#     As we saw earlier in the course, Python does not require the explicit declaration of types.
#     Nevertheless, it’s good practice need to ensure all of your variables are of the right type.
#     mypy is a program that can help you test to make sure all your variables are of the right type.
#     You can install mypy by executing in your terminal window: pip install mypy.

# In the text editor window, code as follows:

#   def meow(n):
#       for _ in range(n):
#           print("meow")


#   number = input("Number: ")
#   meow(number)

# You may already see that number = input("Number: )" returns a string, not an int. But meow will likely want an int!

#     A type hint can be added to give Python a hint of what type of variable meow should expect. In the text editor window, code as follows:

#     def meow(n: int):
#         for _ in range(n):
#             print("meow")


#     number = input("Number: ")
#     meow(number)

#     Notice, though, that our program still throws an error.
#     After installing mypy, execute mypy meows.py in the terminal window. mypy will provide some guidance about how to fix this error.

#     You can annotate all your variables. In the text editor window, code as follows:

#     def meow(n: int):
#         for _ in range(n):
#             print("meow")


#     number: int = input("Number: ")
#     meow(number)

#     Notice how number is now provided a type hint.
#     Again, executing mypy meows.py in the terminal window provides much more specific feedback to you, the programmer.

#     We can fix our final error by coding as follows:

#     def meow(n: int):
#         for _ in range(n):
#             print("meow")


#     number: int = int(input("Number: "))
#     meow(number)

#     Notice how running mypy how produces no errors because cast our input as an integer.

#     Let’s introduce a new error by assuming that meow will return to us a string, or str. In the text editor window, code as follows:

#     def meow(n: int):
#         for _ in range(n):
#             print("meow")


#     number: int = int(input("Number: "))
#     meows: str = meow(number)
#     print(meows)

#     Notice how the meow function has only a side effect. Because we only attempt to print “meow”, not return a value, an error is thrown when we try to store the return value of meow in meows.

#     We can further use type hints to check for errors, this time annotating the return values of functions. In the text editor window, code as follows:

#     def meow(n: int) -> None:
#         for _ in range(n):
#             print("meow")


#     number: int = int(input("Number: "))
#     meows: str = meow(number)
#     print(meows)

#     Notice how the notation -> None tells mypy that there is no return value.

#     We can modify our code to return a string if we wish:

#     def meow(n: int) -> str:
#         return "meow\n" * n


#     number: int = int(input("Number: "))
#     meows: str = meow(number)
#     print(meows, end="")

#     Notice how we store in meows multiple strs. Running mypy produces no errors.
#     You can learn more in Python’s documentation of Type Hints.
#     You can learn more about mypy through the program’s own documentation.

# 4. DocString : there is a convention to how a program should be documented so thatw when we use a third-party library we can simply convert those conmments to a formal pdf 

#     Here is an example of a simple function with a docstring:
# def meow(n):
#     """Prints meow n times."""
#     # Or 
#     """
#     Print meow n times.
#     :param n:
#     :type n: int
#     :raise ValueError:
#     :return none
#     """
#     for _ in range(n):
#         print("meow")


