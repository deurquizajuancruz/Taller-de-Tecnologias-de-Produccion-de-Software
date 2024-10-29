from sys import stdin, stdout


class UFDS:

    def __init__(self, n: int):
        self.parent: list[int] = [i for i in range(n)]
        self.rank: list[int] = [0 for _ in range(n)]

    def find_set(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find_set(self.parent[i])
        return self.parent[i]

    def same_set(self, i: int, j: int) -> bool:
        return self.find_set(i) == self.find_set(j)

    def union_set(self, i: int, j: int) -> None:
        if not self.same_set(i, j):
            x: int = self.find_set(i)
            y: int = self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1


input = stdin.read().split()
index: int = 0
cases: int = int(input[index])
index += 1
results: list[str] = []

for _ in range(cases):
    n, m = int(input[index]), int(input[index + 1])
    index += 2
    ufds = UFDS(n)
    balance = {}
    debt: list[int] = []

    for _ in range(n):
        debt.append(int(input[index]))
        index += 1

    for _ in range(m):
        ufds.union_set(int(input[index]), int(input[index + 1]))
        index += 2

    for j in range(n):
        repr = ufds.find_set(j)
        if repr not in balance:
            balance[repr] = 0
        balance[repr] += debt[j]

    possible = all(value == 0 for value in balance.values())
    results.append("POSSIBLE" if possible else "IMPOSSIBLE")

stdout.write("\n".join(results) + "\n")
