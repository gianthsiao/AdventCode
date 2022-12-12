import sys

register_tracker = {}
if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        cycle = 0
        X = 1
        for line in f.readlines():
            line = line.strip('\n')
            element = line.split(' ')
            if len(element) == 1:
                if cycle != 0:
                    X = register_tracker[cycle]
                cycle += 1
                register_tracker[cycle] = X
            elif len(element) == 2:
                if cycle != 0:
                    X = register_tracker[cycle]
                register = int(element[1])
                cycle += 1
                register_tracker[cycle] = X
                X += register
                cycle += 1
                register_tracker[cycle] = X
        print(register_tracker)
    #print(len(register_tracker))
    sum_up = 0
    for index, item in enumerate(register_tracker):
        # print(item, register_tracker[item])
        if item == 20:
            sum_up += item*register_tracker[item-1]
        if item == 60:
            sum_up += item*register_tracker[item-1]
        if item == 100:
            sum_up += item*register_tracker[item-1]
        if item == 140:
            sum_up += item*register_tracker[item-1]
        if item == 180:
            sum_up += item*register_tracker[item-1]
        if item == 220:
            sum_up += item*register_tracker[item-1]
    print(sum_up)


