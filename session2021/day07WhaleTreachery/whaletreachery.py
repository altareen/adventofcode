###
#-------------------------------------------------------------------------------
# whaletreachery.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 07, 2021
# Execution:    python3 whaletreachery.py
#
# This program determines the horizontal alignment position of a group of crabs.
#
##

# part one
def whale(data):
    with open(data, 'r') as f:
        entries = f.readline()
        positions = [int(num) for num in entries.strip().split(',')]
        largest = max(positions)

        min_fuel = 999999
        for align in range(largest):
            current = 0
            for num in positions:
                current += abs(num - align)
            if current < min_fuel:
                min_fuel = current
        return min_fuel

# part two
def treachery(data):
    with open(data, 'r') as f:
        entries = f.readline()
        positions = [int(num) for num in entries.strip().split(',')]
        largest = max(positions)

        min_fuel = 99999999
        for align in range(largest):
            current = 0
            for num in positions:
                unit = 0
                gap = abs(num - align)
                for step in range(1, gap+1):
                    unit += step
                current += unit
            if current < min_fuel:
                min_fuel = current
        return min_fuel

# display puzzle answers
def main():
    print(f'[whale] sample result: {whale("sampledata.txt")}')
    print(f'[whale] entire result: {whale("entiredata.txt")}')
    print(f'[treachery] sample result: {treachery("sampledata.txt")}')
    print(f'[treachery] entire result: {treachery("entiredata.txt")}')

if __name__ == '__main__':
    main()

