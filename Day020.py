import csv
file = "testInput.txt"
a = 0
b = 0
pointer = 0
key = 19690720


def add(point):
    sum = av[point + 3]
    # print(sum)
    av[sum] = av[av[point + 1]] + av[av[point + 2]]
    # print("added")
    # print(av[point + 1])
    # print(av[point + 2])
    # print("to sumloc")


def mult(point):
    prod = av[point + 3]
    av[prod] = av[av[point + 1]] * av[av[point + 2]]


with open (file, 'r') as csvfile:
    adventreader = list(csv.reader(csvfile, delimiter=","))
    av = list(map(int, adventreader[0]))
    print(av)

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