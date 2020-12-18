###
#-------------------------------------------------------------------------------
# day02positions.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 02, 2020
# Execution:    python3 day02positions.py day02input.txt
#
# This program determines the number of passwords that are valid.
#
##

from sys import argv, exit

def main():
    if len(argv) != 2:
        print("Usage: python3 day02positions.py day02input.txt")
        exit(1)
    
    quantity = 0
    
    with open(argv[1], "r") as fhand:
        for row in fhand:
            row = row.rstrip()
            entry = row.split()

            letter = entry[1][:1]
            password = entry[2]
            first = int(entry[0].split("-")[0])-1
            second = int(entry[0].split("-")[1])-1

            if (password[first] == letter and password[second] != letter) or (password[first] != letter and password[second] == letter):
                quantity += 1

    print(f"quantity: {quantity}")

if __name__ == "__main__":
    main()

