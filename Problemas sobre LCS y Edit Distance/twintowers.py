from sys import stdin

def lcs(string1: str, string2: str) -> int:
    len1 = len(string1) + 1
    len2 = len(string2) + 1

    matrix = [[0] * len2 for _ in range(len1)]

    for i in range(1, len1):
        for j in range(1, len2):
            if string1[i - 1] == string2[j - 1]:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[len1 - 1][len2 - 1]


heights = stdin.readline().strip().split()
cases = 1
while heights != ['0', '0']:
    tower1 = list(map(int, stdin.readline().split()))
    tower2 = list(map(int, stdin.readline().split()))
    print(f'Twin Towers #{cases}')
    print(f'Number of Tiles : {lcs(tower1, tower2)}')
    print()
    cases+=1
    heights = stdin.readline().strip().split()