from sys import stdin

dictionary = {}

for line in stdin:
    numbers = line.strip().split()
    for number in numbers:
        if number not in dictionary.keys():
            dictionary[number] = 1
        else:
            dictionary[number] += 1

for key, value in dictionary.items():
    print(f"{key} {value}")
