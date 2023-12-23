import hashlib

input = 'abcdef609043'
target = '00000'

result = hashlib.md5(input.encode())
print(result.hexdigest())
