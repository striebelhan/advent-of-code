# y is rows, x is cols

import numpy as np

input_file = open("day13_inputs.txt", 'r')
inputs = input_file.read().split('\n')

# CONFIGURE DATA
dots = []
max_row = 0
max_col = 0
i = 0
while inputs[i] != "":
    line = inputs[i]
    col = int(line[:line.find(',')])
    row = int(line[line.find(',')+1:])
    dots.append((row,col))

    max_row = max(max_row, row)
    max_col = max(max_col, col)

    i += 1


# MARK DOTS
paper = np.zeros((max_row+1, max_col+1)).astype(bool)
for dot in dots:
    paper[dot[0]][dot[1]] = True

print(paper.shape)

# FOLD
i += 1
pt1 = True
while i < len(inputs):
    fold = inputs[i]
    axis = int(fold[fold.find('=')+1:])
    # print(fold)
    
    if fold[11] == 'y':
        # fold on row
        after_crease = np.flip(paper[axis+1:,:], 0)
        paper = paper[:axis]
        if paper.shape != after_crease.shape:
            to_add = np.zeros((abs(paper.shape[0]-after_crease.shape[0]), paper.shape[1])).astype(bool)
            if paper.shape[0] < after_crease.shape[0]:
                paper = np.append(to_add, paper, 0)
            else:
                after_crease = np.append(to_add, after_crease, 0)
    elif fold[11] == 'x':
        # fold on col
        after_crease = np.flip(paper[:,axis+1:], 1)
        paper = paper[:,:axis]
        if paper.shape != after_crease.shape:
            to_add = np.zeros((paper.shape[0], abs(paper.shape[1]-after_crease.shape[1]))).astype(bool)
            if paper.shape[1] < after_crease.shape[1]:
                paper = np.append(to_add, paper, 1)
            else:
                after_crease = np.append(to_add, after_crease, 1)
    
    # print(after_crease.shape)
    # print(paper.shape)

    paper += after_crease

    i += 1

    if pt1:
        print(paper.astype(int).sum())
        pt1 = False


print(paper.astype(int))
# copy and paste this into a text file, then find and replace 0's
# with spaces to see the answer

