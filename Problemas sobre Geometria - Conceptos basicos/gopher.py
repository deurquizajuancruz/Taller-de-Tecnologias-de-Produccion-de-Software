from sys import stdin
from math import sqrt


def escape(holes: list[tuple]) -> str:
    can_escape: bool = False
    for hole in holes:
        distance_gopher: float = sqrt(
            (x_gopher - hole[0]) * (x_gopher - hole[0])
            + (y_gopher - hole[1]) * (y_gopher - hole[1])
        )
        distance_dog: float = sqrt(
            (x_dog - hole[0]) * (x_dog - hole[0])
            + (y_dog - hole[1]) * (y_dog - hole[1])
        )
        can_escape = distance_dog >= distance_gopher * 2
        if can_escape:
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
