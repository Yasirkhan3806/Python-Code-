# here we will discuss some additional concepts like:
# 1. SETS , a datatype that eliminates duplicates and save only distinct values
# arr = [2,110,4,6,8,113,9,112,110,3,5,3]

# set1 = set()
# for i in arr:
#     set1.add(i)

# print(sorted(set1))

# 2.GLOBAL variables
# to make a variable global we have to use keyword global like 
global balance 

def main():
    global balance
    balance = 1000
    print(f"initial balance: {balance}")
    deposit(500)
    withdraw(200)
    print(f"final balance: {balance}")

def deposit(amount):
    global balance
    balance += amount
    
def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
    else:
        print("Insufficient funds")

if __name__ == "__main__":
    main()


