PK     0z;XώΝ/w   w   	   bonus8.pydef calculate_time(h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)PK     ;X’"t  t     bous1.pyfrom bagge import convert
from billo import parse

feet_inches = input("enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} result")
if result < 1:
    print("kid is too small")
else:
    print("kid can use the slide. ")
PK      0z;XώΝ/w   w   	           Ά    bonus8.pyPK      ;X’"t  t             Ά   bous1.pyPK      m   8    