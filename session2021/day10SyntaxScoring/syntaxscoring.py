###
#-------------------------------------------------------------------------------
# syntaxscoring.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 10, 2021
# Execution:    python3 syntaxscoring.py
#
# This program calculates a score based on the number of incomplete brackets.
#
##

# part one
def syntax(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        navigation = [item.strip() for item in entries]

        symbols = {')':'(', ']':'[', '}':'{', '>':'<'}
        scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
        result = 0
        for line in navigation:
            stack = []
            for bracket in line:
                if bracket in '([{<':
                    stack.append(bracket)
                elif bracket in ')]}>':
                    last = stack.pop(-1)
                    if last != symbols[bracket]:
                        result += scores[bracket]
                        break
        return result                

# part two
def scoring(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        navigation = [item.strip() for item in entries]

        # run the code solution for part one to generate the corrupted list
        corrupted = []
        symbols = {')':'(', ']':'[', '}':'{', '>':'<'}
        for line in navigation:
            stack = []
            for bracket in line:
                if bracket in '([{<':
                    stack.append(bracket)
                elif bracket in ')]}>':
                    last = stack.pop(-1)
                    if last != symbols[bracket]:
                        corrupted.append(line)
                        break

        # generate the incomplete list from the corrupted list
        incomplete = list(filter(lambda x: x not in corrupted, navigation))
        
        # note that this dictionary's key-value pairs are reversed
        symbols = {'(':')', '[':']', '{':'}', '<':'>'}
        scores = {')': 1, ']': 2, '}': 3, '>': 4}
        openings = []
        closings = []
        points = []
        result = 0
        for line in incomplete:
            stack = []
            for bracket in line:
                if bracket in '([{<':
                    stack.append(bracket)
                elif bracket in ')]}>':
                    last = stack.pop(-1)
            openings.append(''.join(stack))
        
        for chunk in openings:
            endings = []
            for bracket in chunk:
                endings.insert(0, symbols[bracket])
            closings.append(''.join(endings))

        for chunk in closings:
            total = 0
            for bracket in chunk:
                total *= 5
                total += scores[bracket]
            points.append(total)

        points.sort()
        return points[len(points)//2]

# display puzzle answers
def main():
    print(f'[syntax] sample result: {syntax("sampledata.txt")}')
    print(f'[syntax] entire result: {syntax("entiredata.txt")}')
    print(f'[scoring] sample result: {scoring("sampledata.txt")}')
    print(f'[scoring] entire result: {scoring("entiredata.txt")}')

if __name__ == '__main__':
    main()

