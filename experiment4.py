# try:
#     length = float(input("enter length: "))
#     width = float(input("enter width: "))
#     if length == width:
#         exit("that is a square")
#     area = length * width
#     print(area)
# except ValueError:
#     print("write number")


try:
    total_value = int(input("enter total value: "))
    value = int(input("enter value: "))

    d = total_value/value
    if d == 0:
        print("0")
except ZeroDivisionError:
    print("your total value cannot be zero. ")
