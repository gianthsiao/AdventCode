import sys
tree_matrix = []
def calculate_visible_tree():
    tree_length = len(tree_matrix)
    visible_trees = tree_length * 4 - 4
    print(visible_trees)
    for index_r, row in enumerate(tree_matrix[1:tree_length-1]):
        for index_c, element in enumerate(row[1:tree_length-1]):
            visible_list = []
            correct_index_r = index_r+1
            correct_index_c = index_c+1
            visible_list.append(check_up(correct_index_r, correct_index_c))
            visible_list.append(check_down(correct_index_r, correct_index_c, tree_length))
            visible_list.append(check_left(correct_index_r, correct_index_c))
            visible_list.append(check_right(correct_index_r, correct_index_c, tree_length))
            # print visible_list
            if True in visible_list:
                visible_trees += 1
    print(visible_trees)


def check_up(index_r, index_c):
    # print index_r, index_c
    tree_height = tree_matrix[index_r][index_c]
    tree_list = []
    for i in range(index_r):
        tree_list.append(tree_matrix[i][index_c])
    # print tree_list
    tree_list.reverse()
    for _ in tree_list:
        if _ >= tree_height:
            return False
    return True


def check_down(index_r, index_c, tree_length):
    # print index_r, index_c
    tree_height = tree_matrix[index_r][index_c]
    tree_list = []
    for i in range(index_r+1, tree_length):
        tree_list.append(tree_matrix[i][index_c])
    # print tree_list
    for _ in tree_list:
        if _ >= tree_height:
            return False
    return True


def check_left(index_r, index_c):
    # print index_r, index_c
    tree_height = tree_matrix[index_r][index_c]
    tree_list = tree_matrix[index_r][0:index_c]
    # print tree_list
    tree_list.reverse()
    for _ in tree_list:
        if _ >= tree_height:
            return False
    return True


def check_right(index_r, index_c, tree_length):
    # print index_r, index_c
    tree_height = tree_matrix[index_r][index_c]
    tree_list = tree_matrix[index_r][index_c+1:tree_length]
    # print tree_list
    for _ in tree_list:
        if _ >= tree_height:
            return False
    return True


if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            row = [int(i) for i in line]
            tree_matrix.append(row)
    calculate_visible_tree()


