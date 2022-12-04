###
#-------------------------------------------------------------------------------
# rockpaperscissors.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 02, 2022
# Execution:    python3 rockpaperscissors.py
#
# This program determines the score of a Rock-Paper-Scissors game.
#
##

# part one
def rock(data):
    with open(data, 'r') as f:
        entries = f.readlines()

    tournament = [item.rstrip().split() for item in entries]
    elf = {'A': 0, 'B': 1, 'C': 2}
    player = {'X': 0, 'Y': 1, 'Z': 2}
    shapes = {'X': 1, 'Y': 2, 'Z': 3}

    score = 0
    for trial in tournament:
        outcome = (elf[trial[0]] - player[trial[1]]) % 3
        if outcome == 2:
            score += 6 + shapes[trial[1]]
        elif outcome == 1:
            score += shapes[trial[1]]
        else:
            score += 3 + shapes[trial[1]]
    return score

# part two
def paper(data):
    with open(data, 'r') as f:
        entries = f.readlines()

    tournament = [item.rstrip().split() for item in entries]
    elf = {'A': 0, 'B': 1, 'C': 2}
    player = {'X': 0, 'Y': 1, 'Z': 2}
    shapes = {'X': 1, 'Y': 2, 'Z': 3}
    correspond = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    reverse = {0: 'X', 1: 'Y', 2: 'Z'}

    score = 0
    for trial in tournament:
        current = 0
        if trial[1] == 'Z':
            score += 6 + shapes[reverse[(elf[trial[0]] - 2) % 3]]
        elif trial[1] == 'X':
            score += shapes[reverse[(elf[trial[0]] - 1) % 3]]
        elif trial[1] == 'Y':
            score += 3 + shapes[correspond[trial[0]]]
    return score

# display puzzle answers
def main():
    print(f'[rock] sample result: {rock("sampledata.txt")}')
    print(f'[rock] entire result: {rock("entiredata.txt")}')
    print(f'[paper] sample result: {paper("sampledata.txt")}')
    print(f'[paper] entire result: {paper("entiredata.txt")}')

if __name__ == '__main__':
    main()
