moves = []
xCoordinate = 0
yCoordinate = 0
coordinatesList = []

def calculateCoordinates(list):
    results = []
    xCoordinate = 0
    yCoordinate = 0
    results.insert(0, '0,0')
    for element in list:
        if element == '>':
            xCoordinate = xCoordinate + 1
        elif element == '<':
            xCoordinate = xCoordinate - 1
        elif element == '^':
            yCoordinate = yCoordinate + 1
        elif element == '0,0':
            continue
        elif element == 'v': 
            yCoordinate = yCoordinate - 1
        fullCoordinate = str(xCoordinate) + ',' + str(yCoordinate)
        results.append(fullCoordinate)
    return results

with open(r"input.txt") as my_file:
    for element in my_file:
        moves = list(element)

santaCoordinates = moves[::2]
roboSantaCoordinates = moves[1::2]

santaCoordinates.insert(0, '0,0')
roboSantaCoordinates.insert(0, '0,0')

uniqueSantaCoordinates = set((calculateCoordinates(santaCoordinates)))
uniqueRoboSantaCoordinates = set((calculateCoordinates(roboSantaCoordinates)))

uniqueFromBoth = set(uniqueSantaCoordinates.union(uniqueRoboSantaCoordinates))

print(len(uniqueFromBoth))