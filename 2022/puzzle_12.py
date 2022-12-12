import sys


def check_marker(str_list):
    buffer_list = []
    for index, i in enumerate(str_list):
        if i not in buffer_list:
            buffer_list.append(i)
            if len(buffer_list) > 14:
                buffer_list.pop(0)
            print(buffer_list)
            if len(set(buffer_list)) == 14:
                return index
        else:
            buffer_list.pop(0)
            buffer_list.append(i)
            print(buffer_list)


if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            str_list = [i for i in line]
    print(check_marker(str_list) + 1)


