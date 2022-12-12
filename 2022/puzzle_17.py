import sys
import numpy as np

steps_matrix = []

file_name = sys.argv[1]
step_mapping = {
    'U': np.array([1, 0]),
    'D': np.array([-1, 0]),
    'L': np.array([0, -1]),
    'R': np.array([0, 1])
}

all_direction = [np.array([0, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0]),
                 np.array([1, 1]), np.array([1, -1]), np.array([-1, -1]), np.array([-1, 1])]
diag_move = [np.array([-1, -1]), np.array([1, -1]), np.array([1, 1]), np.array([-1, 1])]
ropes = np.full((2, 2), 0)
all_ropes = len(ropes)
tail_list = []


def _check_diag_direction(cur_node, pre_node):
    diag_move = [np.array([1, 1]), np.array([1, -1]), np.array([-1, -1]), np.array([-1, 1])]
    for move in diag_move:
        diag_move = cur_node + move
        for direction in all_direction:
            check_steps = diag_move + direction
            if np.array_equal(check_steps, pre_node):
                return diag_move


def _give_direction(diff):
    if diff[0] == 2:
        diff = diff - np.array([1, 0])
    elif diff[0] == -2:
        diff = diff + np.array([1, 0])
    elif diff[1] == 2:
        diff = diff - np.array([0, 1])
    else:
        diff = diff + np.array([0, 1])
    return diff


if __name__ == '__main__':
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            element = line.split(' ')
            direction = element[0]
            movement = step_mapping[element[0]]
            times = int(element[1])
            for _ in range(times):
                # print direction, _
                for index, cur_node in enumerate(ropes):
                    # first steps
                    # print movement
                    if index == 0:
                        # head
                        ropes[index] = cur_node + movement
                    else:
                        # rest nodes
                        adjust = False
                        pre_node = ropes[index - 1]
                        for dir in all_direction:
                            check_steps = cur_node + dir
                            if np.array_equal(check_steps, pre_node):
                                adjust = True
                        if not adjust:
                            # diagonally move
                            if pre_node[0] != cur_node[0] and pre_node[1] != cur_node[1]:
                                ropes[index] = _check_diag_direction(cur_node, pre_node)
                            else:
                                # regular move
                                # print pre_node, cur_node
                                diff = pre_node - cur_node
                                follow_movement = _give_direction(diff)
                                ropes[index] = cur_node + follow_movement
                        if index == all_ropes - 1:
                            # tail
                            if ropes[index].tolist() not in tail_list:
                                tail_list.append(ropes[index].tolist())
                # print ropes
        print(len(tail_list))
