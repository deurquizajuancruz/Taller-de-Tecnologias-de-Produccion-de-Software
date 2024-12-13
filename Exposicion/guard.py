from sys import stdin


def intersection(coordinates1: list, coordinates2: list) -> bool:
    return (
        (coordinates1[2] > coordinates2[0])
        and (coordinates2[2] > coordinates1[0])
        and (coordinates2[3] > coordinates1[1])
        and (coordinates1[3] > coordinates2[1])
    )


def areas(coordinates1: list, coordinates2: list) -> list:
    return_areas: list = []
    land_area: int = 10000
    area_guard1: int = (coordinates1[2] - coordinates1[0]) * (
        coordinates1[3] - coordinates1[1]
    )
    area_guard2: int = (coordinates2[2] - coordinates2[0]) * (
        coordinates2[3] - coordinates2[1]
    )
    area_intersection: int = 0
    there_is_intersection: bool = intersection(coordinates1, coordinates2)
    if there_is_intersection:
        starts_x: int = max(coordinates1[0], coordinates2[0])
        ends_x: int = min(coordinates1[2], coordinates2[2])
        starts_y: int = max(coordinates1[1], coordinates2[1])
        ends_y: int = min(coordinates1[3], coordinates2[3])
        area_intersection = (ends_y - starts_y) * (ends_x - starts_x)
        area_guard1 -= area_intersection
        area_guard2 -= area_intersection
    return_areas.append(area_intersection)
    area_guards: int = area_guard1 + area_guard2
    return_areas.append(area_guards)
    area_guards += area_intersection
    land_area = land_area - area_guards
    return_areas.append(land_area)
    return return_areas


nights: int = int(stdin.readline().strip())
for i in range(nights):
    guard1: list = list(map(int, stdin.readline().strip().split()))
    guard2: list = list(map(int, stdin.readline().strip().split()))
    results: list = areas(guard1, guard2)
    print(f"Night {i+1}: {results[0]} {results[1]} {results[2]}")
