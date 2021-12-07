###
#-------------------------------------------------------------------------------
# giantsquid.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 04, 2021
# Execution:    python3 giantsquid.py
#
# This program determines a winning bingo board, given a set of random numbers.
#
##

# part one
class Board():
    def __init__(self, board):
        self.board = board
        self.verify = [[False for col in range(5)] for row in range(5)]
        self.win = False

    def mark(self, num):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == num:
                    self.verify[row][col] = True

    def get_win(self):
        return self.win

    def check(self):
        for row in range(len(self.verify)):
            if all(self.verify[row]):
                total = 0
                for i in range(len(self.board)):
                    for j in range(len(self.board)):
                        if i != row and not self.verify[i][j]:
                            total += self.board[i][j]
                self.win = True
                return True, total
        flipped = [*zip(*self.verify)]
        nummed = [*zip(*self.board)]
        for row in range(len(flipped)):
            if all(flipped[row]):
                total = 0
                for i in range(len(self.board)):
                    for j in range(len(self.board)):
                        if j != row and not self.verify[i][j]:
                            total += self.board[i][j]
                self.win = True
                return True, total
        return False, 0

def determine_board(selections, boards):
    for draw in selections:
        for board in boards:
            board.mark(draw)
            result = board.check()
            if result[0]:
                return draw * result[1]

def giant(data):
    with open(data, 'r') as f:
        entries = f.readline()
        selections = [int(num) for num in entries.split(',')]
        boards = []

        for line in f:
            line = line.rstrip()
            if len(line) == 0:
                chunk = []
                continue
            line = [num for num in line.split(' ')]
            line = [int(num) for num in list(filter(lambda x: len(x) > 0, line))]
            chunk.append(line)
            if len(chunk) == 5:
                boards.append(Board(chunk))
    return determine_board(selections, boards)

# part two
def find_board(selections, boards):
    for draw in selections:
        for i in range(len(boards)):
            boards[i].mark(draw)
            result = boards[i].check()
            others = []
            for j in range(len(boards)):
                if i != j:
                    others.append(boards[j].get_win())
            if result[0] and all(others):
                return draw * result[1]

def squid(data):
    with open(data, 'r') as f:
        entries = f.readline()
        selections = [int(num) for num in entries.split(',')]
        boards = []

        for line in f:
            line = line.rstrip()
            if len(line) == 0:
                chunk = []
                continue
            line = [num for num in line.split(' ')]
            line = [int(num) for num in list(filter(lambda x: len(x) > 0, line))]
            chunk.append(line)
            if len(chunk) == 5:
                boards.append(Board(chunk))
    return find_board(selections, boards)

# display puzzle answers
def main():
    print(f'[giant] sample result: {giant("sampledata.txt")}')
    print(f'[giant] entire result: {giant("entiredata.txt")}')
    print(f'[squid] sample result: {squid("sampledata.txt")}')
    print(f'[squid] entire result: {squid("entiredata.txt")}')

if __name__ == '__main__':
    main()

