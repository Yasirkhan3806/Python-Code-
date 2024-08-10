# Dict comprehension is a technique that allow us to perform opertion of a dict to return a dict based on the logic 

students = ["harry","ron","horman"]

# suppose we want to create a dictionary where each name is assigned a house or we want to see where is the student from

# houses = []
# for student in students:
#     houses.append({'name': student, 'house': "griffindor"}) 
# print(houses)
# OR
# houses = [{'name':student , 'house': "griffindor"} for student in students]
# print(houses)
# OR using DictComp

# houses = {student: "griffindor" for student in students} syntax is {first_key:SecondKey Logic__}
# print(houses)

