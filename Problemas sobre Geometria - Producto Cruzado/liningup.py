from sys import stdin


def max_points(points: list[tuple[int, int]]) -> int:
    r: int = 0
    n: int = len(points)
    for i in range(n):
        m = []
        for j in range(i + 1, n):
            if points[i][0] != points[j][0]:
                m.append((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]))
            else:
                m.append(float("inf"))
        m.sort()
        t: int = 1
        for j in range(len(m) - 1):
            if abs(m[j] - m[j + 1]) < 1e-9:
                t += 1
            else:
                if t > r:
                    r = t
                t = 1
        if t > r:
            r = t
    return r + 1


n: int = int(stdin.readline().strip())
stdin.readline()
for i in range(n):
    points: list[tuple[int, int]] = []
    while True:
        line: str = stdin.readline().strip()
        if not line:
            break
        points.append(tuple(map(int, line.split())))
    print(max_points(points))
    if i < n - 1:
        print()
