###
#-------------------------------------------------------------------------------
# rucksackreorganization.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 03, 2022
# Execution:    python3 rucksackreorganization.py
#
# This program determines the sum of the priorites of items in rucksacks.
#
##

import string

lowercase = dict(zip(string.ascii_lowercase, range(1, 27)))
uppercase = dict(zip(string.ascii_uppercase, range(27, 53)))
priorities = {**lowercase, **uppercase}

# part one
def rucksack(data):
    with open(data, 'r') as f:
        entries = f.readlines()
    
    compartments = []
    rucksacks = [item.strip() for item in entries]
    
    for item in rucksacks:
        partitions = [set(item[:len(item)//2]), set(item[len(item)//2:])]
        compartments.append(partitions)

    total = 0
    for item in compartments:
        total += priorities[item[0].intersection(item[1]).pop()]
    return total

# part two
def reorganization(data):
    with open(data, 'r') as f:
        entries = f.readlines()
    
    compartments = []
    rucksacks = [item.strip() for item in entries]

    for i in range(0, len(rucksacks) - 2, 3):
        partitions = [set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])]
        compartments.append(partitions)

    total = 0
    for item in compartments:
        total += priorities[item[0].intersection(item[1]).intersection(item[2]).pop()]
    return total

# display puzzle answers
def main():
    print(f'[rucksack] sample result: {rucksack("sampledata.txt")}')
    print(f'[rucksack] entire result: {rucksack("entiredata.txt")}')
    print(f'[reorganization] sample result: {reorganization("sampledata.txt")}')
    print(f'[reorganization] entire result: {reorganization("entiredata.txt")}')

if __name__ == '__main__':
    main()
