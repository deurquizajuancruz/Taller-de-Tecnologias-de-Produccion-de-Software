from sys import stdin


class Node:

    def __init__(self, content: str) -> None:
        self.content = content
        self.vertices = []

    def add_vertix(self, vertix) -> None:
        self.vertices.append(vertix)

    def get_vertix(self) -> list:
        return self.vertices

    def get_content(self) -> str:
        return self.content


class Graph:

    def __init__(self, n: int) -> None:
        self.nodes = {str(i + 1): Node(str(i+1)) for i in range(n)}
        self.n = n

    def add_node(self, vertix1: str, vertix2: str) -> None:
        if vertix1 in self.nodes and vertix2 in self.nodes:
            self.nodes[vertix1].add_vertix(self.nodes[vertix2])

    def bfs(self, initial: str, end: str) -> list:
        if initial not in self.nodes or end not in self.nodes:
            return "connection impossible"
        queue: list = []
        distances = {str(i + 1): float("inf") for i in range(self.n)}
        queue.append(initial)
        distances[initial] = 0
        predecessors = {str(i + 1): None for i in range(self.n)}


        while queue:
            t = queue.pop(0)
            for w in self.nodes[t].get_vertix():
                w_content: str = w.get_content()
                if distances[w_content] == float("inf"):
                    distances[w_content] = distances[t] + 1
                    queue.append(w_content)
                    predecessors[w_content] = t
                    if w_content == end:
                        queue.clear()
                        break
        
        if distances[end] == float("inf"):
            return "connection impossible"
        
        path = []
        while end is not None:
            path.append(end)
            end = predecessors[end]

        return list(reversed(path))


while True:
    line = stdin.readline().strip()
    if not line:
        break
    n: int = int(line)
    my_graph = Graph(n)
    for _ in range(n):
        line = stdin.readline().strip().split("-")
        before: str = line[0]
        after: list[str] = []
        if len(line[1]) > 0:
            after: list[str] = line[1].split(",")
        for connection in after:
            my_graph.add_node(before, connection)
    m: int = int(stdin.readline().strip())
    print('-----')
    for _ in range(m):
        line = stdin.readline().strip().split()
        start, end = line[0], line[1]
        result = my_graph.bfs(start, end)
        if result == "connection impossible":
            print(result)
        else:
            print(" ".join(map(str, result)))
