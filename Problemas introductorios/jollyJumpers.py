def isJolly(sequence):
    size = int(sequence.split(' ')[0])
    if size == 1:
        return 'Jolly'
    numbers = sequence.split(' ')[1:size+1]
    allValues = [False] * (size - 1)
    numbers = [int(x) for x in numbers]
    for i in range(size-1):
        result = abs(numbers[i] - numbers[i + 1])
        if result >= size or result == 0 or allValues[result - 1]:
            return 'Not jolly'
        allValues[result - 1] = True
    return 'Jolly' if all(allValues) else 'Not jolly'

try:
    while True:
        entrada = input()
        if entrada:
            print(isJolly(entrada))
except:
    pass

# Jolly:
# 4 1 4 2 3
# 6 11 7 4 2 1 6
# 5 8 5 9 7 6
# 5 3 7 6 8 5
# 5 20 16 19 17 18
# Not Jolly: 
# 5 1 4 2 -1 6
# 4 11 13 10 12
# 5 2 5 1 4 3