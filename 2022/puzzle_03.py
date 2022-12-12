import sys
# A,X : Rock
# B,Y : Paper
# C,Z : Scissors

player_score_mapping = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
opponent_score_mapping = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3}
}


if __name__ == '__main__':
    file_name = sys.argv[1]
    total = 0
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            split = line.split(' ')
            round_score = opponent_score_mapping[split[0]][split[1]]
            movement_score = player_score_mapping[split[1]]
            result = round_score + movement_score
            # print split[0], split[1], result
            total += result
    print(total)