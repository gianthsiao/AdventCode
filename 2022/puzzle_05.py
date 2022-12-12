import sys

file_name = sys.argv[1]


def transfer_character_value(asci):
    if asci >= 97:
        return asci - 96
    elif 65 <= asci < 97:
        return asci - 38


if __name__ == '__main__':
    total = 0
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            last = len(line)
            middle = last/2
            first_c = set(line[0:middle])
            second_c = set(line[middle:last])
            inter = first_c & second_c
            character = list(inter)[0]
            result = transfer_character_value(ord(character))
            total += result
    print(total)

