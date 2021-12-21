import numpy as np

input_file = open("day08_inputs.txt", 'r')
inputs = input_file.read().split('\n')

def count_unique():
    count = 0
    for line in inputs:
        pipe_idx = line.find("|")
        digits = line[pipe_idx+2:].split(" ")
        for dig in digits:
            if len(dig) == 2 or len(dig) == 3 or len(dig) == 4 or len(dig) == 7:
                # print(dig)
                count += 1
    return count


def x_in_y(x, y):
    for xi in x:
        if xi not in y:
            return False
    return True

def part2():
    output_sum = 0

    true_segments = {0:'abcefg', 1:'cf', 2:'acdeg', 3:'acdfg', 4:'bcdf', 5:'abdfg', 6:'abdefg', 7:'acf', 8:'abcdefg', 9:'abcdfg'}
    
    for line in inputs:

        potential_matches = {'a':[], 'b':[], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[]} # key = actual, val = list of potential wires
        num_to_chars = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:'', 0:''}

        patterns = sorted(line[:line.find("|")-1].split(" "), key=len)
        
        num_to_chars[1] = patterns[0]
        num_to_chars[7] = patterns[1]
        num_to_chars[4] = patterns[2]
        num_to_chars[8] = patterns[-1]
        

        # FIGURE OUT WHICH WIRES ARE WHICH OUTPUTS


        # narrow down c and f (using 1)
        for seg in true_segments[1]:
            for ch in num_to_chars[1]:
                potential_matches[seg].append(ch)

        # narrow down b and d (using 4 and 1)
        for seg in ['b', 'd']:
            for ch in num_to_chars[4]:
                if ch not in potential_matches['c']: # f also would've worked here
                    potential_matches[seg].append(ch)

        # SOLVE FOR a (using 7 and 1)
        # only difference between 1 and 7 is top segment a
        # so whichever one is in 7 but not 1 corresponds to a.
        for ch in num_to_chars[7]: # since we sorted by length, the second one with be len=3 aka #7
            if ch not in true_segments[1]:
                potential_matches['a'] = ch


        two_three_five = patterns[3:6]
        zero_six_nine = patterns[6:-1]

        for num in two_three_five:
            if x_in_y(potential_matches['c'], num):
                # 3 is the only one out of 2, 3, 5 that has both c and f in it.
                num_to_chars[3] = num # it's 3
                for ch in num:
                    if ch in potential_matches['d']:
                        potential_matches['d'] = ch
                        potential_matches['b'].remove(ch)
                        potential_matches['b'] = potential_matches['b'][0]
        
        two_three_five.remove(num_to_chars[3])
        two_five = two_three_five

        for num in zero_six_nine:
            if not x_in_y(potential_matches['d'], num):
                num_to_chars[0] = num
            if x_in_y(potential_matches['d'], num) and x_in_y(potential_matches['c'], num):
                # it's 9
                num_to_chars[9] = num
                for ch in 'abcdefg':
                    if ch not in num:
                        potential_matches['e'] = ch

        zero_six_nine.remove(num_to_chars[9])
        zero_six_nine.remove(num_to_chars[0])
        num_to_chars[6] = zero_six_nine[0]

        for ch in 'abcdefg':
            if ch not in num_to_chars[6]:
                potential_matches['c'] = ch
                potential_matches['f'].remove(ch)
                potential_matches['f'] = potential_matches['f'][0]

        for ch in 'abcdefg':
            if ch not in potential_matches.values():
                potential_matches['g'] = ch
                break

        for num in two_five:
            if potential_matches['b'] in num:
                num_to_chars[5] = num
            else:
                num_to_chars[2] = num



        # NOW DECODE OUTPUT

        for key, val in num_to_chars.items():
            num_to_chars[key] = ''.join(sorted(val))


        output_signals = line[line.find("|")+2:].split(" ")
        output_num = ''
        for sig in output_signals:
            sig = ''.join(sorted(sig))
            for key, val in num_to_chars.items():
                if sig == val:
                    output_num += str(key)
        
        output_sum += int(output_num)
        # print(output_num)

    return output_sum



print(count_unique())
print(part2())