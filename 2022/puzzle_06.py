import sys

file_name = sys.argv[1]


def transfer_character_value(asci):
    if asci >= 97:
        return asci - 96
    elif 65 <= asci < 97:
        return asci - 38


if __name__ == '__main__':
    total = 0
    count_list = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            count_list.append(line)
            if len(count_list) == 3:
                inter = set(count_list[0]) & set(count_list[1]) & set(count_list[2])
                result = transfer_character_value(ord(list(inter)[0]))
                count_list = []
                total += result
    print(total)
