###
#-------------------------------------------------------------------------------
# campcleanup.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 04, 2022
# Execution:    python3 campcleanup.py
#
# This program determines overlapping sections in cleaning assignment lists.
#
##

import re

# part one
def camp(data):
    with open(data, 'r') as f:
        entries = f.readlines()

    count = 0
    sections = [re.split('[,-]+', item.strip()) for item in entries]
    for row in sections:
        nums = [set(range(int(row[0]), int(row[1]) + 1)), set(range(int(row[2]), int(row[3]) + 1))]
        if nums[0].issuperset(nums[1]) or nums[0].issubset(nums[1]):
            count += 1
    return count

# part two
def cleanup(data):
    with open(data, 'r') as f:
        entries = f.readlines()
    
    count = 0
    sections = [re.split('[,-]+', item.strip()) for item in entries]
    for row in sections:
        nums = [set(range(int(row[0]), int(row[1]) + 1)), set(range(int(row[2]), int(row[3]) + 1))]
        if len(nums[0].intersection(nums[1])) > 0:
            count += 1
    return count

# display puzzle answers
def main():
    print(f'[camp] sample result: {camp("sampledata.txt")}')
    print(f'[camp] entire result: {camp("entiredata.txt")}')
    print(f'[cleanup] sample result: {cleanup("sampledata.txt")}')
    print(f'[cleanup] entire result: {cleanup("entiredata.txt")}')

if __name__ == '__main__':
    main()
