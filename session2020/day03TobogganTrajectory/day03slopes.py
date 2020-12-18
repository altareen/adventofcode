###
#-------------------------------------------------------------------------------
# day03slopes.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 03, 2020
# Execution:    python3 day03slopes.py day03input.txt
#
# This program determines the number of trees encountered in a traversal.
#
##

from sys import argv, exit
import functools

def main():
    if len(argv) != 2:
        print("Usage: python3 day03toboggan.py day03input.txt")
        exit(1)
    
    slopes = []
    for offset in [1, 3, 5, 7]:
        with open(argv[1], "r") as fhand:
            quantity = 0
            col = offset
            fhand.readline()
            for entry in fhand:
                entry = entry.rstrip()
                if entry[col] == "#":
                    quantity += 1
                col = (col+offset)%31
            slopes.append(quantity)

    offset = 1
    with open(argv[1], "r") as fhand:
        quantity = 0
        col = offset
        fhand.readline()
        fhand.readline()
        for entry in fhand:
            entry = entry.rstrip()
            if entry[col] == "#":
                quantity += 1
            col = (col+offset)%31
            fhand.readline()
        slopes.append(quantity)
    
    print(f"slopes: {slopes}")
    result = functools.reduce(lambda a,b: a*b, slopes)
    print(result)
    
if __name__ == "__main__":
    main()

