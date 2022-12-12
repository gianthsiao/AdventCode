import sys

file_name = sys.argv[1]


def create_set(num1, num2):
    return set([i for i in range(num1, num2+1)])

if __name__ == '__main__':
    count = 0
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            split_result = line.split(',')
            first = split_result[0]
            second = split_result[1]
            first_num_set = create_set(int(first.split('-')[0]),  int(first.split('-')[1]))
            second_num_set = create_set(int(second.split('-')[0]),  int(second.split('-')[1]))
            if (first_num_set - second_num_set) == set() or (second_num_set - first_num_set) == set():
                count += 1
    print(count)
