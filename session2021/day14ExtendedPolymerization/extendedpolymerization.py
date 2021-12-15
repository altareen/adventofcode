###
#-------------------------------------------------------------------------------
# extendedpolymerization.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 14, 2021
# Execution:    python3 extendedpolymerization.py
#
# This program generates a polymer based on some pair insertion rules.
#
##

# part one
def extended(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        polymer = entries[0].strip()
        insertions = dict([item.strip().split(' -> ') for item in entries[2:]])
        elements = set(insertions.values())

        numTrials = 10
        for trial in range(numTrials):
            clone = ''
            for i in range(len(polymer)-1):
                pair = polymer[i:i+2]
                first = polymer[i:i+1]
                mid = insertions[pair]
                clone += first + mid
            clone += polymer[-1]
            polymer = clone
        return max(clone.count(item) for item in elements) - min(clone.count(item) for item in elements)

# part two
def polymerization(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        polymer = entries[0].strip()
        insertions = dict([item.strip().split(' -> ') for item in entries[2:]])
        elements = set(insertions.values())
        element_tallies = {element: 0 for element in elements}
        spawn = {key: 0 for key in insertions.keys()}

        # initialize spawn dictionary with counts from polymer
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            spawn[pair] += 1

        # initialize elements_tally with counts from polymer
        for element in polymer:
            element_tallies[element] += 1

        numTrials = 40
        for trial in range(numTrials):
            sibling = spawn.copy()
            for pair, count in spawn.items():
                mid = insertions[pair]
                first = pair[0] + mid
                second = mid + pair[1]
                sibling[pair] -= count
                sibling[first] += count
                sibling[second] += count
                element_tallies[mid] += count
            spawn = sibling.copy()
        return max(element_tallies.values()) - min(element_tallies.values())

# display puzzle answers
def main():
    print(f'[extended] sample result: {extended("sampledata.txt")}')
    print(f'[extended] entire result: {extended("entiredata.txt")}')
    print(f'[polymerization] sample result: {polymerization("sampledata.txt")}')
    print(f'[polymerization] entire result: {polymerization("entiredata.txt")}')

if __name__ == '__main__':
    main()

