import numpy as np

input_file = open("day11_inputs.txt", 'r')
inputs = input_file.read().split('\n')
energy = []
for line in inputs:
    energy.append(list(line))
energy = np.array(energy).astype(int)


count = 0
sync_count = 0


def increment_adjacent(x, y, ocean, has_flashed):
    for xi in range(max(0, x-1), min(len(ocean), x+2)):
        for yi in range(max(0, y-1), min(len(ocean[0]), y+2)):
            if not (xi == x and yi == y) and not has_flashed[xi][yi]:
                ocean[xi][yi] += 1
                if ocean[xi][yi] > 9:
                    global count
                    count += 1
                    ocean[xi][yi] = 0
                    has_flashed[xi][yi] = True
                    ocean, has_flashed = increment_adjacent(xi, yi, ocean, has_flashed)
    
    return ocean, has_flashed


i = 0
while True:
    has_flashed = np.zeros((10,10)).astype(bool)
    energy += 1

    for x in range(len(energy)):
        for y in range(len(energy[0])):
            if energy[x][y] > 9 and not has_flashed[x][y]:
                count += 1
                energy[x][y] = 0
                has_flashed[x][y] = True
                energy, has_flashed = increment_adjacent(x, y, energy, has_flashed)

    if i == 99:
        print(count)

    if has_flashed.all():
        print(i+1)
        break

    i += 1
