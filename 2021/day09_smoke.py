import numpy as np

input_file = open("day09_inputs.txt", 'r')
inputs = input_file.read().split('\n')

ocean = []
for line in inputs:
    ocean.append(list(line))
ocean = np.array(ocean).astype(int)


def find_basin(x, y, ocean, basin_set):
    basin_set.add((x,y))

    if x-1 >= 0 and ocean[x-1][y] > ocean[x][y] and ocean[x-1][y] != 9:
        find_basin(x-1, y, ocean, basin_set)
    if y+1 < len(ocean[0]) and ocean[x][y+1] > ocean[x][y] and ocean[x][y+1] != 9:
        find_basin(x, y+1, ocean, basin_set)
    if x+1 < len(ocean) and ocean[x+1][y] > ocean[x][y] and ocean[x+1][y] != 9:
        find_basin(x+1, y, ocean, basin_set)
    if y-1 >= 0 and ocean[x][y-1] > ocean[x][y] and ocean[x][y-1] != 9:
        find_basin(x, y-1, ocean, basin_set)

    return len(basin_set)


def is_lowest(x, y, ocean):
    for xi in range(max(0, x-1), min(len(ocean), x+2)):
        for yi in range(max(0, y-1), min(len(ocean[0]), y+2)):
            if not (xi == x and yi == y) and ocean[xi][yi] < ocean[x][y]:
                return 0
    # return 1 + ocean[x][y] # part 1
    return find_basin(x, y, ocean, set())



score = 0 # part 1
scores = []
for x in range(len(ocean)):
    for y in range(len(ocean[0])):
        # score += is_lowest(x, y, ocean) # part 1
        size = is_lowest(x, y, ocean)
        if size > 0:
            scores.append(size)
        

# print(score) # 502
print(np.prod(sorted(scores)[-3:]))

