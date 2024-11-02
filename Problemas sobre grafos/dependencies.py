from sys import stdin


class Node:

    def __init__(self, content: int) -> None:
        self.content = content
        self.dependencies = []

    def add_dependency(self, dependency) -> None:
        self.dependencies.append(dependency)

    def get_dependencies(self) -> list:
        return self.dependencies

    def get_content(self) -> int:
        return self.content


class Graph:

    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, number: int, dependency: int) -> None:
        if number not in self.nodes:
            self.nodes[number] = Node(number)
        if dependency not in self.nodes:
            self.nodes[dependency] = Node(dependency)
        self.nodes[number].add_dependency(self.nodes[dependency])

    def count_dependencies(self, node, visited: set) -> int:
        if node.get_content() in visited:
            return 0
        visited.add(node.get_content())
        total: int = 0
        for visit in node.get_dependencies():
            if visit.get_content() not in visited:
                total += 1 + self.count_dependencies(visit, visited)
        return total

    def calculate_dependencies(self) -> int:
        minimum_content: int = -1
        maximum_dependencies: int = -1

        # Itero sobre todos los nodos de mi grafo
        for key, node in self.nodes.items():
            visited: set = set()
            dependencies: int = self.count_dependencies(node, visited)
            if dependencies > maximum_dependencies:
                maximum_dependencies = dependencies
                minimum_content = key
        return minimum_content


n: int = int(stdin.readline().strip())
while n != 0:
    my_graph = Graph()
    for i in range(n):
        dependencies = stdin.readline().strip().split()
        number: int = int(dependencies[0])
        for j in range(number):
            my_graph.add_node(i + 1, int(dependencies[j + 1]))
    print(my_graph.calculate_dependencies())
    n: int = int(stdin.readline().strip())
