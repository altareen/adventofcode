###
#-------------------------------------------------------------------------------
# segmentsearch.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 08, 2021
# Execution:    python3 segmentsearch.py
#
# This program determines the digit value of a seven segment display.
#
##

# part one
def segment(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        codes = [item.strip().split(' | ')[1].split() for item in entries]
        return sum(1 for segments in codes for segment in segments if len(segment) in [2, 4, 3, 7])

# part two
def search(data):
    with open(data, 'r') as f:
        entries = f.readlines()
        codes = [item.strip().split(' | ')[0].split() for item in entries]
        displays = [item.strip().split(' | ')[1].split() for item in entries]

        result = 0
        for i, segments in enumerate(codes):
            encoding = {x: '' for x in range(9)}
            for segment in segments:
                if len(segment) == 2:
                    encoding[1] = segment
                elif len(segment) == 4:
                    encoding[4] = segment
                elif len(segment) == 3:
                    encoding[7] = segment
                elif len(segment) == 7:
                    encoding[8] = segment
            for segment in segments:
                if len(segment) == 5 and set(encoding[1]).issubset(set(segment)):
                    encoding[3] = segment
            for segment in segments:
                if len(segment) == 6 and set(encoding[4]).issubset(set(segment)):
                    encoding[9] = segment
            for segment in segments:
                if len(segment) == 6 and set(encoding[7]).issubset(set(segment)) and segment != encoding[9]:
                    encoding[0] = segment
            for segment in segments:
                if len(segment) == 6 and segment != encoding[0] and segment != encoding[9]:
                    encoding[6] = segment
            for segment in segments:
                if len(segment) == 5 and set(segment).issubset(set(encoding[9])) and segment != encoding[3]:
                    encoding[5] = segment
            for segment in segments:
                if len(segment) == 5 and segment != encoding[5] and segment != encoding[3]:
                    encoding[2] = segment

            for key, value in encoding.items():
                encoding[key] = ''.join(sorted(list(value)))
            decoding = {value: key for key, value in encoding.items()}
            readout = ''
            for segment in displays[i]:
                readout += str(decoding[''.join(sorted(list(segment)))])
            result += int(readout)
        return result

# display puzzle answers
def main():
    print(f'[segment] sample result: {segment("sampledata.txt")}')
    print(f'[segment] entire result: {segment("entiredata.txt")}')
    print(f'[search] sample result: {search("sampledata.txt")}')
    print(f'[search] entire result: {search("entiredata.txt")}')

if __name__ == '__main__':
    main()

