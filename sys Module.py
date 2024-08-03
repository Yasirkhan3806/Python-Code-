#  #So far, we have been providing all values within the program that we have created. What if we wanted to be able to take input from the command-line? For example, rather than typing python average.py in the terminal, what if we wanted to be able to type python average.py 100 90 and be able to get the average between 100 and 90?
# sys is a module that allows us to take arguments at the command line.
#
# argv is a function within the sys module that allows us to learn about what the user typed in at the command line. Notice how you will see sys.argv utilized in the code below. In the terminal window, type code name.py. In the text editor, code as follows:
#
# import sys
#
# print("hello, my name is", sys.argv[1])
#
# Notice that the program is going to look at what the user typed in the command line. Currently, if you type python name.py David into the terminal window, you will see hello, my name is David. Notice that sys.argv[1] is where David is being stored. Why is that? Well, in prior lessons, you might remember that lists start at the 0th element. What do you think is held currently in sys.argv[0]? If you guessed name.py, you would be correct!
#
# There is a small problem with our program as it stands. What if the user does not type in the name at the command line? Try it yourself. Type python name.py into the terminal window. An error list index out of range will be presented by the compiler. The reason for this is that there is nothing at sys.argv[1] because nothing was typed! Here’s how we can protect our program from this type of error:
#
# import sys
#
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
#
# Notice that the user will now be prompted with a useful hint about how to make the program work if they forget to type in a name. However, could we be more defensive to ensure the user inputs the right values?
#
# Our program can be improved as follows:

# import sys
#
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])
#
# Notice how if you test your code, you will see how these exceptions are handled, providing the user with more refined advice. Even if the user types in too many or too few arguments, the user is provided clear instructions about how to fix the issue.
#
# Right now, our code is logically correct. However, there is something very nice about keeping our error checking separate from the remainder of our code. How could we separate out our error handling? Modify your code as follows:
#
# import sys
#
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
#
# print("hello, my name is", sys.argv[1])
#
# Notice how we are using a built-in function of sys called exit that allows us to exit the program if an error was introduced by the user. We can rest assured now that the program will never execute the final line of code and trigger an error. Therefore, sys.argv provides a way by which users can introduce information from the command line. sys.exit provides a means by which the program can exit if an error arises.
# You can learn more in Python’s documentation of sys.

