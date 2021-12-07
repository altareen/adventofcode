###
#-------------------------------------------------------------------------------
# binarydiagnostic.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 03, 2021
# Execution:    python3 binarydiagnostic.py
#
# This program decodes various ratings from a submarine's diagnostic report.
#
##

from collections import Counter

# part one
def binary(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        report = [item.strip() for item in entries]

        # determine gamma rate and epsilon rate
        gamma = ''
        epsilon = ''
        for i in range(len(report[0])):
            bits = []
            for num in report:
                bits.append(num[i])
            gamma += max(set(bits), key=bits.count)
            epsilon += min(bits[::-1], key=Counter(bits).get)
        return int(gamma, 2) * int(epsilon, 2)

# part two
def most_common(n, pos, elements):
    common = max(set(elements), key=elements.count)
    return n[pos] == common

from collections import Counter
def least_common(n, pos, elements):
    common = min(elements[::-1], key=Counter(elements).get)
    return n[pos] == common

def diagnostic(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        report = [item.strip() for item in entries]
        clone = report[:]

        # determine oxygen generator rating
        for i in range(len(report[0])):
            bits = []
            for num in report:
                bits.append(num[i])
            if bits.count('1') == bits.count('0'):
                result = list(filter(lambda n: n[i] == '1', report))
            else:
                result = list(filter(lambda n: most_common(n, i, bits), report))
            if len(result) == 1:
                oxygen = result[0]
                break
            report = result[:]

        # determine CO2 scrubber rating
        report = clone[:]
        for i in range(len(report[0])):
            bits = []
            for num in report:
                bits.append(num[i])
            if bits.count('1') == bits.count('0'):
                result = list(filter(lambda n: n[i] == '0', report))
            else:
                result = list(filter(lambda n: least_common(n, i, bits), report))
            if len(result) == 1:
                carbon = result[0]
                break
            report = result[:]

        # display result
        return int(oxygen, 2) * int(carbon, 2)

# display puzzle answers
def main():
    print(f'[binary] sample result: {binary("sampledata.txt")}')
    print(f'[binary] entire result: {binary("entiredata.txt")}')
    print(f'[diagnostic] sample result: {diagnostic("sampledata.txt")}')
    print(f'[diagnostic] entire result: {diagnostic("entiredata.txt")}')

if __name__ == '__main__':
    main()

