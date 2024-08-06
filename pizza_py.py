import csv
from tabulate import tabulate

pizzas = []
table = []

with open("regular.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
      pizzas.append(row)
    print(pizzas)
    for line in pizzas:
   
         table.append([line["Regular Pizza"], line["Small"], line["Large"]] )
    print(tabulate(table, headers=["Regular Pizza", "Small", "Large"] ,tablefmt="grid"))
    # hehe boy i am the Best muehehee
    