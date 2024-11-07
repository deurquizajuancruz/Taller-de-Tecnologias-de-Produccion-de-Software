from sys import stdin
from math import sqrt


def distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def escape(holes: list[tuple[float, float]]) -> str:
    for hole in holes:
        if distance((x_dog, y_dog), hole) >= distance((x_gopher, y_gopher), hole) * 2:
            return f"The gopher can escape through the hole at ({hole[0]:.3f},{hole[1]:.3f})."

    return "The gopher cannot escape."


while True:
    line: list[str] = stdin.readline().strip().split()
    if not line:
        break
    number_holes: int = int(line[0])
    coord: list[float] = list(map(float, line[1:]))
    x_gopher, y_gopher, x_dog, y_dog = coord[0], coord[1], coord[2], coord[3]
    holes: list[tuple[float, float]] = []
    for _ in range(number_holes):
        holes.append(tuple(map(float, stdin.readline().split())))
    print(escape(holes))
    stdin.readline()
