import math

input_file = open("day05_input.txt", 'r')
inputs = input_file.read().split()

seat_ids = []

for ticket in inputs:

    bot = 0
    top = 127
    for BF in ticket[:7]:
        if BF == "F":
            top = bot + math.floor((top-bot)/2)
        else:
            bot = bot + math.ceil((top-bot)/2)
    row = bot

    bot = 0
    top = 7
    for LR in ticket[7:]:
        if LR == "L":
            top = bot + math.floor((top-bot)/2)
        else:
            bot = bot + math.ceil((top-bot)/2)
    col = bot

    seat_ids.append(row*8 + col)

print(max(seat_ids))

seat_ids = sorted(seat_ids)
test = [seat_ids[i+1]-1 for i in range(1,len(seat_ids)-1) if seat_ids[i+1] - 1 != seat_ids[i] ]
print(test)