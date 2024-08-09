class Students:
    def __init__(self, name, house):#its like a parameterized constructor and self is like this pointer which is referring to the current object which is instantiated by this class
        self.name = name
        self.house = house

    def __str__(self):#this function is called when the object as a whole being applied operation on and its like represent the class
        return f"A student {self.name} from {self.house}"
    
    @property # used to say that the following method is a getter function
    def get_house(self):
        return self.house
    
    @get_house.setter
    def set_house(self, house):
        self.house = house
        # the point that should be noted here is that whenever value of house is set to a value this function will be automatically called to set the value even in the __init__ method so if we want to perform an opertation before setting the value we will need a setter function
        # setter will be called anytime .house is called anywhere in the program that is related to this class even in the other functions like the following example in main function

def main():
    student = get_the_stu_data()
    # student.house = "random house" setter will be called for this and the advantage of this is that whatever condition you have applied on getting the house data will be applied if you change the value from anywhere
    print(student)


def get_the_stu_data():
    
    name = input("name: ")
    house = input("house: ")
    return Students(name, house)


if __name__ == "__main__":
    main()