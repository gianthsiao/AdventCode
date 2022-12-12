import sys
"""
[J]             [F] [M]
[Z] [F]     [G] [Q] [F]
[G] [P]     [H] [Z] [S] [Q]
[V] [W] [Z] [P] [D] [G] [P]
[T] [D] [S] [Z] [N] [W] [B] [N]
[D] [M] [R] [J] [J] [P] [V] [P] [J]
[B] [R] [C] [T] [C] [V] [C] [B] [P]
[N] [S] [V] [R] [T] [N] [G] [Z] [W]
 1   2   3   4   5   6   7   8   9
"""
bucket_dict = {
    1: ['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],
    2: ['S', 'R', 'M', 'D', 'W', 'P', 'F'],
    3: ['V', 'C', 'R', 'S', 'Z'],
    4: ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],
    5: ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],
    6: ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],
    7: ['G', 'C', 'V', 'B', 'P', 'Q'],
    8: ['Z', 'B', 'P', 'N'],
    9: ['W', 'P', 'J']
}

file_name = sys.argv[1]

if __name__ == '__main__':
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            ops = line.split(' ')
            pop_num = int(ops[1])
            target = int(ops[3])
            dest = int(ops[5])
            while pop_num > 0:
                element = bucket_dict[target].pop()
                bucket_dict[dest].append(element)
                pop_num -= 1
    concatenate_str = ''
    for i in range(1, 10):
        last = len(bucket_dict[i]) - 1
        #print bucket_dict[i]
        concatenate_str += bucket_dict[i][last]
    print(concatenate_str)
