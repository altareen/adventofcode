###
#-------------------------------------------------------------------------------
# caloriecounting.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 01, 2022
# Execution:    python3 caloriecounting.py
#
# This program determines the total calories that an Elf is carrying.
#
##

# part one
def calorie(data):
    with open(data, 'r') as f:
        entries = f.readlines()
    calories = [int(item.strip()) if item != '\n' else -1 for item in entries]
    clusters = []
    current = 0
    for num in calories:
        if num > 0:
            current += num
        else:
            clusters += [current]
            current = 0
    clusters += [current]
    return max(clusters), clusters

# part two
def counting(data):
    return sum(sorted(calorie(data)[1], reverse=True)[:3])

# display puzzle answers
def main():
    print(f'[calorie] sample result: {calorie("sampledata.txt")[0]}')
    print(f'[calorie] entire result: {calorie("entiredata.txt")[0]}')
    print(f'[counting] sample result: {counting("sampledata.txt")}')
    print(f'[counting] entire result: {counting("entiredata.txt")}')

if __name__ == '__main__':
    main()
