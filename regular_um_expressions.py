import sys
import re


def main():
    # taking_input()
    print(f"Number of times um is used is : {taking_input()}")



def taking_input():
    input_taken = input("Type any statement: ")
    stri = re.findall(r"\b(um)\b",input_taken,re.IGNORECASE)
    return len(stri)


if __name__ == "__main__":
    main()