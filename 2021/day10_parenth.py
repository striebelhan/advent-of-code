import numpy as np

input_file = open("day10_inputs.txt", 'r')
inputs = input_file.read().split('\n')

start = '([{<'
end = ')]}>'
pairs = {'(':')', '[':']', '{':'}', '<':'>'}
points_pt1 = {')':3, ']':57, '}':1197, '>':25137}
points_pt2 = {')':1, ']':2, '}':3, '>':4}

score_pt1 = 0
pt2_list = []
for line in inputs:
    stack = []
    valid = True
    for ch in list(line):
        if ch in start:
            stack.append(ch)
        elif ch in end:
            match = stack.pop()
            if pairs[match] != ch:
                score_pt1 += points_pt1[ch]
                valid = False
                break

    if valid:
        score_pt2 = 0
        while len(stack) > 0:
            ch = stack.pop()
            pts = points_pt2[pairs[ch]]
            score_pt2 *= 5
            score_pt2 += pts
        
        pt2_list.append(score_pt2)

print(score_pt1) #318081
print(sorted(pt2_list)[int(len(pt2_list)/2)]) # 4361305341