import csv
file = "input_02.txt"
a = 0
b = 0
pointer = 0
key = 19690720

def add(point):
    sum = av[point + 3]
    #print(sum)
    av[sum] = av[av[point + 1]] + av[av[point + 2]]
    #print("added")
    #print(av[loc + 1])
    #print(av[loc + 2])
    #print("to sumloc")


def mult(point):
    prod = av[point + 3]
    av[prod] = av[av[point + 1]] * av[av[point + 2]]

with open (file, 'r') as csvfile:
    adventreader = list(csv.reader(csvfile, delimiter=","))
    av = list(map(int, adventreader[0]))
    print(av)
while av[0] != key:
    av = list(map(int, adventreader[0]))
    pointer = 0
    b += 1
    if b == 99:
        a += 1
        b = 0
    av[1] = a
    av[2] = b
    while av[pointer] != 99:
        if av[pointer] == 1:
            add(pointer)
            pointer += 4
        elif av[pointer] == 2:
            mult(pointer)
            pointer += 4
        elif pointer == 99:
            print(av[0])
        else:
            print("fuck")
print(av)
print(a)
print(b)
c = 100 * a + b
print(c)