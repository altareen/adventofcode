###
#-------------------------------------------------------------------------------
# treehouse.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 08, 2022
# Execution:    python3 treehouse.py
#
# This program determines how many trees are visible from outside a grid.
#
##

# part one
def tree(data):
    with open(data, 'r') as f:
        entries = [[int(num) for num in list(line.strip())] for line in f]

    count = 2 * len(entries) + 2 * len(entries[0]) - 4
    for row in range(1, len(entries)-1):
        for col in range(1, len(entries[0])-1):
            height = entries[row][col]
            visible = False
            
            # upwards motion
            for up in range(row-1, -1, -1):
                if entries[up][col] >= height:
                    break
                elif entries[up][col] < height and up == 0:
                    visible = True
                    count += 1
            
            # downwards motion
            if not visible:
                for down in range(row+1, len(entries)):
                    if entries[down][col] >= height:
                        break
                    elif entries[down][col] < height and down == len(entries)-1:
                        visible = True
                        count += 1

            # leftwards motion
            if not visible:
                for left in range(col-1, -1, -1):
                    if entries[row][left] >= height:
                        break
                    elif entries[row][left] < height and left == 0:
                        visible = True
                        count += 1

            # rightwards motion
            if not visible:
                for right in range(col+1, len(entries[0])):
                    if entries[row][right] >= height:
                        break
                    elif entries[row][right] < height and right == len(entries[0])-1:
                        visible = True
                        count += 1
    return count

# part two
def house(data):
    with open(data, 'r') as f:
        entries = [[int(num) for num in list(line.strip())] for line in f]

    largest = 0
    for row in range(1, len(entries)-1):
        for col in range(1, len(entries[0])-1):
            height = entries[row][col]
            
            # upwards motion
            north = 0
            for up in range(row-1, -1, -1):
                north += 1
                if entries[up][col] >= height:
                    break

            # downwards motion
            south = 0
            for down in range(row+1, len(entries)):
                south += 1
                if entries[down][col] >= height:
                    break

            # leftwards motion
            west = 0
            for left in range(col-1, -1, -1):
                west += 1
                if entries[row][left] >= height:
                    break

            # rightwards motion
            east = 0
            for right in range(col+1, len(entries[0])):
                east += 1
                if entries[row][right] >= height:
                    break

            largest = max(north * south * west * east, largest)
    return largest

# display puzzle answers
def main():
    print(f'[tree] sample result: {tree("sampledata.txt")}')
    print(f'[tree] entire result: {tree("entiredata.txt")}')
    print(f'[house] sample result: {house("sampledata.txt")}')
    print(f'[house] entire result: {house("entiredata.txt")}')

if __name__ == '__main__':
    main()
