import csv
from enum import Enum


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Intcore:
    def __init__(self, file):
        self.file = file
        self.i = 0
        self.opcodes = [1, 2, 3, 4, 99]
        self.av = []
        self.point = 0
        self.mode_a = Mode.POSITION
        self.mode_b = Mode.POSITION
        self.mode_c = Mode.POSITION
        self.modelist = [self.mode_a, self.mode_b, self.mode_c]
        self.zeromodes()
        self.go()

    def go(self):
        self.load(self.file)
        while (self.av[self.point] % 100) != 99:
            self.getmode()
            opcode = self.av[self.point] % 100
            if opcode in self.opcodes:
                if opcode == self.opcodes[0]:
                    self.add(self.point, self.modelist)
                elif opcode == self.opcodes[1]:
                    self.mult(self.point, self.modelist)
                elif opcode == self.opcodes[2]:
                    self.store(self.point, self.modelist)
                else:
                    self.pull(self.point, self.modelist)
            else:
                print("fuck")
                print(self.av)
                print(self.point)
                print(opcode)
                print("the number at point is")
                print(self.av[self.point])
                break
            self.i += 1

    def load(self, a):
        with open(a, 'r') as csvfile:
            adventreader = list(csv.reader(csvfile, delimiter=","))
            self.av = list(map(int, adventreader[0]))

    def getmode(self):
        if self.av[self.point] // 100 % 10 == 0:
            self.mode_a = Mode.POSITION
        else:
            self.mode_a = Mode.IMMEDIATE
        if self.av[self.point] // 1000 % 10 == 0:
            self.mode_b = Mode.POSITION
        else:
            self.mode_b = Mode.IMMEDIATE
        if self.av[self.point] // 10000 % 10 == 0:
            self.mode_c = Mode.POSITION
        else:
            self.mode_c = Mode.IMMEDIATE
        self.modelist = [self.mode_a, self.mode_b, self.mode_c]

    def zeromodes(self):
        self.mode_a = Mode.POSITION
        self.mode_b = Mode.POSITION
        self.mode_c = Mode.POSITION
        self.modelist = [self.mode_a, self.mode_b, self.mode_c]

    def add(self, point, modelist):
        if modelist[0] == Mode.POSITION:
            a = self.av[self.av[point + 1]]
        else:
            a = self.av[point + 1]
        if modelist[1] == Mode.POSITION:
            b = self.av[self.av[point + 2]]
        else:
            b = self.av[point + 2]
        if modelist[2] == Mode.POSITION:
            c = self.av[point + 3]
        else:
            raise Exception("Error, add store value in wrong mode")
        self.av[c] = a + b
        self.point += 4

    def mult(self, point, modelist):
        if modelist[0] == Mode.POSITION:
            a = self.av[self.av[point + 1]]
        else:
            a = self.av[point + 1]
        if modelist[1] == Mode.POSITION:
            b = self.av[self.av[point + 2]]
        else:
            b = self.av[point + 2]
        if modelist[2] == Mode.POSITION:
            c = self.av[point + 3]
        else:
            raise Exception("Error, mult store value in wrong mode")
        self.av[c] = a * b
        self.point += 4

    def store(self, point, modelist):
        if modelist[0] == Mode.POSITION:
            storage = self.av[point + 1]
            self.av[storage] = int(input("input:"))

        else:
            storage = self.av[point + 1]
            self.av[self.av[storage]] = int(input("input:"))
        self.point += 2

    def pull(self, point, modelist):
        if modelist[0] == Mode.POSITION:
            output = self.av[self.av[point + 1]]
        else:
            output = self.av[point + 1]
        print("\t\tOUT\t", output)
        self.point += 2
