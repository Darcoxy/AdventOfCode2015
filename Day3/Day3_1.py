moves = []
xCoordinate = 0
yCoordinate = 0
coordinatesList = []
fullCoordinate = coordinatesList.append(str(xCoordinate) + ',' + str(yCoordinate))

with open(r"C:\Users\JJ\Desktop\Projects\AdventOfCode2015\Day3\input.txt") as my_file:
    for character in my_file:
        moves = list(character)

for element in moves:
    if element == '>':
        xCoordinate = xCoordinate + 1
    elif element == '<':
        xCoordinate = xCoordinate - 1
    elif element == '^':
        yCoordinate = yCoordinate + 1
    else: yCoordinate = yCoordinate - 1
    fullCoordinate = str(xCoordinate) + ',' + str(yCoordinate)
    coordinatesList.append(fullCoordinate)
print(len(set(coordinatesList)))