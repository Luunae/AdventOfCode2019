import csv
from enum import IntEnum


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Opcode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMPIFTRUE = 5
    JUMPIFFALSE = 6
    LESSTHAN = 7
    EQUAL = 8
    RBASEADJUST = 9


class GrowingList(list):  # Initial code from SO
    def __getitem__(self, index):
        if index >= len(self):
            return 0
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index >= len(self):
            self.extend([0]*(index + 1 - len(self)))
        list.__setitem__(self, index, value)


class Intcore:
    def __init__(self, file, askuserforinput=True):
        self.file = file
        self.i = 0
        self.opcodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
        self.av = []
        self.point = 0
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.rbase = 0
        self.mode_a = Mode.POSITION
        self.mode_b = Mode.POSITION
        self.mode_c = Mode.POSITION
        self.modelist = [self.mode_a, self.mode_b, self.mode_c]
        self.zeromodes()
        self.outputs = []
        self.stop = False
        self.load(self.file)
        self.needsinput = False
        self.askuserforinput = askuserforinput
        self.inputs = None

    def go(self, inputs=None):
        self.stop = False
        self.inputs = inputs
        self.needsinput = False
        while (self.av[self.point] % 100) != 99:
            if self.needsinput:
                return
            self.getmode()
            self.getvals()
            opcode = self.av[self.point] % 100
            if opcode in self.opcodes:
                if opcode == Opcode.ADD:            # Day 2
                    self.add(self.p1, self.p2, self.p3)
                elif opcode == Opcode.MULTIPLY:     # Day 2
                    self.mult(self.p1, self.p2, self.p3)
                elif opcode == Opcode.INPUT:        # Day 5
                    self.store(self.p1)
                elif opcode == Opcode.OUTPUT:       # Day 5
                    self.pull(self.p1)
                elif opcode == Opcode.JUMPIFTRUE:   # Day 5
                    self.jumpiftrue(self.p1, self.p2, True)
                elif opcode == Opcode.JUMPIFFALSE:  # Day 5
                    self.jumpiftrue(self.p1, self.p2, False)
                elif opcode == Opcode.LESSTHAN:     # Day 5
                    self.lessthanequals(self.p1, self.p2, self.p3, True)
                elif opcode == Opcode.EQUAL:        # Day 5
                    self.lessthanequals(self.p1, self.p2, self.p3, False)
                elif opcode == Opcode.RBASEADJUST:  # Day 9
                    self.rbaseadjust(self.p1)
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
        self.stop = True

    def load(self, a):
        with open(a, 'r') as csvfile:
            adventreader = list(csv.reader(csvfile, delimiter=","))
            self.av = GrowingList(list(map(int, adventreader[0])))

    def getmode(self):
        if self.av[self.point] // 100 % 10 == 0:
            self.mode_a = Mode.POSITION
        elif self.av[self.point] // 100 % 10 == 1:
            self.mode_a = Mode.IMMEDIATE
        else:
            self.mode_a = Mode.RELATIVE
        if self.av[self.point] // 1000 % 10 == 0:
            self.mode_b = Mode.POSITION
        elif self.av[self.point] // 1000 % 10 == 1:
            self.mode_b = Mode.IMMEDIATE
        else:
            self.mode_b = Mode.RELATIVE
        if self.av[self.point] // 10000 % 10 == 0:
            self.mode_c = Mode.POSITION
        elif self.av[self.point] // 10000 % 10 == 1:
            self.mode_c = Mode.IMMEDIATE
        else:
            self.mode_c = Mode.RELATIVE
        self.modelist = [self.mode_a, self.mode_b, self.mode_c]

    def getvals(self):
        if self.mode_a == Mode.POSITION:
            self.p1 = self.av[self.point + 1]
        elif self.mode_a == Mode.IMMEDIATE:
            self.p1 = self.point + 1
        else:
            self.p1 = self.av[self.point + 1] + self.rbase

        if self.point + 2 >= len(self.av):
            self.p3 = None
        if self.mode_b == Mode.POSITION:
            self.p2 = self.av[self.point + 2]
        elif self.mode_b == Mode.IMMEDIATE:
            self.p2 = self.point + 2
        else:
            self.p2 = self.av[self.point + 2] + self.rbase

        if self.point + 3 >= len(self.av):
            self.p3 = None
        elif self.mode_c == Mode.POSITION:
            self.p3 = self.av[self.point + 3]
        elif self.mode_c == Mode.IMMEDIATE:
            self.p3 = self.point + 3
        else:
            self.p3 = self.av[self.point + 3] + self.rbase

    def zeromodes(self):
        self.mode_a = Mode.POSITION
        self.mode_b = Mode.POSITION
        self.mode_c = Mode.POSITION
        self.modelist = [self.mode_a, self.mode_b, self.mode_c]

    def add(self, p1, p2, p3):
        # if modelist[0] == Mode.POSITION:
        #     a = self.av[self.av[point + 1]]
        # else:
        #     a = self.av[point + 1]
        # if modelist[1] == Mode.POSITION:
        #     b = self.av[self.av[point + 2]]
        # else:
        #     b = self.av[point + 2]
        # if modelist[2] == Mode.POSITION:
        #     c = self.av[point + 3]
        # else:
        #     raise Exception("Error, add store value in wrong mode")
        self.av[p3] = self.av[p1] + self.av[p2]
        self.point += 4

    def mult(self, p1, p2, p3):
        # if modelist[0] == Mode.POSITION:
        #     a = self.av[self.av[point + 1]]
        # else:
        #     a = self.av[point + 1]
        # if modelist[1] == Mode.POSITION:
        #     b = self.av[self.av[point + 2]]
        # else:
        #     b = self.av[point + 2]
        # if modelist[2] == Mode.POSITION:
        #     c = self.av[point + 3]
        # else:
        #     raise Exception("Error, mult store value in wrong mode")
        self.av[p3] = self.av[p1] * self.av[p2]
        self.point += 4

    def store(self, p1):
        if self.askuserforinput:
            self.av[p1] = int(input("Input:"))
            self.point += 2
        elif self.inputs:
            self.av[p1] = self.inputs.pop(0)
            self.point += 2
        else:
            self.needsinput = True

    def pull(self, p1):
        # if modelist[0] == Mode.POSITION:
        #     output = self.av[self.av[point + 1]]
        # else:
        #     output = self.av[point + 1]
        self.outputs.append(self.av[p1])
        self.point += 2

    def jumpiftrue(self, p1, p2, to_true):
        # if modelist[0] == Mode.POSITION:
        #     check_value = self.av[self.av[point + 1]]
        # else:
        #     check_value = self.av[point + 1]
        check_value = self.av[p1]
        result = False
        if to_true:
            if check_value != 0:
                result = True
        else:
            if check_value == 0:
                result = True
        if result:
            # if modelist[1] == Mode.POSITION:
            #     self.point = self.av[self.av[point + 2]]
            # else:
            #     self.point = self.av[point + 2]
            self.point = self.av[p2]
        else:
            self.point += 3

    def lessthanequals(self, p1, p2, p3, lessthan):
        # if modelist[0] == Mode.POSITION:
        #     firstnum = self.av[self.av[point + 1]]
        # else:
        #     firstnum = self.av[point + 1]
        # if modelist[1] == Mode.POSITION:
        #     secondnum = self.av[self.av[point + 2]]
        # else:
        #     secondnum = self.av[point + 2]
        result = False
        if lessthan:
            if self.av[p1] < self.av[p2]:
                result = True
        else:
            if self.av[p1] == self.av[p2]:
                result = True
        if result:
        #     self.av[self.av[point + 3]] = 1
        # else:
        #     self.av[self.av[point + 3]] = 0
            self.av[p3] = 1
        else:
            self.av[p3] = 0
        self.point += 4

    def rbaseadjust(self, p1):
        self.rbase += self.av[p1]
        self.point += 2
