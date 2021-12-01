import math


input_file = open("day03_input.txt", 'r')
inputs = input_file.read().split("\n")
size = len(inputs[0])

def day03(row_increment, col_increment):
    row = 0
    col = 0
    trees = 0
    while row < len(inputs):
        if inputs[row][col] == '#':
            trees += 1
        row += row_increment
        col = (col + col_increment) % size

    return trees

# part 1
print(day03(1, 3))


# part 2
increments = [(1,1), (1,3), (1,5), (1,7), (2,1)]
print(math.prod([day03(*increments[i]) for i in range(len(increments))]))
