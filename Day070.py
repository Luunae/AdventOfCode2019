import IntClass
from itertools import permutations
file = "input_07.txt"
max = 0
maxlist = []

permlist = list(permutations(range(0, 5)))
print(permlist)

for i in range(len(permlist)):
    a = IntClass.Intcore(file, [permlist[i][0], 0])
    b = IntClass.Intcore(file, [permlist[i][1], a.output[0]])
    c = IntClass.Intcore(file, [permlist[i][2], b.output[0]])
    d = IntClass.Intcore(file, [permlist[i][3], c.output[0]])
    e = IntClass.Intcore(file, [permlist[i][4], d.output[0]])
    if e.output[0] > max:
        max = e.output[0]
        maxlist = permlist[i]

print("max signal: ", max)
print("phase settings: ", maxlist)