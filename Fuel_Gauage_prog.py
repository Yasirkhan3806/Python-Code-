def main():
    actual_value = int(calculating_fuel_gauge())
    if(actual_value <=100):
        print(f'{actual_value}%')
    else:
        calculating_fuel_gauge()
def taking_value(prompt):

            return input(prompt)



def calculating_fuel_gauge():
    while True:
        try:
            taken_value = taking_value("Enter the current value of your fuel meter? ")
            x, y = taken_value.split("/")
            if y != "0" :
                return (int(x) / int(y)) * 100
        except ValueError:
            pass




if __name__ == "__main__":
    main()
