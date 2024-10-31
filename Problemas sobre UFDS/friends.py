from sys import stdin


class UFDS:

    def __init__(self):
        self.parent = {}
        self.size = {}

    def find_set(self, person: str) -> str:
        if person not in self.parent:
            self.parent[person] = person
            self.size[person] = 1

        if self.parent[person] != person:
            self.parent[person] = self.find_set(self.parent[person])
        return self.parent[person]

    def union_set(self, first: str, second: str) -> int:
        x: str = self.find_set(first)
        y: str = self.find_set(second)

        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
                return self.size[y]
            self.parent[y] = x
            self.size[x] += self.size[y]
        return self.size[x]


number_cases: int = int(stdin.readline().strip())
for _ in range(number_cases):
    formed: int = int(stdin.readline().strip())
    ufds = UFDS()
    for _ in range(formed):
        names: list[str] = stdin.readline().strip().split(" ")
        person1, person2 = names[0], names[1]
        print(ufds.union_set(person1, person2))
