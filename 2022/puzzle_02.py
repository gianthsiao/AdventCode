import sys

file_name = sys.argv[1]
total_list = []
with open(file_name) as f:
    total = 0
    maximum = 0
    for line in f.readlines():
        line = line.strip('\n')
        if len(line) > 0:
            total += int(line)
        elif len(line) == 0:
            total_list.append(total)
            total = 0
    top3 = sorted(total_list, reverse=True)[0:3]
    print(sum(top3[0:3]))
