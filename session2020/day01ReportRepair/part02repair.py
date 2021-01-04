###
#-------------------------------------------------------------------------------
# part02repair.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2020
# Execution:    python3 part02repair.py
#
# This program finds the three entries that sum to 2020, and multiplies them.
#
##

def repair(data):
    with open(data, 'r') as fhand:
        entries = fhand.readlines()
    
    entries = [int(x) for x in entries]
    entries.sort()

    for i in range(len(entries)-2):
        for j in range(i+1, len(entries)-1):
            for k in range(j+1, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]

def main():
    print(f'result: {repair("day01givendata.txt")}')

if __name__ == '__main__':
    main()

