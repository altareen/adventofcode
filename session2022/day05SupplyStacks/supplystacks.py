###
#-------------------------------------------------------------------------------
# supplystacks.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 05, 2022
# Execution:    python3 supplystacks.py
#
# This program determines which crates are on the top of each stack.
#
##

# part one
def supply(data):
    with open(data, 'r') as f:
        entries = f.readlines()

    # sample data initialization
    # start = 5
    # crates = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    
    # entire data initialization
    start = 10
    cargo = ['SPHVFG', 'MZDVBFJG', 'NJLMG', 'PWDVZGN', 'BCRV', 'ZLWPMSRV', 'PHT', 'VZHCNSRQ', 'JQVPGLF']
    crates = [list(item) for item in cargo]
    
    procedure = [item.strip().split()[1:] for item in entries[start:]]

    for step in procedure:
        moves = int(step[0])
        src = int(step[2]) - 1
        dest = int(step[-1]) - 1

        for move in range(moves):
            crates[dest].insert(0, crates[src].pop(0))

    return ''.join([item[0] for item in crates])

# part two
def stacks(data):
    with open(data, 'r') as f:
        entries = f.readlines()

    # sample data initialization
    # start = 5
    # crates = [['N', 'Z'], ['D', 'C', 'M'], ['P']]

    # entire data initialization
    start = 10
    cargo = ['SPHVFG', 'MZDVBFJG', 'NJLMG', 'PWDVZGN', 'BCRV', 'ZLWPMSRV', 'PHT', 'VZHCNSRQ', 'JQVPGLF']
    crates = [list(item) for item in cargo]

    procedure = [item.strip().split()[1:] for item in entries[start:]]

    for step in procedure:
        moves = int(step[0])
        src = int(step[2]) - 1
        dest = int(step[-1]) - 1

        if moves > 1:
            chunk = crates[src][:moves]
            for move in range(moves):
                crates[src].pop(0)
            crates[dest] = chunk + crates[dest]
        else:
            crates[dest].insert(0, crates[src].pop(0))

    return ''.join([item[0] for item in crates])

# display puzzle answers
def main():
#    print(f'[supply] sample result: {supply("sampledata.txt")}')
    print(f'[supply] entire result: {supply("entiredata.txt")}')
#    print(f'[stacks] sample result: {stacks("sampledata.txt")}')
    print(f'[stacks] entire result: {stacks("entiredata.txt")}')

if __name__ == '__main__':
    main()
