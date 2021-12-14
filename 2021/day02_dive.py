input_file = open("day02_inputs.txt", 'r')
inputs = input_file.read().split('\n')

pos = 0
depth = 0
for command in inputs:
    cmds = command.split()

    if cmds[0] == "forward":
        pos += int(cmds[1])
    elif cmds[0] == "down":
        depth += int(cmds[1])
    elif cmds[0] == "up":
        depth -= int(cmds[1])

print(pos*depth)


pos = 0
depth = 0
aim = 0
for command in inputs:
    cmds = command.split()

    if cmds[0] == "forward":
        pos += int(cmds[1])
        depth += aim * int(cmds[1])
    elif cmds[0] == "down":
        aim += int(cmds[1])
    elif cmds[0] == "up":
        aim -= int(cmds[1])

print(pos*depth)