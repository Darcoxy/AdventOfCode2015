floor = 0
floorUp = 0
floorDown = 0

userInput = input("Enter: ")

for element in userInput:
    if element == '(':
        floorUp = floorUp + 1
    else: floorDown = floorDown + 1

print('Floor up number: ' + str(floorUp))
print('Floor down number: ' + str(floorDown))

anwser = floor + (floorUp - floorDown)

print('Awnser is: ' + str(anwser))