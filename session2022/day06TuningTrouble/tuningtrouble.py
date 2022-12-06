###
#-------------------------------------------------------------------------------
# tuningtrouble.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 06, 2022
# Execution:    python3 tuningtrouble.py
#
# This program determines the position of a start-of-packet marker.
#
##

# part one
def tuning(data):
    with open(data, 'r') as f:
        entries = f.read()

    letters = entries.strip()
    for i in range(len(letters)):
        if len(set(letters[i-4:i])) == 4:
            return i

# part two
def trouble(data):
    with open(data, 'r') as f:
        entries = f.read()

    letters = entries.strip()
    for i in range(len(letters)):
        if len(set(letters[i-14:i])) == 14:
            return i

# display puzzle answers
def main():
    print(f'[tuning] sample result: {tuning("sampledata.txt")}')
    print(f'[tuning] entire result: {tuning("entiredata.txt")}')
    print(f'[trouble] sample result: {trouble("sampledata.txt")}')
    print(f'[trouble] entire result: {trouble("entiredata.txt")}')

if __name__ == '__main__':
    main()
