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
    if vowelCount == 3: return True
    return False

def checkForConsecutiveLetters(element):
    count = 0
    for character in element:
        try:    
            if character in element[count + 1] == character:
                return True
            else: count += 1
        except IndexError:
            return False

def checkForBadStrings(badStrings, element):
    for badVowel in badStrings:
        if badVowel in element:
            return False
        else: continue
    return True
        

def evaluateList(list):
    for element in list:
        resultForVowels = checkForVowels(element)
        resultForConsecutiveLetters = checkForConsecutiveLetters(element)
        resultForBadStrings = checkForBadStrings(badStrings, element)
        
        if resultForVowels and resultForConsecutiveLetters and resultForBadStrings: return True
        else: return False

lines = getListOfLines(file)
print(evaluateList(lines))