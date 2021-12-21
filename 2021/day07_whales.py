import numpy as np

input_file = open("day07_inputs.txt", 'r')
inputs = input_file.read().split(',')

positions = np.array(inputs).astype(int)

# part 1
min_fuel = 99**99
min_fuel_pos = -1
for pos in range(positions.min(), positions.max()+1):
    dif = abs(positions - pos)
    if dif.sum() < min_fuel:
        min_fuel = dif.sum()
        min_fuel_pos = pos

print(min_fuel_pos, min_fuel)


# part 2
min_fuel = 99**99
min_fuel_pos = -1
for pos in range(positions.min(), positions.max()+1):
    dif = abs(positions - pos)
    dif_cost = np.array([sum(range(d+1)) for d in dif]).astype(int)
    if dif_cost.sum() < min_fuel:
        min_fuel = dif_cost.sum()
        min_fuel_pos = pos

print(min_fuel_pos, min_fuel) #95221573 too low
