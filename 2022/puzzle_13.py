import sys, re
import os.path

dirs = {'/'}
files = {}
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
        print(pwd)
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
    sum_dict = {}
    total = 0
    for path in files:
        size = files[path]
        element = path.split('/')
        os.path.dirname(pwd)
        path_counter = len(element)-1
        current_path = ''
        print(path)
        while path_counter - 1 >= 0:
            current_path = ''
            for i in range(1, path_counter):
                current_path += '/' + element[i]
            if current_path == '':
                current_path = '/'
            if current_path not in sum_dict:
                sum_dict[current_path] = size
            else:
                sum_dict[current_path] += size
            path_counter -= 1
    for count in sum_dict:
        if sum_dict[count] <= 100000:
            total += sum_dict[count]
    return total

if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            operatior = line.split(' ')
            operation_size = len(operatior)
            construct_path(operatior, operation_size)
    print(computer_size(files))

