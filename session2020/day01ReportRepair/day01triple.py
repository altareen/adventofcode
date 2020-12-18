###
#-------------------------------------------------------------------------------
# day01triple.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2020
# Execution:    python3 day01triple.py day01input.txt
#
# This program finds the three entries that sum to 2020, and multiplies them.
#
##

from sys import argv, exit

def main():
    if len(argv) != 2:
        print('Usage: python3 day01triple.py day01input.txt')
        exit(1)

    with open(argv[1], 'r') as fhand:
        entries = fhand.readlines()
    
    entries = [int(x) for x in entries]
    entries.sort()

    for i in range(len(entries)-2):
        for j in range(i+1, len(entries)-1):
            for k in range(j+1, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    print(f'result: {entries[i] * entries[j] * entries[k]}')
                    break

if __name__ == '__main__':
    main()

