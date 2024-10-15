from sys import stdin


def knapsack(bars, maximum) -> int:
    len1 = len(bars) + 1
    len2 = maximum + 1

    matrix = [[0] * len2]  # Primer fila inicializada en 0
    for _ in range(1, len1):
        matrix.append(
            [0] + [None] * (len2 - 1)
        )  # Primer columna en 0 y el resto en None

    for i in range(1, len1):
        for j in range(1, len2):
            if bars[i - 1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(
                    matrix[i - 1][j],
                    matrix[i - 1][j - bars[i - 1]] + bars[i - 1],
                )

    return matrix[len1 - 1][len2 - 1]


cases = int(stdin.readline().strip())
for _ in range(cases):
    wish = int(stdin.readline().strip())
    number_bars = int(stdin.readline().strip())
    bars = list(map(int, stdin.readline().split()))
    print("YES" if knapsack(bars, wish) == wish else "NO")