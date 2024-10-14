from sys import stdin


def lis(elephants):
    n = len(elephants)
    lis = [1] * n
    prev = [-1] * n

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if elephants[i][1] > elephants[j][1] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j

    max_index = 0
    for i in range(1, n):
        if lis[i] > lis[max_index]:
            max_index = i
    return_elephants = []
    current = max_index
    while current != -1:
        return_elephants.append(elephants[current][2])
        current = prev[current]
    return return_elephants


elephants = []
line = stdin.readline().strip()
index = 1
while line:
    e = list(map(int, line.split()))
    e.append(index)
    elephants.append(e)
    index += 1
    line = stdin.readline().strip()

result = lis(sorted(elephants, key=lambda e: e[0]))
print(len(result))
for e in result:
    print(e)
