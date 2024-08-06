import csv

name = input("whats your name?")
house = input("where do you live?")

# with open("writing_names.csv", "a",newline='') as file:
    # writer = csv.writer(file)
    # writer.writerow([name, house])
with open("writing_names.csv", "a",newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","house"])
    writer.writerow({'name': name,'house': house})    