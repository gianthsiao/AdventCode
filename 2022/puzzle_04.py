import sys
# X : lose the game
# Y : Draw
# Z : Win the game

# A : Rock
# B : Paper
# C : Scissors

strategy_score_mapping = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

movement_score_mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
}
opponent_score_mapping = {
    'A': {3: 'A', 6: 'B', 0: 'C'},
    'B': {0: 'A', 3: 'B', 6: 'C'},
    'C': {6: 'A', 0: 'B', 3: 'C'}
}


if __name__ == '__main__':
    file_name = sys.argv[1]
    total = 0
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip('\n')
            split = line.split(' ')
            strategy_score = strategy_score_mapping[split[1]]
            player_movement = opponent_score_mapping[split[0]][strategy_score]
            movement_score = movement_score_mapping[player_movement]
            # print split[0], split[1], player_step, strategy_score, player_score
            total += strategy_score + movement_score
    print(total)