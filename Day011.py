filepath = 'input_01.txt'
fuel = 0
tempfuel = 1
flist = []

def getfuel(fuel):
    return (int(fuel) // 3) - 2

def getrecursivefuel(line):
    modulefuel = getfuel(line)
    tempfuel = modulefuel
    while tempfuel > 5:
        tempfuel = getfuel(tempfuel)
        modulefuel += tempfuel
    return modulefuel

with open(filepath) as file:
    for count, line in enumerate(file):
        fuel += getrecursivefuel(line)
    print(fuel)