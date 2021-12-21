import numpy as np

input_file = open("day06_inputs.txt", 'r')
inputs = input_file.read().split(',')

fish = np.array(inputs).astype(int)

days_left = {} # keys = days left, vals = number of fish
for i in range(9):
    days_left[i] = 0

for i in fish:
    days_left[i] += 1

for i in range(256):
    spawn = days_left[0]
    for j in range(8):
        days_left[j] = days_left[j+1]
    days_left[8] = spawn
    days_left[6] += spawn

    if i == 79:
        print(sum(days_left.values())) # 375482

print(sum(days_left.values()))