from sys import stdin

def jump_buildings(n, heights):
    min_energy = [float("inf")] * n
    min_energy[0] = 0
    for i in range(n):
        # Itero sobre las potencias de 2
        jump = 1
        while (i + jump) < n:
            # Edificio al que salta
            j = i + jump
            energy = abs(heights[j] - heights[i])
            # Mínimo entre la energía que tenía y la nueva energía + lo que cuesta llegar al edificio donde estoy
            min_energy[j] = min(min_energy[j], energy + min_energy[i])
            jump *= 2
    return min_energy[n - 1]


input_data = stdin.read().strip().splitlines()

for i in range(0, len(input_data), 2):
    n = int(input_data[i])
    heights = list(map(int, input_data[i + 1].split()))
    print(jump_buildings(n, heights))
