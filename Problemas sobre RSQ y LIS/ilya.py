from sys import stdin


def fill_array(sequence: list[int]) -> list[int]:
    """
    Llena un array con la cantidad de coincidencias de la secuencia por posición;
    utilizando programación dinámica
    Params:
        sequence: list[int]
            secuencia de string leídas
    Returns:
        equals: list[int]
            array con la cantidad de coincidencias de la secuencia leída por posición
    """
    n = len(sequence)
    equals = [0] * n
    for i in range(n - 2, -1, -1):
        equals[i] = equals[i + 1]
        if sequence[i] == sequence[i + 1]:
            equals[i] += 1
    return equals


sequence = stdin.readline().strip()  # Se lee el string
queries = int(stdin.readline().strip())  # Se lee la cantidad de queries
result_array = fill_array(list(sequence))
for _ in range(queries):
    indexes = stdin.readline().strip().split(" ")
    print(result_array[int(indexes[0]) - 1] - result_array[int(indexes[1]) - 1])
