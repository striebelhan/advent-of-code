# test_depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open("day01_input.txt") as input_file:
    depths = input_file.read().split()
    depths = [int(depths[i]) for i in range(len(depths))]
    
    count = sum([1 if depths[i] > depths[i-1] else 0 for i in range(1,len(depths))])
    print(count)

    sliding_count = sum([1 if sum(depths[i:i+3]) < sum(depths[i+1:i+4]) else 0 for i in range(len(depths)-2)])
    print(sliding_count)
