from sys import stdin
from string import ascii_uppercase


class Node:

    def __init__(self, content: str) -> None:
        self.content = content
        self.vertices = []

    def add_vertix(self, vertix) -> None:
        self.vertices.append(vertix)

    def get_content_number(self) -> int:
        return ord(self.content) - 65

    def get_vertices(self) -> list:
        return self.vertices


class Graph:

    def __init__(self, n: int) -> None:
        self.nodes = {ascii_uppercase[i]: Node(ascii_uppercase[i]) for i in range(n)}
        self.visited = [False for _ in range(n)]

    def add_node(self, vertix1: str, vertix2: str) -> None:
        self.nodes[vertix1].add_vertix(self.nodes[vertix2])
        self.nodes[vertix2].add_vertix(self.nodes[vertix1])

    def dfs(self, node) -> None:
        self.visited[node.get_content_number()] = True
        for vertice in node.get_vertices():
            if not self.visited[vertice.get_content_number()]:
                self.dfs(vertice)

    def number_subgraphs(self) -> int:
        number_subgraphs = 0
        for node in self.nodes.values():
            if not self.visited[node.get_content_number()]:
                number_subgraphs += 1
                self.dfs(node)
        return number_subgraphs


number_cases: int = int(stdin.readline().strip())
stdin.readline().strip()
for i in range(number_cases):
    max_node: int = ord(stdin.readline().strip()) - 64
    my_graph = Graph(max_node)
    while True:
        line = stdin.readline().strip()
        if not line:
            break
        my_graph.add_node(line[0], line[1])
    if i > 0:
        print()
    print(my_graph.number_subgraphs())
