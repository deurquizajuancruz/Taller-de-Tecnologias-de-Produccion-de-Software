from sys import stdin


def lcs(string1: str, string2: str) -> int:
    len1 = len(string1) + 1
    len2 = len(string2) + 1

    matrix = [[0] * len2]
    for _ in range(1, len1):
        row = [0] + [None] * (len2 - 1)
        matrix.append(row)

    for i in range(1, len1):
        for j in range(1, len2):
            if string1[i - 1] == string2[j - 1]:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[len1 - 1][len2 - 1]


str1 = stdin.readline().strip()
cases = 1
while str1 != "#":
    str2 = stdin.readline().strip()
    print(f"Case #{cases}: you can visit at most {lcs(str1, str2)} cities.")
    cases += 1
    str1 = stdin.readline().strip()
