from sys import stdin


class UFDS:

    def __init__(self, n: int):
        self.parent: list[int] = [i for i in range(n)]
        self.rank: list[int] = [0 for _ in range(n)]

    def find_set(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find_set(self.parent[i])
        return self.parent[i]

    def union_set(self, i: int, j: int) -> None:
        x: int = self.find_set(i)
        y: int = self.find_set(j)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1


class Graph:

    def __init__(self, n: int):
        self.streets = []
        self.n = n
        self.connections = [[] for _ in range(n)]

    def add_street(self, weight: int, first: int, second: int) -> None:
        self.streets.append((weight, first, second))

    def mst(self) -> None:
        ufds = UFDS(self.n)
        self.streets.sort()
        for weight, street1, street2 in self.streets:
            if ufds.find_set(street1) != ufds.find_set(street2):
                ufds.union_set(street1, street2)
                self.connections[street1].append((street2, weight))
                self.connections[street2].append((street1, weight))

    def max_intensity_path(self, origin: int, destiny: int) -> int:
        visited = [False] * self.n
        return self.dfs(origin, destiny, visited, -1)

    def dfs(self, origin: int, destiny: int, visited: list, actual_max: int) -> int:
        if origin == destiny:
            return actual_max
        visited[origin] = True
        for connection, intensity in self.connections[origin]:
            if not visited[connection]:
                maximum = self.dfs(
                    connection, destiny, visited, max(actual_max, intensity)
                )
                if maximum != -1:
                    return maximum
        return -1


first_data = stdin.readline().strip().split()
number_case: int = 1
results = []
while first_data != ["0", "0", "0"]:
    c, s, q = map(int, first_data)
    my_graph = Graph(c)
    for _ in range(s):
        line = stdin.readline().strip().split()
        first, second, weight = map(int, line)
        my_graph.add_street(weight, first - 1, second - 1)
    my_graph.mst()
    results.append(f"Case #{number_case}")
    for _ in range(q):
        query = stdin.readline().strip().split()
        street1, street2 = map(int, query)
        minmax: int = my_graph.max_intensity_path(street1 - 1, street2 - 1)
        results.append(str(minmax) if minmax != -1 else "no path")
    results.append("")
    number_case += 1
    first_data = stdin.readline().strip().split()
print("\n".join(results).strip())
