###
#-------------------------------------------------------------------------------
# part02philosophy.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 02, 2020
# Execution:    python3 part02philosophy.py
#
# This program determines the number of passwords that are valid.
#
##

def philosophy(data):
    quantity = 0
    with open(data, 'r') as fhand:
        for row in fhand:
            row = row.rstrip()
            entry = row.split()

            letter = entry[1][:1]
            password = entry[2]
            first = int(entry[0].split('-')[0])-1
            second = int(entry[0].split('-')[1])-1

            if (password[first] == letter and password[second] != letter) or (password[first] != letter and password[second] == letter):
                quantity += 1
    return quantity

def main():
    print(f'result: {philosophy("day02givendata.txt")}')

if __name__ == '__main__':
    main()

