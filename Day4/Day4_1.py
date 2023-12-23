import hashlib

def findHash(valueToHash):
    result = hashlib.md5(valueToHash.encode())
    return result.hexdigest()

def createCandidate(input, number):
    candidate = input + str(number)
    return candidate

input = 'abcdef'
# target = '00000'
count = 0
firstCharacters = ''

while firstCharacters != '00000':
    candidate = createCandidate(input, count)
    hashed = findHash(candidate)
    firstCharacters = hashed[0:5]
    print(count)
    if firstCharacters == '00000':
        print(candidate)
        print(hashed)
        break
    else:
        count += 1