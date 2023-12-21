dimensions = []
total = 0

with open(r"C:\Users\postl\Desktop\Personal\Projects\AdventOfCode2015\Day2\input.txt") as my_file:
    for line in my_file:
        dimensions.append(line)

for element in dimensions:
    converted = list(map(int, element.split('x')))
    length = converted[0]
    width = converted[1]
    height = converted[2]

    ribbonSize = 2 * min(length + width, width + height, height + length)
    bowSize = length * width * height

    total = total + ribbonSize + bowSize

print(total)