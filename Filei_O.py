# )
#
# File = open("names.txt", "a")
# File.write(f'{name}\n')
# File.close()
# OR we can use this syntax
# with open("names.txt", "a") as file:
#     file.write(f'{name}\n')
#     Now to access this file we have some syntax for that

# with open("names.txt","r") as file:
#      lines = file.readlines()
# for line in lines:
#     print('hello, ',line.rstrip())The rstrip function in Python is used to remove trailing characters from the end of a string
# Second method
#
#     for line in file:
#         print("hello, ", line.rstrip())

# we want to organize the names so we can do it like this
# names = []
# with open("names.txt","r") as file:
#     for line in file:
#         names.append(line.rstrip())
#     for name in sorted(names):
#         print("hello, ",name)
    # Or
    # for line in sorted(file):
    #     print(f'hello {line.rstrip()}')

#
# now lets say we want to store multiple values in a file so instead of text file we are gonna use csv file which stands for comma separated values so lets creat a csv file
students = []
with open("names") as file:
    # for line in sorted(file, reverse=True): this is getting sorted by just the fact that english is being read from right to left so now we need a mechanism to sort by either name or house or any other information stored
    #     row = line.rstrip().split(",")
    #     print(f'{row[0]} lives in {row[1]}')
    # lets start by storing the information inside an list that contain dictonary having keys names and house
    for line in file:
        name , house = line.rstrip().split(",")
        student = {"names":name , "house": house}
        students.append(student)
    # here comes a concept of key that tells a sort function to access which key information inside a dict inside a list
# def get_name(student):
#     return student["names"]
# def get_house(student):
#     return student["house"] Or we can use lambda function : a lambda function is an anonymous function that has no name but since its used only one time thats why we create a lambda function

# for data in sorted(students,key=get_name, reverse=True):  sort by name
#     print(f'{data["names"]} lives in the {data["house"]}')

# for data in sorted(students,key=get_house): sorted by house
#     print(f'{data["names"]} lives in the {data["house"]}')
#
# for data in sorted(students,key=lambda student : student["names"]): lambda function syntax is lambda parameter : return value
#  print(f'{data["names"]} lives in the {data["house"]}')