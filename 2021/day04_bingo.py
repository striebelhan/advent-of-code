import numpy as np

input_file = open("day04_inputs.txt", 'r') # open("day04_test_inputs.txt", 'r')
Lines = input_file.readlines()

calls = np.array(Lines[0].split(',')).astype(int)
boards = []



for i in range(2, len(Lines), 6):
    board = []
    for j in range(5):
        board_row = np.array(Lines[i+j].split(' '))
        board_row = board_row[board_row != ''].astype(int)
        board.append(board_row)
    
    boards.append(board)

boards = np.array(boards)



def part1(calls, boards):
    for call in calls:
        for board in boards:
            board[board == call] = -1
        
            if np.any(board.sum(axis=0) == -5) or np.any(board.sum(axis=1) == -5):
                # then we have a winner
                return board[board != -1].sum() * call


def part2(calls, boards):
    for call in calls:
        idx_to_delete = []
        for b in range(len(boards)):
            board = boards[b]
            board[board == call] = -1
        
            if np.any(board.sum(axis=0) == -5) or np.any(board.sum(axis=1) == -5):
                # then we have a winner
                
                # if it's the last winner, return it
                if len(boards) - len(idx_to_delete) == 1:
                    return board[board != -1].sum() * call

                # otherwise, remove it
                idx_to_delete.append(b)                    

        boards = np.delete(boards, idx_to_delete, axis=0)





print(part1(calls, np.copy(boards)))
print(part2(calls, np.copy(boards)))

