###
#-------------------------------------------------------------------------------
# smokebasin.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 09, 2021
# Execution:    python3 smokebasin.py
#
# This program calculates the sum of all of the low points on a heatmap.
#
##

# part one
def smoke(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        heatmap = [list(item.strip()) for item in entries]
        for row in heatmap:
            for i, num in enumerate(row):
                row[i] = int(num)

        result = 0
        for row, chunk in enumerate(heatmap):
            for col, num in enumerate(chunk):
                neighbors = []
                if row > 0:
                    neighbors.append(heatmap[row-1][col])
                if row < len(heatmap) - 1:
                    neighbors.append(heatmap[row+1][col])
                if col > 0:
                    neighbors.append(heatmap[row][col-1])
                if col < len(chunk) - 1:
                    neighbors.append(heatmap[row][col+1])
                verify = list(map(lambda x: num < x, neighbors))
                if all(verify):
                    result += (1 + num)
        return result

# part two
def search(row, col, heatmap, marked):
    if marked[row][col] or heatmap[row][col] == 9:
        return
    marked[row][col] = True
    if row > 0:
        search(row-1, col, heatmap, marked)
    if row < len(heatmap) - 1:
        search(row+1, col, heatmap, marked)
    if col > 0:
        search(row, col-1, heatmap, marked)
    if col < len(heatmap[0]) - 1:
        search(row, col+1, heatmap, marked)

def basin(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        heatmap = [list(item.strip()) for item in entries]
        for row in heatmap:
            for i, num in enumerate(row):
                row[i] = int(num)

        # get (row, col) coordinates of all of the low points
        low_points = []
        for row, chunk in enumerate(heatmap):
            for col, num in enumerate(chunk):
                neighbors = []
                if row > 0:
                    neighbors.append(heatmap[row-1][col])
                if row < len(heatmap) - 1:
                    neighbors.append(heatmap[row+1][col])
                if col > 0:
                    neighbors.append(heatmap[row][col-1])
                if col < len(chunk) - 1:
                    neighbors.append(heatmap[row][col+1])
                verify = list(map(lambda x: num < x, neighbors))
                if all(verify):
                    low_points.append((row, col))

        # conduct a depth-first search, commencing from each low point
        basins = []
        for point in low_points:
            marked = [[False for col in range(len(heatmap[0]))] for row in range(len(heatmap))]
            search(point[0], point[1], heatmap, marked)
            total = sum(1 for row in marked for item in row if item)
            basins.append(total)
        basins.sort(reverse=True)
        return basins[0] * basins[1] * basins[2]

# display puzzle answers
def main():
    print(f'[smoke] sample result: {smoke("sampledata.txt")}')
    print(f'[smoke] entire result: {smoke("entiredata.txt")}')
    print(f'[basin] sample result: {basin("sampledata.txt")}')
    print(f'[basin] entire result: {basin("entiredata.txt")}')

if __name__ == '__main__':
    main()

