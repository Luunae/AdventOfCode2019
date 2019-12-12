import csv

file = "input_03.txt"
up = "U"
right = "R"
down = "D"
left = "L"


def compare():
    mindist = float('inf')
    for collision in collisionlist:
        a, b = collision.split(",")
        a, b = int(a), int(b)
        tempdist = abs(a) + abs(b)
        if tempdist < mindist and tempdist != 0:
            mindist = tempdist
    return mindist

def comparesteps():
    minsteps = float('inf')
    for collision in collisionlist:
        a = lred.index(collision)
        b = lblue.index(collision)
        tempsteps = a + b
        if tempsteps < minsteps and tempsteps != 0:
            minsteps = tempsteps
    return minsteps

def visitwirepath(inputdirections):
    loc_x = 0
    loc_y = 0
    coord_list = []
    for i in range(0, len(inputdirections)):
        if inputdirections[i][0] == up:
            j = int(inputdirections[i][1:])
            count = 0
            while count < j:
                loc_y += 1
                coord_list.append(str(loc_x) + "," + str(loc_y))
                count += 1
        elif inputdirections[i][0] == right:
            j = int(inputdirections[i][1:])
            count = 0
            while count < j:
                loc_x += 1
                coord_list.append(str(loc_x) + "," + str(loc_y))
                count += 1
        elif inputdirections[i][0] == down:
            j = int(inputdirections[i][1:])
            count = 0
            while count < j:
                loc_y -= 1
                coord_list.append(str(loc_x) + "," + str(loc_y))
                count += 1
        elif inputdirections[i][0] == left:
            j = int(inputdirections[i][1:])
            count = 0
            while count < j:
                loc_x -= 1
                coord_list.append(str(loc_x) + "," + str(loc_y))
                count += 1
        else:
            print("fuck")
    return coord_list


with open(file, 'r') as csvfile:
    allwires = list(csv.reader(csvfile, delimiter=","))
    red = list(allwires[0])
    blue = list(allwires[1])

lred = visitwirepath(red)
lblue = visitwirepath(blue)
print("lred, lblue")
print(lred)
print(lblue)

collisionlist = []
lblue_set = set(lblue)
collisionlist = [item for item in lred if item in lblue_set]
print("collisionlist, compare()")
print(collisionlist)
print(compare())
print("")


print(comparesteps() + 2)