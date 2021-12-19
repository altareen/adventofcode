###
#-------------------------------------------------------------------------------
# chitoncavern.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 15, 2021
# Execution:    python3 chitoncavern.py
#
# This program determines a path through a cavern with the lowest total risk.
#
##

# part one: recursive solution, much too slow
def search(row, col, end_row, end_col, risks, total):
    if row != 0 or col != 0:
        total += risks[row][col]
    if row == end_row and col == end_col:
        return total
    if row == end_row:
        return search(row, col+1, end_row, end_col, risks, total)
    elif col == end_col:
        return search(row+1, col, end_row, end_col, risks, total)
    else:
        offset = 4
        first = search(row+1, col, min(row+offset, end_row), min(col+offset, end_col), risks, total)
        second = search(row, col+1, min(row+offset, end_row), min(col+offset, end_col), risks, total)
        if first < second:
            return search(row+1, col, end_row, end_col, risks, total)
        else:
            return search(row, col+1, end_row, end_col, risks, total)

def recursive(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        risks = [list(item.strip()) for item in entries]
        for chunk in risks:
            for col, num in enumerate(chunk):
                chunk[col] = int(num)
        row = 0
        col = 0
        end_row = len(risks) - 1
        end_col = len(risks[0]) - 1
        total = 0
        result = search(row, col, end_row, end_col, risks, total)
        return result

# part one
def chiton(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        risks = [list(item.strip()) for item in entries]
        for chunk in risks:
            for col, num in enumerate(chunk):
                chunk[col] = int(num)

        count = 0
        labels = [['0' for col, num in enumerate(chunk)] for row, chunk in enumerate(risks)]
        for row, chunk in enumerate(risks):
            for col, num in enumerate(chunk):
                labels[row][col] = str(count)
                count += 1
        nodes = [str(num) for num in list(range(count))]

        distances = dict()
        for row, chunk in enumerate(risks):
            for col, num in enumerate(chunk):
                neighbors = dict()
                if col < len(risks[0]) - 1:
                    neighbors[labels[row][col+1]] = risks[row][col+1]
                if row < len(risks) - 1:
                    neighbors[labels[row+1][col]] = risks[row+1][col]
                distances[labels[row][col]] = neighbors

        # Dijkstra's algorithm
        unvisited = {node: None for node in nodes}
        visited = dict()
        current = '0'
        currentDistance = 0
        unvisited[current] = currentDistance
        
        while True:
            for neighbor, distance in distances[current].items():
                if neighbor not in unvisited:
                    continue
                newDistance = currentDistance + distance
                if unvisited[neighbor] is None or unvisited[neighbor] > newDistance:
                    unvisited[neighbor] = newDistance
            visited[current] = currentDistance
            del unvisited[current]
            if not unvisited:
                break
            candidates = [node for node in unvisited.items() if node[1]]
            current, currentDistance = min(candidates, key=lambda x: x[1])
        return(visited[labels[-1][-1]])

# part two
def cavern(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        risks = [list(item.strip()) for item in entries]
        for chunk in risks:
            for col, num in enumerate(chunk):
                chunk[col] = int(num)

        zero = []
        one = []
        two = []
        three = []
        for i in range(len(risks)):
            for step in range(4):
                additions = []
                if step == 0:
                    current = risks[i][:]
                for num in current:
                    if num == 8:
                        additions.append(9)
                    else:
                        additions.append((num+1)%9)
                risks[i].extend(additions)
                if step == 0:
                    zero.append(additions)
                elif step == 1:
                    one.append(additions)
                elif step == 2:
                    two.append(additions)
                elif step == 3:
                    three.append(additions)
                current = additions[:]

        downward = []
        downward.extend(zero)
        downward.extend(one)
        downward.extend(two)
        downward.extend(three)
        for i in range(len(downward)):
            for num in range(4):
                additions = []
                if num == 0:
                    current = downward[i][:]
                for num in current:
                    if num == 8:
                        additions.append(9)
                    else:
                        additions.append((num+1)%9)
                downward[i].extend(additions)
                current = additions[:]
        risks.extend(downward)

        # solve the puzzle using code from part one
        count = 0
        labels = [['0' for col, num in enumerate(chunk)] for row, chunk in enumerate(risks)]
        for row, chunk in enumerate(risks):
            for col, num in enumerate(chunk):
                labels[row][col] = str(count)
                count += 1
        nodes = [str(num) for num in list(range(count))]

        distances = dict()
        for row, chunk in enumerate(risks):
            for col, num in enumerate(chunk):
                neighbors = dict()
                if col < len(risks[0]) - 1:
                    neighbors[labels[row][col+1]] = risks[row][col+1]
                if row < len(risks) - 1:
                    neighbors[labels[row+1][col]] = risks[row+1][col]
                distances[labels[row][col]] = neighbors

        # Dijkstra's algorithm
        unvisited = {node: None for node in nodes}
        visited = dict()
        current = '0'
        currentDistance = 0
        unvisited[current] = currentDistance
        
        while True:
            for neighbor, distance in distances[current].items():
                if neighbor not in unvisited:
                    continue
                newDistance = currentDistance + distance
                if unvisited[neighbor] is None or unvisited[neighbor] > newDistance:
                    unvisited[neighbor] = newDistance
            visited[current] = currentDistance
            del unvisited[current]
            if not unvisited:
                break
            candidates = [node for node in unvisited.items() if node[1]]
            current, currentDistance = min(candidates, key=lambda x: x[1])
        return(visited[labels[-1][-1]])

# display puzzle answers
def main():
    print(f'[recursive] sample result: {recursive("sampledata.txt")}')
    print(f'[chiton] sample result: {chiton("sampledata.txt")}')
    print(f'[chiton] entire result: {chiton("entiredata.txt")}')
    print(f'[cavern] sample result: {cavern("sampledata.txt")}')
#    print(f'[cavern] entire result: {cavern("entiredata.txt")}')

if __name__ == '__main__':
    main()

