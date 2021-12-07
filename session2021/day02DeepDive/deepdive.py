###
#-------------------------------------------------------------------------------
# deepdive.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 02, 2021
# Execution:    python3 deepdive.py
#
# This program determines the product of horizontal position by final depth.
#
##

# part one
def deep(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        navigation = [item.strip() for item in entries]

        horizontal = 0
        depth = 0
        for command in navigation:
            direction = command.split()[0]
            units = int(command.split()[1])
            if direction == 'forward':
                horizontal += units
            elif direction == 'down':
                depth += units
            elif direction == 'up':
                depth -= units
        return horizontal * depth

# part two
def dive(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        navigation = [item.strip() for item in entries]

        horizontal = 0
        depth = 0
        aim = 0
        for command in navigation:
            direction = command.split()[0]
            units = int(command.split()[1])
            if direction == 'forward':
                horizontal += units
                depth += aim * units
            elif direction == 'down':
                aim += units
            elif direction == 'up':
                aim -= units
        return horizontal * depth

# display puzzle answers
def main():
    print(f'[deep] sample result: {deep("sampledata.txt")}')
    print(f'[deep] entire result: {deep("entiredata.txt")}')
    print(f'[dive] sample result: {dive("sampledata.txt")}')
    print(f'[dive] entire result: {dive("entiredata.txt")}')

if __name__ == '__main__':
    main()

