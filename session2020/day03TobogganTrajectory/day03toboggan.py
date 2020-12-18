###
#-------------------------------------------------------------------------------
# day03toboggan.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 03, 2020
# Execution:    python3 day03toboggan.py day03input.txt
#
# This program determines the number of trees encountered in a traversal.
#
##

from sys import argv, exit

def main():
    if len(argv) != 2:
        print("Usage: python3 day03toboggan.py day03input.txt")
        exit(1)
    
    quantity = 0
    col = 3
    with open(argv[1], "r") as fhand:
        fhand.readline()
        for entry in fhand:
            entry = entry.rstrip()
            if entry[col] == "#":
                quantity += 1
            col = (col+3)%31
    
    print(f"quantity: {quantity}")

if __name__ == "__main__":
    main()

