import numpy as np

input_file = open("day05_inputs.txt", 'r')
inputs = input_file.read().split('\n')

vents = []
max_row = 0
max_col = 0

for line in inputs:
    x1 = int(line[:line.find(",")])
    y1 = int(line[line.find(",")+1:line.find(" ")])

    two = line[line.find(" -> ")+4:]
    x2 = int(two[:two.find(",")])
    y2 = int(two[two.find(",")+1:])

    max_row = max(max_row, x1, x2)
    max_col = max(max_col, y1, y2)
    vents.append([x1, y1, x2, y2])


def part1():
    ocean = np.zeros((max_row+2, max_col+2))

    for vent in vents:

        if vent[0]==vent[2] or vent[1]==vent[3]:
            x1 = min(vent[1],vent[3])
            x2 = max(vent[1],vent[3])+1
            y1 = min(vent[0],vent[2])
            y2 = max(vent[0],vent[2])+1
            ocean[x1:x2, y1:y2] += 1

    return len(ocean[ocean > 1])


def part2():
    ocean = np.zeros((max_row+2, max_col+2))

    for vent in vents:

        if vent[0]==vent[2] or vent[1]==vent[3]:
            x1 = min(vent[1],vent[3])
            x2 = max(vent[1],vent[3])+1
            y1 = min(vent[0],vent[2])
            y2 = max(vent[0],vent[2])+1
            ocean[x1:x2, y1:y2] += 1

        else:
            x_counter = 1 if vent[3] > vent[1] else -1
            y_counter = 1 if vent[2] > vent[0] else -1
            x = vent[1]
            y = vent[0]
            while x != vent[3] and y != vent[2]:
                ocean[x, y] += 1
                x += x_counter
                y += y_counter
            ocean[x, y] += 1
    # print(ocean[:-1, :-1].astype(int))
    return len(ocean[ocean > 1])

print(part1())
print(part2()) #22091 too low