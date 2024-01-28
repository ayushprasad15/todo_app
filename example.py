password = input("enter the password: ")
# result = []
result = {}

if len(password) >= 5:
    result["length"] = True
else:
    result["length"] = False

print(result)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit
print(result)

upper_case = False
for i in password:
    if i.isupper():
        upper_case = True
result["upper case"] = upper_case
print(result)

if all(result.values()):
    print("strong password")
else:
    print("weak password")
