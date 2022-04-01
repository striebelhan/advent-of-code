# template = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
# template_dict = {}
# for i in range(len(template)-1):
#     template_dict[template[i:i+2]] = 1 if template[i:i+2] not in template_dict.keys() else template_dict[template[i:i+2]] + 1
# print('after step 4 ' + str(template_dict) + '\n')


input_file = open("day14_inputs.txt", 'r')
inputs = input_file.read().split('\n')

template = inputs[0]
rules = {}

for i in range(2, len(inputs)):
    pair = inputs[i][:2]
    insert = inputs[i][-1]

    rules[pair] = insert



# encode template as dictionary
template_dict = {}
char_counts = {}
for i in range(len(template)-1):
    template_dict[template[i:i+2]] = 1 if template[i:i+2] not in template_dict.keys() else template_dict[template[i:i+2]] + 1
    char_counts[template[i]] = 1 if template[i] not in char_counts.keys() else char_counts[template[i]] + 1
char_counts[template[-1]] = 1 if template[-1] not in char_counts.keys() else char_counts[template[-1]] + 1

# print('starting point')
# print('template: ' + template)
# print('template_dict: ' + str(template_dict))
# print()

for step in range(40): # repeat x times
    new_template = {}
    # print(f'step {step+1}')
    polymers = list(template_dict.items())
    
    for key, val in polymers:

        # print(f'template_dict key={key} val={val}')

        if key in rules.keys():
            char_counts[rules[key]] = 1 if rules[key] not in char_counts.keys() else char_counts[rules[key]] + val
            # print(f'rule {key} -> {rules[key]}')
            # print('template_dict ' + str(template_dict))
            # print('new_template ' + str(new_template))
            # input('...')

            del template_dict[key]

            p1 = key[0] + rules[key]
            p2 = rules[key] + key[1]

            new_template[p1] = new_template.get(p1, 0) + val
            new_template[p2] = new_template.get(p2, 0) + val

        else:
            new_template[key] = val

    template_dict = new_template


# print(char_counts)
# print('length ' + str(sum([val for val in char_counts.values()])))
counts_list = sorted(char_counts.items(), key=lambda x:x[1])
print(counts_list[-1][1] - counts_list[0][1])