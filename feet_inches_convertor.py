from inches_mind import convert
from billo import parse

feet_inches = input("enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} result")
if result < 1:
    print("kid is too small")
else:
    print("kid can use the slide. ")
