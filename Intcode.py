# before made intcode into a class
# probably broke something
# dab on the haters 2019
import csv
point = 0
opcodes = [1, 2, 3, 4, 99]
av = []
modes = ["position", "immediate"]


def load(file):
    with open(file) as csvfile:
        adventreader = csv.reader(csvfile, delimiter=",")
        av = list(map(int, adventreader[0]))
    return av


def go():
    while point < len(av):
        strpt = str(point)
        for i in len("%i" % point):

            if av[point] < 100:
                if av[point] in opcodes:
                    if av[point] == opcodes[0]:
                        add(point)
                    elif av[point] == opcodes[1]:
                        mult(point)
                    elif av[point] == opcodes[2]:
                        store[point]
                    elif av[point] == opcodes[3]:
                        pull[point]
                    elif av[point] == opcodes[4]:
                        print("point:")
                        print(point)


def get_digit(number, n):
    return number // 10 ** n % 10


def add(point):
    sum = av[point + 3]
    av[sum] = av[av[point + 1]] + av[av[point + 2]]
    point += 4


def mult(point):
    a = av[point + 3]
    av[a] = av[av[point + 1]] * av[av[point + 2]]
    point += 4


def store(point):
    storage = av[point + 1]
    av[av[storage]] = input("input:")


def pull(point):
    output = av[point + 1]
    print(output)