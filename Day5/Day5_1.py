file = open(r"C:\Users\postl\Desktop\Personal\Projects\AdventOfCode2015\Day5\input.txt")
vowels = ['a', 'e', 'i', 'o', 'u']
badStrings = ['ab', 'cd', 'pq', 'xy']
niceCount = 0
naughtyCount = 0

def getListOfLines(file):
    with open(r"C:\Users\postl\Desktop\Personal\Projects\AdventOfCode2015\Day5\input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

def checkForVowels(element):
    vowelCount = 0
    for character in element:
        # count = 0
        if vowelCount == 3:
            return True
        if character in vowels:
            vowelCount += 1
        else: continue

def evaluateList(list):
    for element in list:
        result = checkForVowels(element)
        if result: return True
        

lines = getListOfLines(file)
print(evaluateList(lines))