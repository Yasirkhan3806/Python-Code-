# well now lets suppose we recieved a data and instead of validating it we want to clean it up so lets start by getting name from a user 

username = input("What is ur name? ")
# now lets dicuss some scenario 
# 1. adding comma to the name or writing it backward
# print(username) # by directly printing it it would be completely wrong so instead we pass a condition
# if "," in username:
#     lastname , firstname = username.split(", ")
#     print(f"Hello, {firstname} {lastname}") 
    # now this might fix my condition that is it will remove the comma and write my name in a straight forward manner but what if i forget to add space after the comma or write my name as yasir khan,yousafzai this will completely break my code 
    # so again we will use re package so lets import it first
import re

# now we have to create suuch a pattern so that there is something before the comma and after a comma so lets use a re.search function  lets go
if matches := re.search(r"^(.+), *(.+)$",username):
# now there is a concept in regix that anything that is in paranthesis it will be returned and we can access it by  calling the grouped function and anything in the paranthesis will be returned to it and we can avoid that us (?:) anything written in this syntax will only be checked if available and will not be returned
# if matches: # to tighten this code a little bit we are going to use a new operator called walrus operator that is going to not only assign the values to matches but also check it at the same line
    # lastname, firstname = matches.groups() OR 
    # lastname = matches.group(1)
    # firstname = matches.group(2) or
    name = matches.group(2) + " " + matches.group(1) 
    print(f"Hello, {name}")
else:
    print(username)
# there is still a bug that if we try to add too many white spaces or no spaces before the first name so to counter that we will use an asterik sign that will take no words or any word after comma and will only return whats in the block 