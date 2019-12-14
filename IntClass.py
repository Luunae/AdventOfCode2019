import csv
from enum import IntEnum


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


class Opcode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMPIFTRUE = 5
    JUMPIFFALSE = 6
    LESSTHAN = 7
    EQUAL = 8


class Intcore:
    def __init__(self, file, inputs=None):
        self.file = file
        self.i = 0
        self.opcodes = [1, 2, 3, 4, 5, 6, 7, 8, 99]
        self.av = []
        self.point = 0
        self.mode_a = Mode.POSITION
        self.mode_b = Mode.POSITION
        self.mode_c = Mode.POSITION
        self.modelist = [self.mode_a, self.mode_b, self.mode_c]
        self.zeromodes()
        self.output = []
        self.inputs = inputs
        self.inputsused = 0

        self.go()

    def go(self):
        self.load(self.file)
        while (self.av[self.point] % 100) != 99:
            self.getmode()
            opcode = self.av[self.point] % 100
            if opcode in self.opcodes:
                if opcode == Opcode.ADD:
                    self.add(self.point, self.modelist)
                elif opcode == Opcode.MULTIPLY:
                    self.mult(self.point, self.modelist)
                elif opcode == Opcode.INPUT:
                    self.store(self.point, self.modelist)
                elif opcode == Opcode.OUTPUT:
                    self.pull(self.point, self.modelist)
                elif opcode == Opcode.JUMPIFTRUE:
                    self.jumpiftrue(self.point, self.modelist, True)
                elif opcode == Opcode.JUMPIFFALSE:
                    self.jumpiftrue(self.point, self.modelist, False)
                elif opcode == Opcode.LESSTHAN:
                    self.lessthanequals(self.point, self.modelist, True)
                elif opcode == Opcode.EQUAL:
                    self.lessthanequals(self.point, self.modelist, False)
                else:
                    print("fuck")
                    break
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
        storage = self.av[point + 1]
        if self.inputs:
            self.av[storage] = self.inputs[self.inputsused]
            self.inputsused += 1
            self.point += 2
            return
        if modelist[0] == Mode.POSITION:
            self.av[storage] = int(input("input:"))
        else:
            raise Exception("Error, store value in wrong mode")
        self.point += 2

    def pull(self, point, modelist):
        if modelist[0] == Mode.POSITION:
            output = self.av[self.av[point + 1]]
        else:
            output = self.av[point + 1]
        print("\t\tOUT\t", output)
        self.output.append(output)
        self.point += 2

    def jumpiftrue(self, point, modelist, to_true):
        if modelist[0] == Mode.POSITION:
            check_value = self.av[self.av[point + 1]]
        else:
            check_value = self.av[point + 1]
        result = False
        if to_true:
            if check_value != 0:
                result = True
        else:
            if check_value == 0:
                result = True
        if result:
            if modelist[1] == Mode.POSITION:
                self.point = self.av[self.av[point + 2]]
            else:
                self.point = self.av[point + 2]
        else:
            self.point += 3

    def lessthanequals(self, point, modelist, lessthan):
        if modelist[0] == Mode.POSITION:
            firstnum = self.av[self.av[point + 1]]
        else:
            firstnum = self.av[point + 1]
        if modelist[1] == Mode.POSITION:
            secondnum = self.av[self.av[point + 2]]
        else:
            secondnum = self.av[point + 2]
        result = False
        if lessthan:
            if firstnum < secondnum:
                result = True
        else:
            if firstnum == secondnum:
                result = True
        if result:
            self.av[self.av[point + 3]] = 1
        else:
            self.av[self.av[point + 3]] = 0
        self.point += 4