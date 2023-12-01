###
#-------------------------------------------------------------------------------
# trebuchetcalibration.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2023
# Execution:    python3 trebuchetcalibration.py
#
# This program determines the calibration values for a trebuchet.
#
##

# part one
def trebuchet(data):
    with open(data, 'r') as f:
        entries = f.readlines()
    measurements = [list(filter(lambda x: x.isdigit(), item.rstrip())) for item in entries]
    total = 0
    for element in measurements:
        total += int(element[0] + element[-1])
    return total

# part two
def calibration(data):
    with open(data, 'r') as f:
        entries = f.readlines()
    measurements = [item.rstrip() for item in entries]
    total = 0
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    backwards = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
    for element in measurements:
        current = ''
        flipped = element[::-1]

        # perform the algorithm on the element's front
        i = 0
        while i < len(element):
            chunk = element[i:]
            if chunk[0].isdigit():
                current += chunk[0]
                i = len(element)
            else:
                for num, digit in enumerate(digits):
                    if chunk.startswith(digit):
                        current += str(num + 1)
                        i = len(element)
            i += 1

        # perform the algorithm on the element's end
        j = 0
        while j < len(flipped):
            chunk = flipped[j:]
            if chunk[0].isdigit():
                current += chunk[0]
                j = len(flipped)
            else:
                for num, digit in enumerate(backwards):
                    if chunk.startswith(digit):
                        current += str(num + 1)
                        j = len(flipped)
            j += 1

        total += int(current)
    return total

# display puzzle answers
def main():
    print(f'[trebuchet] sample result: {trebuchet("sampledata.txt")}')
    print(f'[trebuchet] entire result: {trebuchet("entiredata.txt")}')
    print(f'[calibration] enhanced result: {calibration("enhanceddata.txt")}')
    print(f'[calibration] entire result: {calibration("entiredata.txt")}')

if __name__ == '__main__':
    main()
