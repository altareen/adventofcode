###
#-------------------------------------------------------------------------------
# day04credentials.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 04, 2020
# Execution:    python3 day04credentials.py day04input.txt
#
# This program determines whether a given passport data is valid.
#
# Part 1 of AoC 2020.
#
##

from sys import argv, exit

def main():
    if len(argv) != 2:
        print("Usage: python3 day04credentials.py day04input.txt")
        exit(1)
    
    quantity = 0
    passports = []
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    current = ""
    with open(argv[1], "r") as fhand:
        for line in fhand:
            current += " " + line.rstrip()
            if line == "\n":
                passports.append(current.strip())
                current = ""
        passports.append(current.strip())

    for entry in passports:
        verify = []
        for item in fields:
            if item in entry:
                verify.append(True)
            else:
                verify.append(False)
    
        if all(verify):
            quantity += 1
    
    print(passports)
    print(f"Valid passports: {quantity}")

if __name__ == "__main__":
    main()

