from sys import stdin


def knapsack(suitcases, maximum):
    len1 = len(suitcases) + 1
    len2 = maximum + 1

    matrix = [[0] * len2]  # Primer fila inicializada en 0
    for _ in range(1, len1):
        matrix.append(
            [0] + [None] * (len2 - 1)
        )  # Primer columna en 0 y el resto en None

    for i in range(1, len1):
        for j in range(1, len2):
            if suitcases[i - 1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(
                    matrix[i - 1][j],
                    matrix[i - 1][j - suitcases[i - 1]] + suitcases[i - 1],
                )

    return matrix[len1 - 1][len2 - 1]


cases = int(stdin.readline().strip())
for _ in range(cases):
    suitcases = list(map(int, stdin.readline().split()))
    maximum = sum(suitcases) / 2

    if not maximum.is_integer():
        result = "NO"
    else:
        maximum = int(maximum)
        result = "YES" if knapsack(suitcases, maximum) == maximum else "NO"
    print(result)
