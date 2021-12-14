import numpy as np

input_file = open("day03_inputs.txt", 'r') #open("day03_test_inputs.txt", 'r')
inputs = input_file.read().split('\n')

np_inputs = np.array([list(x) for x in inputs]).astype(np.int0)

ones_counts = np_inputs.sum(axis=0)

gamma_list = np.array([1 if x > len(np_inputs)/2 else 0 for x in ones_counts]).astype(str)
gamma = int(''.join(gamma_list), 2)

epsilon_list = np.array([0 if x > len(np_inputs)/2 else 1 for x in ones_counts]).astype(str)
epsilon = int(''.join(epsilon_list), 2)

print(gamma*epsilon)




most = np_inputs
o2_output = ""
for i in range(len(inputs[0])):
    count = most.sum(axis=0)[i]
    if count >= len(most)/2:
        o2_output += "1"
    else:
        o2_output += "0"

    most = most[[row[i] == int(o2_output[-1]) for row in most]]


least = np_inputs
co2_output = ""
for i in range(len(inputs[0])):
    if len(least) == 1:
        for j in range(i, len(inputs[0])):
            co2_output += str(least[0][j])
        break
    
    count = least.sum(axis=0)[i]
    if count < len(least)/2:
        co2_output += "1"
    else:
        co2_output += "0"

    least = least[[row[i] == int(co2_output[-1]) for row in least]]

o2_val = int(o2_output, 2)
co2_val = int(co2_output, 2)

print(o2_val * co2_val)