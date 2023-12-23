import hashlib

def findHash(valueToHash):
    result = hashlib.md5(valueToHash.encode())
    return result.hexdigest()

def createCandidate(input, number):
    candidate = input + str(number)
    return candidate

input = 'iwrupvqb'
count = 0
firstCharacters = ''

while firstCharacters != '000000':
    candidate = createCandidate(input, count)
    hashed = findHash(candidate)
    firstCharacters = hashed[0:6]
    if firstCharacters == '000000':
        print(candidate)
        print(hashed)
        break
    else:
        count += 1