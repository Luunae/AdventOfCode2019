import csv
file = "test.txt"
lred = []
lblue = []
up = "U"
right = "R"
down = "D"
left = "L"

def start():
    global locx, locy
    locx = 0
    locy = 0

def compare():
    mindist = float('inf')
    for collision in collisionlist:
        a, b = collision.split(",")
        a, b = int(a), int(b)
        tempdist = abs(a) + abs(b)
        if tempdist < mindist and tempdist != 0:
            mindist = tempdist
    return mindist



start()
with open (file, 'r') as csvfile:
    allwires = list(csv.reader(csvfile, delimiter=","))
    red = list(allwires[0])
    blue = list(allwires[1])

for i in range(0,len(red)):
    if red[i][0] == up:
        j = int(red[i][1:])
        count = 0
        while (count < j):
            locy += 1
            lred.append(str(locx) +  "," + str(locy))
            count += 1
    elif red[i][0] == right:
        j = int(red[i][1:])
        count = 0
        while (count < j):
            locx += 1
            lred.append(str(locx) + "," + str(locy))
            count += 1
    elif red[i][0] == down:
        j = int(red[i][1:])
        count = 0
        while (count < j):
            locy -= 1
            lred.append(str(locx) + "," + str(locy))
            count += 1
    elif red[i][0] == left:
        j = int(red[i][1:])
        count = 0
        while (count < j):
            locx -= 1
            lred.append(str(locx) + "," + str(locy))
            count += 1
    else:
        print("fuck")

start()
for i in range(0,len(blue)):
    if blue[i][0] == up:
        j = int(blue[i][1:])
        count = 0
        while (count < j):
            locy += 1
            lblue.append(str(locx) +  "," + str(locy))
            count += 1
    elif blue[i][0] == right:
        j = int(blue[i][1:])
        count = 0
        while (count < j):
            locx += 1
            lblue.append(str(locx) + "," + str(locy))
            count += 1
    elif blue[i][0] == down:
        j = int(blue[i][1:])
        count = 0
        while (count < j):
            locy -= 1
            lblue.append(str(locx) + "," + str(locy))
            count += 1
    elif blue[i][0] == left:
        j = int(blue[i][1:])
        count = 0
        while (count < j):
            locx -= 1
            lblue.append(str(locx) + "," + str(locy))
            count += 1
    else:
        print("fuck")

print(lred)
print(lblue)

collisionlist = []
lblue_set = set(lblue)
collisionlist = [item for item in lred if item in lblue_set]

print(collisionlist)

print(compare())