import csv

file = "input_06.txt"
orbits = 0

with open(file, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=")")
    uom = list(reader)
llist = []
rlist = []
for i in range(0, len(uom)):
    llist.append(uom[i][0])
    rlist.append(uom[i][1])


for i in range(0, len(uom)):
    left = llist[i]
    while left != "COM":
        orbits += 1
        left = llist[rlist.index(left)]

print(orbits)