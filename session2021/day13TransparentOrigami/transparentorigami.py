###
#-------------------------------------------------------------------------------
# transparentorigami.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 13, 2021
# Execution:    python3 transparentorigami.py
#
# This program determines the number of dots visible on a piece of folded paper.
#
##

# part one
def display(paper):
    for row in paper:
        for item in row:
            print(item + ' ', end='')
        print()

def transparent(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        post = entries.index('\n')
        points = [entries[i].strip().split(',') for i in range(post)]
        for row, chunk in enumerate(points):
            for col, num in enumerate(chunk):
                points[row][col] = int(points[row][col])
        folds = [entries[i].strip().split('=') for i in range(post+1, len(entries))]
        for row, chunk in enumerate(folds):
            folds[row][0] = folds[row][0][-1]
            folds[row][1] = int(folds[row][1])
        fold_way = folds[0][0]
        fold_amt = int(folds[0][1])

        rows = max(chunk[1] for chunk in points) + 1
        cols = max(chunk[0] for chunk in points) + 1
        paper = [['.' for col in range(cols)] for row in range(rows)]

        for coord in points:
            paper[coord[1]][coord[0]] = '#'

        if fold_way == 'x':
            for row in range(len(paper)):
                vert = fold_amt - 1
                for col in range(fold_amt+1, len(paper[0])):
                    if paper[row][vert] == '.':
                        paper[row][vert] = paper[row][col]
                    paper[row][col] = '.'
                    vert -= 1
        elif fold_way == 'y':
            horiz = fold_amt - 1
            for row in range(fold_amt+1, len(paper)):
                for col in range(len(paper[0])):
                    if paper[horiz][col] == '.':
                        paper[horiz][col] = paper[row][col]
                    paper[row][col] = '.'
                horiz -= 1

        return sum(1 for chunk in paper for item in chunk if item == '#')

# part two
def show(paper):
    for row in range(6):
        for col in range(39):
            print(paper[row][col] + ' ', end='')
        print()

def origami(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        post = entries.index('\n')
        points = [entries[i].strip().split(',') for i in range(post)]
        for row, chunk in enumerate(points):
            for col, num in enumerate(chunk):
                points[row][col] = int(points[row][col])
        folds = [entries[i].strip().split('=') for i in range(post+1, len(entries))]
        for row, chunk in enumerate(folds):
            folds[row][0] = folds[row][0][-1]
            folds[row][1] = int(folds[row][1])

        rows = max(chunk[1] for chunk in points) + 1
        cols = max(chunk[0] for chunk in points) + 1
        paper = [['.' for col in range(cols)] for row in range(rows)]

        for coord in points:
            paper[coord[1]][coord[0]] = '#'

        for fold in folds:
            fold_way = fold[0]
            fold_amt = fold[1]

            if fold_way == 'x':
                for row in range(len(paper)):
                    vert = fold_amt - 1
                    for col in range(fold_amt+1, len(paper[0])):
                        if paper[row][vert] == '.':
                            paper[row][vert] = paper[row][col]
                        paper[row][col] = '.'
                        vert -= 1
            elif fold_way == 'y':
                horiz = fold_amt - 1
                for row in range(fold_amt+1, len(paper)):
                    for col in range(len(paper[0])):
                        if paper[horiz][col] == '.':
                            paper[horiz][col] = paper[row][col]
                        paper[row][col] = '.'
                    horiz -= 1

        show(paper)
        return sum(1 for chunk in paper for item in chunk if item == '#')

# display puzzle answers
def main():
    print(f'[transparent] sample result: {transparent("sampledata.txt")}')
    print(f'[transparent] entire result: {transparent("entiredata.txt")}')
#    print(f'[origami] sample result: {origami("sampledata.txt")}')
    print(f'[origami] entire result: {origami("entiredata.txt")}')

if __name__ == '__main__':
    main()

