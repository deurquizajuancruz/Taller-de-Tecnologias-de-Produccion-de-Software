from sys import stdin
from math import sqrt


def distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest_pair(x: list[tuple[float, float]], y: list[tuple[float, float]]) -> float:
    n: int = len(x)

    if n == 2:
        return distance(x[0], x[1])

    if n == 3:
        return min(distance(x[0], x[1]), distance(x[1], x[2]), distance(x[0], x[2]))

    mid: int = n // 2
    midpoint: float = x[mid][0]

    left_x: list[tuple[float, float]] = x[:mid]
    right_x: list[tuple[float, float]] = x[mid:]
    left_y: list[tuple[float, float]] = [point for point in y if point[0] <= midpoint]
    right_y: list[tuple[float, float]] = [point for point in y if point[0] > midpoint]

    left: float = closest_pair(left_x, left_y)
    right: float = closest_pair(right_x, right_y)
    d: float = min(left, right)

    strip: list[tuple[float, float]] = [point for point in y if abs(point[0] - midpoint) < d]

    strip_len: int = len(strip)
    for i in range(strip_len):
        for j in range(i + 1, min(i + 8, strip_len)):
            d = min(d, distance(strip[i], strip[j]))
    return d


n: int = int(stdin.readline().strip())
while n != 0:
    points: list[tuple[float, float]] = []
    for _ in range(n):
        points.append(tuple(map(float, stdin.readline().strip().split())))

    if len(points) < 2:
        print("INFINITY")
    else:
        sorted_x: list[tuple[float, float]] = sorted(points, key=lambda x: x[0])
        sorted_y: list[tuple[float, float]] = sorted(points, key=lambda x: x[1])

        min_distance: float = closest_pair(sorted_x, sorted_y)
        if min_distance >= 10000:
            print("INFINITY")
        else:
            print("{:.4f}".format(min_distance))
    n = int(stdin.readline().strip())
