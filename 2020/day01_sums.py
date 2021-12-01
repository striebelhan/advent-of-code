test_input = [1721, 979, 366, 299, 675, 1456]

input_file = open("day01_input.txt", 'r')
inputs = input_file.read().split()
inputs = [int(inputs[i]) for i in range(len(inputs))]

def day01_two():
    for i in range(len(inputs)):
        for j in range(len(inputs)):
            if inputs[i] + inputs[j] == 2020:
                print(inputs[i], inputs[j])
                return inputs[i] * inputs[j]


def day01_three():
    for i in range(len(inputs)):
        for j in range(len(inputs)):
            for k in range(len(inputs)):
                if inputs[i] + inputs[j] + inputs[k] == 2020:
                    print(inputs[i], inputs[j], inputs[k])
                    return inputs[i] * inputs[j] * inputs[k]


print(day01_two())
print(day01_three())