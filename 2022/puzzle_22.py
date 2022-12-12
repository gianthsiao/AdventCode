import sys, re

class Monkey(object):
    def __init__(self):
        self.item_list = []
        self.divide = 0
        self.true_situation = -1
        self.false_situation = -1
        self.cal = lambda x: x
        self.inspected_count = 0

    def add_item(self, item):
        self.item_list.append(item)

    def delete_item(self, num):
        self.item_list.remove(num)

    def show_item(self):
        print(self.item_list)
        print(self.divide)
        print(self.true_situation)
        print(self.false_situation)


    def create_worry_level_cal_func(self, operation):
        operator = operation[3]
        if operation[4] == 'old':
            self.cal = lambda x: x * x
        else:
            condition = int(operation[4])
            if operator == '+':
                self.cal = lambda x: x + condition
            elif operator == '*':
                self.cal = lambda x: x * condition

    def set_divide(self, num):
        self.divide = num

    def set_situation(self, situation, num):
        if situation == 'true':
            self.true_situation = num
        else:
            self.false_situation = num

monkey_dict = {}

if __name__ == '__main__':
    inspected_list = []
    file_name = sys.argv[1]
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            sentence = line.split(':')
            if len(sentence) >= 2:
                first = sentence[0]
                second = sentence[1]
                #print line
                if re.search('Monkey', first):
                    items = first.split(' ')
                    index = int(items[1])
                    monkey_dict[index] = Monkey()
                elif re.search('Starting items', first):
                    item_list = second.split(',')
                    for item in item_list:
                        monkey_dict[index].add_item(int(item))
                elif re.search('Operation', first):
                     operation = second.split(' ')[1:]
                     monkey_dict[index].create_worry_level_cal_func(operation)
                elif re.search('Test', first):
                    divide = int(second.split(' ')[3])
                    monkey_dict[index].set_divide(divide)
                elif re.search('true', first) or re.search('false', first):
                    element = first.split(' ')
                    all = len(element)
                    situation = element[all-1]
                    ans = int(second.split(' ')[4])
                    monkey_dict[index].set_situation(situation, ans)
    factors = []
    for index, monkey in enumerate(monkey_dict):
        factors.append(monkey_dict[index].divide)
    lcm = 1
    for f in factors:
        lcm *= f
    for i in range(10000):
        # print('round {0}'.format(i))
        for index, monkey in enumerate(monkey_dict):
            item_list = monkey_dict[index].item_list
            if len(item_list) > 0:
                remove_list = []
                for item in item_list:
                    new_level = int(monkey_dict[index].cal(item))
                    true_monkey = monkey_dict[index].true_situation
                    false_monkey = monkey_dict[index].false_situation
                    divide = monkey_dict[index].divide
                    """
                    91238 % 5 = 3
                    91238 % 7 = 0
                    91238 % (5*7) = 28
                    28 % 5 = 3
                    28 % 7 = 0
                    """
                    new_level = new_level % lcm
                    if new_level % divide == 0:
                        monkey_dict[true_monkey].add_item(new_level)
                    else:
                        monkey_dict[false_monkey].add_item(new_level)
                    remove_list.append(item)
                    monkey_dict[index].inspected_count += 1
                for remove in remove_list:
                    monkey_dict[index].delete_item(remove)
    for index, monkey in enumerate(monkey_dict):
        print(monkey_dict[index].item_list)
        inspected_list.append(monkey_dict[index].inspected_count)
    inspected_list = sorted(inspected_list, reverse=True)
    print('{0} * {1} = {2}'.format(inspected_list[0],
                                   inspected_list[1], inspected_list[0] * inspected_list[1]))