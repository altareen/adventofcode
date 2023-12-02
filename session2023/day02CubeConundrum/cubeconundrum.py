###
#-------------------------------------------------------------------------------
# cubeconundrum.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 02, 2023
# Execution:    python3 cubeconundrum.py
#
# This program determines the quantity of valid cube games.
#
##

import functools
import re

# part one
def cube(data):
    with open(data, 'r') as f:
        entries = f.readlines()    
    games = dict([item.rstrip().split(':') for item in entries])
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    total = 0

    for key, val in games.items():
        total += int(key.split()[-1])
        events = [item.strip().split() for item in re.split(r'[;,]', val)]
        for event in events:
            if int(event[0]) > cubes[event[-1]]:
                total -= int(key.split()[-1])
                break
    return total

# part two
def conundrum(data):
    with open(data, 'r') as f:
        entries = f.readlines()    
    games = dict([item.rstrip().split(':') for item in entries])
    powers = []

    for key, val in games.items():
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        events = [item.strip().split() for item in re.split(r'[;,]', val)]
        for event in events:
            if int(event[0]) > cubes[event[-1]]:
                cubes[event[-1]] = int(event[0])
        powers += [functools.reduce(lambda x, y: x * y, cubes.values())]
    return sum(powers)

# display puzzle answers
def main():
    print(f'[cube] sample result: {cube("sampledata.txt")}')
    print(f'[cube] entire result: {cube("entiredata.txt")}')
    print(f'[conundrum] sample result: {conundrum("sampledata.txt")}')
    print(f'[conundrum] entire result: {conundrum("entiredata.txt")}')

if __name__ == '__main__':
    main()
