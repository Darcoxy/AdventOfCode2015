file = open(r"C:\Users\postl\Desktop\Personal\Projects\AdventOfCode2015\Day5\input.txt")
vowels = ['a', 'e', 'i', 'o', 'u']
badStrings = ['ab', 'cd', 'pq', 'xy']
niceCount = 0
naughtyCount = 0

def getListOfLines(file):
    with open(r"C:\Users\postl\Desktop\Personal\Projects\AdventOfCode2015\Day5\input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

def checkForPairs(element):
    count = 0
    for character in element:
        try:
            pair = element[count] + element[count + 1]
            if pair in element:
                newString = element.replace(pair, '', 1)
                if pair in newString:
                    return True
        except IndexError:
            return False
        
def checkForRepeatCharacters(element):
    count = 0
    for character in element:
        try:
            if character in element[count + 2] == character:
                return True
        except IndexError:
            return False

def evaluateList(list):
    goodCount = 0
    for element in list:
        #tests for strings
         if checkForPairs(element) and checkForRepeatCharacters(element):
             goodCount += 1
    return goodCount

lines = getListOfLines(file)
print(evaluateList(lines))