###
#-------------------------------------------------------------------------------
# day04passports.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 04, 2020
# Execution:    python3 day04passports.py day04input.txt
#
# This program determines whether a given passport data is valid.
#
# Part 2 of AoC 2020.
#
##

from sys import argv, exit
import re

def main():
    if len(argv) != 2:
        print("Usage: python3 day04passports.py day04input.txt")
        exit(1)
    
    quantity = 0
    passports = []
    inspect = []
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    rules = [lambda x: len(x) == 4 and 1920 <= int(x) <= 2002, \
            lambda x: len(x) == 4 and 2010 <= int(x) <= 2020, \
            lambda x: len(x) == 4 and 2020 <= int(x)<= 2030, \
            lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or (x.endswith("in") and 59 <= int(x[:-2]) <= 76), \
            lambda x: True if re.search("#[0-9a-f]{6}", x) else False, \
            lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], \
            lambda x: True if re.search("^\d{9}$", x) else False]
    
    current = ""
    with open(argv[1], "r") as fhand:
        for line in fhand:
            current += " " + line.rstrip()
            if line == "\n":
                passports.append(current.strip())
                current = ""
        passports.append(current.strip())
    
    for entry in passports:
        relation = dict([x.split(":") for x in entry.split()])
        inspect.append(relation)
    
    passports = inspect[:]
    
    for entry in passports:
        verify = []
        for i in range(len(fields)):
            result = entry.get(fields[i], "")
            if result != "":
                verify.append(rules[i](result))
            else:
                verify.append(False)
    
        if all(verify):
            quantity += 1
    
    print(passports)
    print(f"Valid passports: {quantity}")

if __name__ == "__main__":
    main()

