###
#-------------------------------------------------------------------------------
# part01report.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2020
# Execution:    python3 part01report.py
#
# This program finds the two entries that sum to 2020, and multiplies them.
#
##

def report(data):
    with open(data, 'r') as fhand:
        entries = fhand.readlines()
    
    entries = [int(x) for x in entries]
    entries.sort()

    for i in range(len(entries)-1):
        for j in range(i+1, len(entries)):
            if entries[i] + entries[j] == 2020:
                return entries[i] * entries[j]

def main():
    print(f'result: {report("day01input.txt")}')

if __name__ == '__main__':
    main()

