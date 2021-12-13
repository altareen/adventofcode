###
#-------------------------------------------------------------------------------
# dumbooctopus.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 11, 2021
# Execution:    python3 dumbooctopus.py
#
# This program determines the number of energy flashes after 100 time steps.
#
##

total = 0

def flash(row, col, chunk, energies, marked):
    global total
    if energies[row][col] > 9:
        energies[row][col] = 0
        marked[row][col] = True
        total += 1
        if row > 0 and not marked[row-1][col]:
            energies[row-1][col] += 1
            marked[row-1][col]
            flash(row-1, col, chunk, energies, marked)
        if row < len(energies) - 1 and not marked[row+1][col]:
            energies[row+1][col] += 1
            marked[row+1][col]
            flash(row+1, col, chunk, energies, marked)
        if col > 0 and not marked[row][col-1]:
            energies[row][col-1] += 1
            marked[row][col-1]
            flash(row, col-1, chunk, energies, marked)
        if col < len(chunk) - 1 and not marked[row][col+1]:
            energies[row][col+1] += 1
            marked[row][col+1]
            flash(row, col+1, chunk, energies, marked)
        if row > 0 and col > 0 and not marked[row-1][col-1]:
            energies[row-1][col-1] += 1
            marked[row-1][col-1]
            flash(row-1, col-1, chunk, energies, marked)
        if row > 0 and col < len(chunk) - 1 and not marked[row-1][col+1]:
            energies[row-1][col+1] += 1
            marked[row-1][col+1]
            flash(row-1, col+1, chunk, energies, marked)
        if row < len(energies) - 1 and col > 0 and not marked[row+1][col-1]:
            energies[row+1][col-1] += 1
            marked[row+1][col-1]
            flash(row+1, col-1, chunk, energies, marked)
        if row < len(energies) - 1 and col < len(chunk) - 1 and not marked[row+1][col+1]:
            energies[row+1][col+1] += 1
            marked[row+1][col+1]
            flash(row+1, col+1, chunk, energies, marked)

# part one
def dumbo(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        energies = [list(item.strip()) for item in entries]
        for row in energies:
            for i, num in enumerate(row):
                row[i] = int(num)
        
        numTrials = 100
        for trial in range(numTrials):
            # increase energy level by 1
            for row in energies:
                for i, num in enumerate(row):
                    row[i] += 1

            # check for flashes
            marked = [[False for col in range(len(energies[0]))] for row in range(len(energies))]
            for row, chunk in enumerate(energies):
                for col, num in enumerate(chunk):
                    flash(row, col, chunk, energies, marked)
        return total

# part two
def octopus(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        energies = [list(item.strip()) for item in entries]
        for row in energies:
            for i, num in enumerate(row):
                row[i] = int(num)
        
        numTrials = 250
        for trial in range(numTrials):
            # increase energy level by 1
            for row in energies:
                for i, num in enumerate(row):
                    row[i] += 1

            # check for flashes
            marked = [[False for col in range(len(energies[0]))] for row in range(len(energies))]
            for row, chunk in enumerate(energies):
                for col, num in enumerate(chunk):
                    flash(row, col, chunk, energies, marked)
        
            # check for synchronization
            if all(all(row) for row in marked):
                return trial + 1

# display puzzle answers
def main():
#    print(f'[dumbo] sample result: {dumbo("sampledata.txt")}')
    print(f'[dumbo] entire result: {dumbo("entiredata.txt")}')
#    print(f'[octopus] sample result: {octopus("sampledata.txt")}')
    print(f'[octopus] entire result: {octopus("entiredata.txt")}')

if __name__ == '__main__':
    main()

