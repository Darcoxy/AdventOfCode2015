vowels = 'aeiou'
badStrings = ['ab', 'cd', 'pq', 'xy']

file = open(r"C:\Users\postl\Desktop\Personal\Projects\AdventOfCode2015\Day5\input.txt")
totalLine = 0
niceCount = 0
naughtyCount = 0

lines = file.readlines()
count = 0
for line in lines:
    count += 1
    line.strip()
    print(line)