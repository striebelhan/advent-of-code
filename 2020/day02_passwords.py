input_file = open("day02_input.txt", 'r')
inputs = input_file.read().split("\n")
# inputs = [int(inputs[i]) for i in range(len(inputs))]

count = 0
for line in inputs:
    dash = line.index("-")
    space = line.index(" ")
    min = int(line[:dash])
    max = int(line[dash+1:space])
    letter = line[space+1]
    password = line[space+4:]
    letter_count = password.count(letter)

    if min <= letter_count and letter_count <= max:
        count += 1

print(count)


count = 0
for line in inputs:
    dash = line.index("-")
    space = line.index(" ")
    min = int(line[:dash])
    max = int(line[dash+1:space])
    letter = line[space+1]
    password = line[space+4:]

    if (password[min-1] == letter) ^ (password[max-1] == letter):
        count += 1

print(count)