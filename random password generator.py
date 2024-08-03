import random

alphabets = ["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number = [1,2,3,4,5,6,7,8,9,0]
i = 0
j = 0
password = ""
numbers = ''
while i <= 8:
    password += random.choice(alphabets)
    i +=1

while j < 3:
    numbers += str(random.choice(number))
    j +=1

print(password + numbers)
