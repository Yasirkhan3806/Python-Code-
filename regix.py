# email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")


# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid"




import re



email = input("please type in ur email?").strip()

# if re.search(".+@.+",email):
#     print("valid")
# else:
#     print("invalid") # re is a package that is used for regular experression which actually uses some sign and symbols that is .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# now lets say we want to add .edu but dot in regix expression is a special character so we aadd a backslash which interpret in these statement as take this expression as literal string but at some point we might want to add n then \n is a special character so to avoid that we convert this into raw string which means that interpret this exression as how it is
# if re.search(r".+@.+\.com",email):
#     print("valid")
# else:
#     print("invalid")
# # there is a bug now that if we write a whole sentence like my email address is yk56@gmail.com it will be consider as valid so to avoid that we will use starting and ending signs that are
# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string


# if re.search(r"^.+@.+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")
 # # ^ and $ are used to match the start and end of the string respectively
 # # .+ matches one or more of any character except a newline
#  with this we haved solved the bugs upto some extent but there is still a bug that is we can add multiple @ sign like yj@@@@gmail.com and it will  be consider valide so what we will do is introduce new charcters that are 
# []    set of characters
# [^]   complementing the set

# if re.search(r"^[^@]+@[^@]+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")
# # [^@]+ matches one or more of any character except @
# We can still improve this regular expression further. It turns out there are certain requirements for what an email address can be! Currently, our validation expression is far too accomodating. We might only want to allow for characters normally used in a sentence. We can modify our code as follows:
# if re.search(r"^[a-zA-z0-9_]+@[a-zA-Z0-9_]+\.com$",email):
#     print("valid")
# else:
#     print("Invalid")
# Notice that [a-zA-Z0-9_] tells the validation that characters must be between a and z, between A and Z, between 0 and 9 and potentially include an _ symbol. Testing the input, you’ll find that many potential user mistakes can be indicated.
# Thankfully, common patterns have been built into regular expressions by hard-working programmers. In this case, you can modify your code as follows: 
# if re.search(r"^\w+@\w+\.edu$", email): # OR
# if re.search(r"^\w+@\w+\.(com|edu|pk|gov|org)",email):
#     print("Valid")
# else:
#     print("Invalid")

# A|B     either A or B
# (...)   a group
# (?:...) non-capturing version

# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character

# To illustrate how you might address issues around case sensitivity, where there is a difference between EDU and edu and the like, let’s rewind our code to the following:


# if re.search(r"^\w+@\w+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# Notice how we have removed the | statements provided previously.
# Recall that within the re.search function, there is a parameter for flags.
# Some built-in flag variables are:

# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

# Consider how you might use these in your code.
# Therefore, we can change our code as follows.

# import re

# email = input("What's your email? ").strip()

# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")

# Notice how we added a third parameter re.IGNORECASE. Running this program with MALAN@HARVARD.EDU, the input is now considered valid.

# after all of this lets have one final test that is use a valid email like yasirkhan@cs26.uop.edu which is pretty valid email address but it is being shown as invalid so how to tackle that well we had to specify a regix pattern for that but that will actually break our initial code that is this email yk56@gmail.com will now be considered as invalid so to solve this we will use another special character that is a ? which means 0 or 1 repititions means if its there its valide but if its not it doesnt matter so lets write it as follow 
# if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org|gov|org)$",email,re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")
# Interestingly enough, the edits we have done so far to our code do not fully encompass all the checking that could be done to ensure a valid email address. Indeed, here is the full expression that one would have to type to ensure that a valid email is inputted:
# ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$