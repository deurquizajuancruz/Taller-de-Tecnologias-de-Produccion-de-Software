from sys import stdin


class UFDS:

    def __init__(self, n: int) -> None:
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


n_m = stdin.readline().strip().split()
number_case: int = 1
while n_m != ["0", "0"]:
    n: int = int(n_m[0])
    m: int = int(n_m[1])
    ufds = UFDS(n)
    for _ in range(m):
        students = stdin.readline().strip().split()
        ufds.union_set(int(students[0]) - 1, int(students[1]) - 1)

    religions = {}
    for j in range(n):
        religion = ufds.find_set(j)
        if religion not in religions:
            religions[religion] = 1
        else:
            religions[religion] += 1

    print(f"Case {number_case}: {len(religions.keys())}")
    number_case += 1
    n_m = stdin.readline().strip().split()
