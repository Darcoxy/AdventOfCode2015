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

    sides = [length * width, width * height, height * length]
    smallestSide = min(sides)

    calculations = ['', '', '']
    calculations[0] = (2 * length * width)
    calculations[1] = (2 * width * height)
    calculations[2] = (2 * height * length)

    slack = smallestSide

    sum = calculations[0] + calculations[1] + calculations[2] + slack

    total = total + sum

print(total)