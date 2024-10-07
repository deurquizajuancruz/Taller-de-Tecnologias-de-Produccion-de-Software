from sys import stdin


def fill_array(sequence):
    sequence = list(sequence)
    n = len(sequence)
    equals = [0] * n
    for i in range(n - 2, -1, -1):
        equals[i] = equals[i + 1]
        if sequence[i] == sequence[i + 1]:
            equals[i] += 1
    return equals


sequence = stdin.readline().strip()  # Se lee el string
queries = int(stdin.readline().strip())  # Se lee la cantidad de queries
result_array = fill_array(sequence)
for i in range(queries):
    indexes = stdin.readline().strip().split(" ")
    print(result_array[int(indexes[0]) - 1] - result_array[int(indexes[1]) - 1])
