###
#-------------------------------------------------------------------------------
# lanternfishbreeding.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 06, 2021
# Execution:    python3 lanternfishbreeding.py
#
# This program models the breeding patterns of a school of lanternfish.
#
##

# part one
class Lanternfish():
    def __init__(self, timer):
        self.timer = timer

    def update(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Lanternfish(8)
        return None

    def __str__(self):
        return str(self.timer)

class Ocean():
    def __init__(self, timers):
        self.lanternfish = [Lanternfish(timer) for timer in timers]

    def getLanternfish(self):
        return self.lanternfish

    def getTotalPop(self):
        return len(self.lanternfish)

    def update(self):
        school = self.lanternfish[:]
        for fish in school:
            result = fish.update()
            if result != None:
                self.lanternfish.append(result)

    def __str__(self):
        result = ''
        for item in self.lanternfish:
            result += str(item) + ','
        return result

def lanternfishobject(data):
    with open(data, 'r') as f:
        entry = f.readline()
        timers = [int(item) for item in entry.strip().split(',')]

        numTrials = 80
        atlantic = Ocean(timers)
        for trial in range(numTrials):
            atlantic.update()
        return atlantic.getTotalPop()

# alternate solution
def lanternfish(data):
    with open(data, 'r') as f:
        entry = f.readline()
        lanternfish = [int(item) for item in entry.strip().split(',')]

        numTrials = 80
        for trial in range(numTrials):
            offspring = []
            for i in range(len(lanternfish)):
                lanternfish[i] -= 1
                if lanternfish[i] < 0:
                    lanternfish[i] = 6
                    offspring.append(8)
            lanternfish.extend(offspring)
        return len(lanternfish)

# part two
def breeding(data):
    with open(data, 'r') as f:
        entry = f.readline()
        timers = [int(item) for item in entry.strip().split(',')]
        lanternfish = [0] * 9
        for timer in timers:
            lanternfish[timer] += 1

        numTrials = 256
        for trial in range(numTrials):
            base = lanternfish[0]
            for pos in range(1, 9):
                lanternfish[pos-1] = lanternfish[pos]
            lanternfish[6] += base
            lanternfish[8] = base
        return sum(lanternfish)

# display puzzle answers
def main():
    print(f'[lanternfish] sample result: {lanternfish("sampledata.txt")}')
    print(f'[lanternfish] entire result: {lanternfish("entiredata.txt")}')
    print(f'[breeding] sample result: {breeding("sampledata.txt")}')
    print(f'[breeding] entire result: {breeding("entiredata.txt")}')

if __name__ == '__main__':
    main()

