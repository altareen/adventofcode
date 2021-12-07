###
#-------------------------------------------------------------------------------
# hydrothermalventure.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 05, 2021
# Execution:    python3 hydrothermalventure.py
#
# This program determines how many times at least two lines overlap.
#
##

def display_diagram(graph):
    for row in graph:
        for num in row:
            if num == 0:
                print('. ', end='')
            else:
                print(str(num) + ' ', end='')
        print()

# part one
def hydrothermal(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        lines = [item.strip().split(' -> ') for item in entries]
        for i in range(len(lines)):
            lines[i][0] = lines[i][0].split(',')
            lines[i][1] = lines[i][1].split(',')
        for i in range(len(lines)):
            lines[i][0][0] = int(lines[i][0][0])
            lines[i][0][1] = int(lines[i][0][1])
            lines[i][1][0] = int(lines[i][1][0])
            lines[i][1][1] = int(lines[i][1][1])
        lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines))

        graph = [[0 for col in range(1000)] for row in range(1000)]
        for coord in lines:
            if coord[0][0] == coord[1][0]:
                for row in range(min(coord[0][1], coord[1][1]), max(coord[0][1], coord[1][1])+1):
                    graph[row][coord[0][0]] += 1
            elif coord[0][1] == coord[1][1]:
                for col in range(min(coord[0][0], coord[1][0]), max(coord[0][0],coord[1][0])+1):
                    graph[coord[0][1]][col] += 1
        return sum(1 for row in graph for num in row if num > 1)

# part two
def venture(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        lines = [item.strip().split(' -> ') for item in entries]
        for i in range(len(lines)):
            lines[i][0] = lines[i][0].split(',')
            lines[i][1] = lines[i][1].split(',')
        for i in range(len(lines)):
            lines[i][0][0] = int(lines[i][0][0])
            lines[i][0][1] = int(lines[i][0][1])
            lines[i][1][0] = int(lines[i][1][0])
            lines[i][1][1] = int(lines[i][1][1])

        graph = [[0 for col in range(1000)] for row in range(1000)]
        for coord in lines:
            if coord[0][0] == coord[1][0]:
                for row in range(min(coord[0][1], coord[1][1]), max(coord[0][1], coord[1][1])+1):
                    graph[row][coord[0][0]] += 1
            elif coord[0][1] == coord[1][1]:
                for col in range(min(coord[0][0], coord[1][0]), max(coord[0][0],coord[1][0])+1):
                    graph[coord[0][1]][col] += 1
            else:
                if coord[0][0] < coord[1][0] and coord[0][1] < coord[1][1]:
                    row = min(coord[0][1], coord[1][1])
                    for col in range(coord[0][0], coord[1][0]+1):
                        graph[row][col] += 1
                        row += 1
                elif coord[0][0] > coord[1][0] and coord[0][1] < coord[1][1]:
                    row = min(coord[0][1], coord[1][1])
                    for col in range(coord[0][0], coord[1][0]-1, -1):
                        graph[row][col] += 1
                        row += 1
                elif coord[0][0] < coord[1][0] and coord[0][1] > coord[1][1]:
                    row = max(coord[0][1], coord[1][1])
                    for col in range(coord[0][0], coord[1][0]+1):
                        graph[row][col] += 1
                        row -= 1
                elif coord[0][0] > coord[1][0] and coord[0][1] > coord[1][1]:
                    row = max(coord[0][1], coord[1][1])
                    for col in range(coord[0][0], coord[1][0]-1, -1):
                        graph[row][col] += 1
                        row -= 1
        return sum(1 for row in graph for num in row if num > 1)

# display puzzle answers
def main():
    print(f'[hydrothermal] sample result: {hydrothermal("sampledata.txt")}')
    print(f'[hydrothermal] entire result: {hydrothermal("entiredata.txt")}')
    print(f'[venture] sample result: {venture("sampledata.txt")}')
    print(f'[venture] entire result: {venture("entiredata.txt")}')

if __name__ == '__main__':
    main()

