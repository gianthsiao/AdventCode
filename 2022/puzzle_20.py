import sys

register_tracker = {}

def draw_pixle(crt_row, cycle):
    if sprite_list[cycle-1] == '#':
        crt_row.append('#')
    else:
        crt_row.append('.')
    if len(crt_row) == 40:
        print(crt_row)
        full_screen.extend(crt_row)
        crt_row = []
        cycle = 0
    return crt_row, cycle

def update_sprite_list(middle, sprite_list):
    first = middle - 1
    range_list = [x for x in range(first, first+3)]
    for i in range(40):
        if i not in range_list:
            sprite_list[i] = '.'
        else:
            sprite_list[i] = '#'
    return sprite_list

full_screen = []
if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        sprite_list = ['.' for i in range(40)]
        cycle = 1
        X = 1
        for i in range(0, 3):
            sprite_list[i] = '#'
        crt_row = []
        for line in f.readlines():
            line = line.strip('\n')
            element = line.split(' ')
            if len(element) == 1:
                crt_row, cycle = draw_pixle(crt_row, cycle)
                cycle += 1
            elif len(element) == 2:
                register = int(element[1])
                crt_row, cycle = draw_pixle(crt_row, cycle)
                cycle += 1
                X += register
                crt_row, cycle = draw_pixle(crt_row, cycle)
                cycle += 1
                sprite_list = update_sprite_list(X, sprite_list)
    str_list = ''
    for i in full_screen:
        if i == '#':
            str_list += '█'
        else:
            str_list += ' '
        if len(str_list) == 40:
            print(str_list)
            str_list = ''


