# lets discover the function that is filter which based on our kogic decide which element of a list should be included in other list/Dict or not let see

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# we want to get only those students whose house is Gryffindor

filtered_students = list(filter(lambda student: student["house"] == "Gryffindor", students))

for student in sorted(filtered_students, key=lambda s:s['name']):
    print(student['name'])


#filter function will return a new list which contains only those elements for which the given function returns true