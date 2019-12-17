import IntClass
from itertools import permutations
file = "input_07.txt"
maximum = 0
maxlist = []
permlist = list(permutations(range(5, 10)))

for i in range(len(permlist)):
    start = True
    a = IntClass.Intcore(file)
    b = IntClass.Intcore(file)
    c = IntClass.Intcore(file)
    d = IntClass.Intcore(file)
    e = IntClass.Intcore(file)
    while not e.stop:
        if start:
            a.go([permlist[i][0], 0])
            b.go([permlist[i][1], a.output.pop(0)])
            c.go([permlist[i][2], b.output.pop(0)])
            d.go([permlist[i][3], c.output.pop(0)])
            e.go([permlist[i][4], d.output.pop(0)])
            start = False
        else:
            a.go([e.output.pop(0)])
            b.go([a.output.pop(0)])
            c.go([b.output.pop(0)])
            d.go([c.output.pop(0)])
            e.go([d.output.pop(0)])

    if e.output[0] > maximum:
        maximum = e.output[0]
        maxlist = permlist[i]

print("max signal: ", maximum)
print("phase settings: ", maxlist)
