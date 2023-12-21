moves = []
xCoordinate = 0
yCoordinate = 0
coordinatesList = []
fullCoordinate = str(xCoordinate) + ',' + str(yCoordinate)
coordinatesList[0] = fullCoordinate

with open(r"C:\Users\postl\Desktop\Personal\Projects\AdventOfCode2015\Day3\input.txt") as my_file:
    for character in my_file:
        moves = list(character)

for element in moves:
    count = 1
    if element == '>':
        xCoordinate =+ 1
    elif element == '<':
        xCoordinate = xCoordinate - 1
    elif element == '^':
        yCoordinate =+ 1
    else: yCoordinate = yCoordinate - 1
    fullCoordinate = str(xCoordinate) + ',' + str(yCoordinate)
    coordinatesList[count] = fullCoordinate
    count =+ 1
    print(coordinatesList)
