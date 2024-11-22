from sys import stdin


def edit(stringA: str, stringB: str) -> int:
    len1: int = len(stringA) + 1
    len2: int = len(stringB) + 1

    memo = [[0] * len2 for _ in range(len1)]

    for i in range(len1):
        memo[i][0] = i
    for i in range(len2):
        memo[0][i] = i

    for i in range(1, len1):
        for j in range(1, len2):
            memo[i][j] = memo[i - 1][j - 1]
            if not stringA[i - 1] == stringB[j - 1]:
                memo[i][j] = min(memo[i][j] + 1, memo[i - 1][j] + 1, memo[i][j - 1] + 1)

    return memo[len1 - 1][len2 - 1]


cases: int = int(stdin.readline().strip())
for _ in range(cases):
    string_a: str = stdin.readline().strip()
    string_b: str = stdin.readline().strip()
    print(edit(string_a, string_b))
