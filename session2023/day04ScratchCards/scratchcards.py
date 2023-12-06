###
#-------------------------------------------------------------------------------
# scratchcards.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 04, 2023
# Execution:    python3 scratchcards.py
#
# This program determines the number of points from winning scratchcards.
#
##

# part one
def scratch(data, offset):
    with open(data, 'r') as f:
        entries = f.readlines()
    cards = [item.rstrip().split(' | ')[0] for item in entries]
    digits = [item[offset:].strip().split(' ') for item in cards]
    winners = [list(filter(lambda x: len(x) > 0, row)) for row in digits]
    for r, row in enumerate(winners):
        for c, col in enumerate(row):
            winners[r][c] = int(winners[r][c])

    cards = [item.rstrip().split(' | ')[1] for item in entries]
    digits = [item.split(' ') for item in cards]
    selections = [list(filter(lambda x: len(x) > 0, row)) for row in digits]
    for r, row in enumerate(selections):
        for c, col in enumerate(row):
            selections[r][c] = int(selections[r][c])

    total = 0
    for r, row in enumerate(winners):
        quantity = len(set(row).intersection(set(selections[r])))
        if quantity > 0:
            total += 2 ** (quantity - 1)
    return total

# part two
def cards(data, offset):
    with open(data, 'r') as f:
        entries = f.readlines()
    cards = [item.rstrip().split(' | ')[0] for item in entries]
    digits = [item[offset:].strip().split(' ') for item in cards]
    winners = [list(filter(lambda x: len(x) > 0, row)) for row in digits]
    for r, row in enumerate(winners):
        for c, col in enumerate(row):
            winners[r][c] = int(winners[r][c])

    cards = [item.rstrip().split(' | ')[1] for item in entries]
    digits = [item.split(' ') for item in cards]
    selections = [list(filter(lambda x: len(x) > 0, row)) for row in digits]
    for r, row in enumerate(selections):
        for c, col in enumerate(row):
            selections[r][c] = int(selections[r][c])

    copies = [1] * len(winners)
    for r, row in enumerate(winners):
        matches = len(set(row).intersection(set(selections[r])))
        repeats = copies[r]
        if matches > 0:
            for trial in range(repeats):
                spread = matches
                pos = r
                while spread > 0:
                    copies[pos+1] += 1
                    spread -= 1
                    pos += 1
    return sum(copies)

# display puzzle answers
def main():
    print(f'[scratch] sample result: {scratch("sampledata.txt", 7)}')
    print(f'[scratch] entire result: {scratch("entiredata.txt", 9)}')
    print(f'[cards] sample result: {cards("sampledata.txt", 7)}')
    print(f'[cards] entire result: {cards("entiredata.txt", 9)}')

if __name__ == '__main__':
    main()
