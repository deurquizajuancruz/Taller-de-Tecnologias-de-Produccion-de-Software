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
        self.calles = []
        self.n = n
        self.conexiones = [[] for _ in range(n)]

    def agregar_calle(self, peso: int, primero: int, segundo: int) -> None:
        self.calles.append((peso, primero, segundo))

    def mst(self) -> None:
        ufds = UFDS(self.n)
        self.calles.sort()
        for intensidad, calle1, calle2 in self.calles:
            if ufds.find_set(calle1) != ufds.find_set(calle2):
                ufds.union_set(calle1, calle2)
                self.conexiones[calle1].append((calle2, intensidad))
                self.conexiones[calle2].append((calle1, intensidad))
    
    def max_intensidad_camino(self, origen: int, destino: int):
        visitado = [False] * self.n
        return self.dfs(origen, destino, visitado, -1)

    def dfs(self, origen: int, destino: int, visitado: list, max_actual: int) -> int:
        if origen == destino:
            return max_actual
        visitado[origen] = True
        for conexion, intensidad in self.conexiones[origen]:
            if not visitado[conexion]:
                maximo = self.dfs(conexion, destino, visitado, max(max_actual, intensidad))
                if maximo != -1:
                    return maximo
        return -1

first_data = stdin.readline().strip().split()
number_case: int = 1
resultados = []
while first_data != ["0", "0", "0"]:
    c: int = int(first_data[0])
    s: int = int(first_data[1])
    q: int = int(first_data[2])
    my_graph = Graph(c)
    for _ in range(s):
        line = stdin.readline().strip().split()
        first: int = int(line[0])
        second: int = int(line[1])
        weight: int = int(line[2])
        my_graph.agregar_calle(weight, first - 1, second - 1)
    my_graph.mst()
    resultados.append(f"Case #{number_case}")
    for _ in range(q):
        query = stdin.readline().strip().split()
        calle1: int = int(query[0])
        calle2: int = int(query[1])
        minmax: int = my_graph.max_intensidad_camino(calle1 - 1, calle2 - 1)
        resultados.append(str(minmax) if minmax != -1 else "no path")
    resultados.append("")
    number_case+=1
    first_data = stdin.readline().strip().split()
print("\n".join(resultados).strip())