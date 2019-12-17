import IntClass
from itertools import permutations
file = "test.txt"
maximum = 0
maxlist = []
permlist = list(permutations(range(5, 10)))



print(permlist)
print(permlist[0])
print(permlist[0][0])
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
            start = False
        else:
            a.go([permlist[i][0], e.output])
        b.go([permlist[i][1], a.output])
        c.go([permlist[i][2], b.output])
        d.go([permlist[i][3], c.output])
        e.go([permlist[i][4], d.output])
    if e.output > maximum:
        maximum = e.output
        maxlist = permlist[i]
    print(e.output)
    print(permlist[i])

print("max signal: ", maximum)
print("phase settings: ", maxlist)
