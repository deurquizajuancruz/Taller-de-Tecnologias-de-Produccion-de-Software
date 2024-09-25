from sys import stdin
dictionary = {}

def translate(message):
    return dictionary.get(message, 'eh')
    

while True:
    line = input().strip()
    if not line:
        break
    line = line.split(' ')
    dictionary[line[1]] = line[0]

while True:
    message = stdin.readline().strip()
    if not message:
        break
    print(translate(message))