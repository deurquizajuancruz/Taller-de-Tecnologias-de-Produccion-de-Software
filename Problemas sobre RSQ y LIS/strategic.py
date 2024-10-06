from sys import stdin


def max_hits(missiles):
    n = len(missiles)
    lis = [1] * n
    prev = [-1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if missiles[i] < missiles[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j

    max_index = 0
    for i in range(1, n):
        if lis[i] > lis[max_index]:
            max_index = i

    hits = []
    current = max_index
    while current != -1:
        hits.append(missiles[current])
        current = prev[current]
    return hits

input = stdin.read().splitlines()
cases = int(input[0].strip())
index = 2

for i in range(cases):
    missiles = []
    while index < len(input) and input[index].strip() != "":
        missiles.append(int(input[index].strip()))
        index += 1
    targets = max_hits(missiles)
    print(f'Max hits: {len(targets)}')
    for t in targets:
        print(t)
    if i < cases - 1:
        print()
    index += 1
