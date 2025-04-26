import copy
import time
from sys import stdin


class Edge:

    def __init__(self, origin, target, capacity: int):
        self.origin = origin
        self.target = target
        self.capacity = capacity
        self.flow = 0

    def get_target(self):
        return self.target

    def get_origin(self):
        return self.origin

    def get_capacity(self):
        return self.capacity

    def get_target_content(self) -> str:
        return self.target.get_content()

    def get_origin_content(self) -> str:
        return self.origin.get_content()

    def get_available_capacity(self) -> int:
        return self.capacity - self.flow

    def send_flow(self, amount: int) -> None:
        self.flow += amount

    def is_saturated(self) -> bool:
        return self.capacity == self.flow

    def increase_capacity(self, amount: int) -> None:
        self.capacity += amount


class Node:

    def __init__(self, content: str):
        self.content = content
        self.adjacent = []

    def add_adjacent(self, adjacent, weight: int):
        edge = Edge(self, adjacent, weight)
        self.adjacent.append(edge)
        return edge

    def get_content(self) -> str:
        return self.content

    def get_adjacents(self) -> list:
        return self.adjacent

    def get_edge_to(self, target):
        return next(
            (edge for edge in self.adjacent if edge.get_target() == target), None
        )

    def add_edge(self, edge):
        self.adjacent.append(edge)


class Graph:

    def __init__(self):
        self.nodes = []

    def add_node(self, n) -> None:
        self.nodes.append(n)

    def get_node_by_content(self, content: str):
        return next(
            (node for node in self.nodes if node.get_content() == content), None
        )

    def dfs(self, current, target, path, visited) -> list:
        if current == target:
            return list(path)

        visited.add(current)

        for edge in current.get_adjacents():
            if not edge.is_saturated() and edge.get_target() not in visited:
                path.append(edge)
                result: list = self.dfs(edge.get_target(), target, path, visited)
                if result:
                    return result
                path.pop()

        return None
    
    def bfs(self, origin, target) -> list:
        queue: list = []
        visited = set()
        dictionary: dict = {}

        queue.append(origin)
        visited.add(origin)

        while (len(queue) > 0):
            current = queue.pop(0)
            if current == target:
                path = []
                while not target == origin:
                    edge = dictionary[target]
                    path.append(edge)
                    target = edge.get_origin()
                path.reverse()
                return path
            for edge in current.get_adjacents():
                edge_target = edge.get_target()
                if not edge.is_saturated() and edge_target not in visited:
                    visited.add(edge_target)
                    queue.append(edge_target)
                    dictionary[edge_target] = edge
        
        return None

    def ford_fulkerson(self, origin, target) -> int:
        max_flow: int = 0
        residual = self.clone()
        residual_origin, residual_target = residual.get_node_by_content(
            origin
        ), residual.get_node_by_content(target)
        path: list = residual.dfs(residual_origin, residual_target, [], set())
        #path: list = residual.bfs(residual_origin, residual_target)
        while path:
            #iterations += 1
            path_capacity: int = min(edge.get_available_capacity() for edge in path)
            print(f"Capacity: {path_capacity}")
            max_flow += path_capacity
            for edge in path:
                edge.send_flow(path_capacity)
                reverse_edge = edge.get_target().get_edge_to(edge.get_origin())
                if not reverse_edge:
                    reverse_edge = edge.get_target().add_adjacent(edge.get_origin(), 0)
                reverse_edge.increase_capacity(path_capacity)
            #path = residual.bfs(residual_origin, residual_target)
            path = residual.dfs(residual_origin, residual_target, [], set())
        return max_flow
    
    def clone(self):
        return copy.deepcopy(self)


number_network: int = 1
number_nodes: int = int(stdin.readline().strip())
while number_nodes:
    my_graph = Graph()
    for i in range(number_nodes):
        my_graph.add_node(Node(str(i + 1)))

    info: list = stdin.readline().split()
    origin: str = info[0]
    destination: str = info[1]
    number_connections: int = int(info[2])

    for _ in range(number_connections):
        info = stdin.readline().split()
        my_graph.get_node_by_content(info[0]).add_adjacent(
            my_graph.get_node_by_content(info[1]), int(info[2])
        )
        my_graph.get_node_by_content(info[1]).add_adjacent(
            my_graph.get_node_by_content(info[0]), int(info[2])
        )
    result = my_graph.ford_fulkerson(origin, destination)
    print(f"Network {number_network}")
    print(f"The bandwidth is {result}.\n")
    number_network += 1
    number_nodes = int(stdin.readline().strip())
