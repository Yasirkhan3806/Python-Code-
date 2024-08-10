import argparse

parse = argparse.ArgumentParser(description="this program meows like a cat")
"""we are calling ArgsParser method of argparse which will allow us to add an arguments in latter lines"""
parse.add_argument("-n", default=1, type=int, help="Number of times a cat should meow")
arg = parse.parse_args()

for i in range(arg.n):
    print("meow!")