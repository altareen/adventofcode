###
#-------------------------------------------------------------------------------
# sonarsweep.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2021
# Execution:    python3 sonarsweep.py
#
# This program counts the number of depth measurement increases.
#
##

# part one
def sonar(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        depths = [int(item.strip()) for item in entries]

        count = 0
        for i in range(1, len(depths)):
            if depths[i] > depths[i-1]:
                count += 1
        return count

# part two
def sweep(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        depths = [int(item.strip()) for item in entries]

        windows = []
        for i in range(len(depths)-2):
            windows.append(depths[i] + depths[i+1] + depths[i+2])

        count = 0
        for i in range(1, len(windows)):
            if windows[i] > windows[i-1]:
                count += 1
        return count

# display puzzle answers
def main():
    print(f'[sonar] sample result: {sonar("sampledata.txt")}')
    print(f'[sonar] entire result: {sonar("entiredata.txt")}')
    print(f'[sweep] sample result: {sweep("sampledata.txt")}')
    print(f'[sweep] entire result: {sweep("entiredata.txt")}')

if __name__ == '__main__':
    main()

