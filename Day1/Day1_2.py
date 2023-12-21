floor = 0
floor = 0
count = 0
floorUp = 0
floorDown = 0

userInput = input("Enter: ")

for element in userInput:
    if element == '(':
        count = count + 1
        floor = floor + 1
    else: 
        count = count + 1
        floor = floor - 1
    if floor == -1:
        break
print(str(count))