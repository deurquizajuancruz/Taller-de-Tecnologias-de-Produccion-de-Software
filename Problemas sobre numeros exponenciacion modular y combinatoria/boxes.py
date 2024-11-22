from sys import stdin

cases: int = int(stdin.readline().strip())
for _ in range(cases):
    line: str = stdin.readline().strip().split()
    line: list = list(map(int, line))
    friends, boxes = line[0], line[1]
    total: int = 0
    for _ in range(boxes):
        small_boxes: str = stdin.readline().strip().split()
        small_boxes: list = list(map(int, small_boxes))
        times: int = small_boxes[0]
        result: int = 1
        for i in range(times):
            result *= small_boxes[i + 1]
        total += result
    print(total % friends)
