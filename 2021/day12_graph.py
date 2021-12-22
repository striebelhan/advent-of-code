import numpy as np

input_file = open("day12_inputs.txt", 'r')
inputs = input_file.read().split('\n')

adj_list = {}
visited = []
path_count = 0

for line in inputs:
    node1 = line[:line.find('-')]
    node2 = line[line.find('-')+1:]
    if node1 not in adj_list.keys():
        adj_list[node1] = []
    if node2 not in adj_list.keys():
        adj_list[node2] = []
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

def is_caps(string):
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in string:
        if ch not in caps:
            return False
    return True

def explore(path):
    current_node = path[-1]

    if current_node == "end":
        # print(path)
        global path_count
        path_count += 1
        return

    for node in adj_list[current_node]:
        if node not in path or is_caps(node):
            # print('trying node', node)
            path.append(node)
            explore(path)
            path.pop()


def explore_more(path, visited_small):
    current_node = path[-1]

    if current_node == "end":
        global path_count
        path_count += 1
        return

    for node in adj_list[current_node]:

        if node not in path or is_caps(node):
            path.append(node)
            explore_more(path, visited_small)
            path.pop()

        elif node != "start" and not visited_small:
            path.append(node)
            explore_more(path, True)
            path.pop()



# print(adj_list)

explore(["start"])
print(path_count) # pt1 5756

path_count = 0
explore_more(["start"], False)
print(path_count)