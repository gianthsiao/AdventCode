import sys, re
import os.path

dirs = {'/'}
files = {}
sum_dict = {}
def construct_path(operatior, operation_size):
    #print operatior, operation_size
    global pwd
    if operation_size == 3:
        if operatior[1] == 'cd' and operatior[2] == '/':
            pwd = '/'
        elif operatior[1] == 'cd' and operatior[2] != '..':
            pwd = os.path.join(pwd, operatior[2])
        else:
            pwd = os.path.dirname(pwd) or '/'
        # print pwd
    if operation_size == 2:
        #print operatior
        f_name = operatior[1]
        if operatior[0] == 'dir':
            dirs.add(os.path.join(pwd, f_name))
        elif re.search('[0-9]', operatior[0]):
            f_name = operatior[1]
            size = int(operatior[0])
            files[os.path.join(pwd, f_name)] = size


def computer_size(files):
    total = 0
    for path in files:
        size = files[path]
        element = path.split('/')
        os.path.dirname(pwd)
        path_counter = len(element)-1
        while path_counter - 1 >= 0:
            current_path = ''
            print(element)
            for i in range(1, path_counter):
                current_path += '/' + element[i]
            print(current_path)
            # print "cur %s " % current_path
            if current_path == '':
                current_path = '/'
            if current_path not in sum_dict:
                sum_dict[current_path] = size
            else:
                sum_dict[current_path] += size
            path_counter -= 1

def find_smallest_dict():
    full_size = 70000000
    min_require = 30000000
    current_left = full_size - sum_dict['/']
    diff = min_require - current_left
    small = diff
    for path in sum_dict:
        if sum_dict[path] - diff >= 0:
            diff_result = sum_dict[path] - diff
            if diff_result <= small:
                small = diff_result
    for path in sum_dict:
        if sum_dict[path] == small + diff:
            print(sum_dict[path])

if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            operatior = line.split(' ')
            operation_size = len(operatior)
            construct_path(operatior, operation_size)
    computer_size(files)
    find_smallest_dict()

