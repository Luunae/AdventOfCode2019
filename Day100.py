file = "test.txt"

def load(file):
    locs = []
    with open(file, 'r') as inputfile:
        y = 0
        for line in inputfile:
            x = 0
            for char in line.strip():
                if char == '#':
                    locs.append([x, y, 0])
                x += 1
            y += 1
    return locs


def pathcheck(posa, posb, locs):
    posax, posay, asteroids = posa
    posbx, posby, asteroids = posb
    minx = min(posax, posbx)
    miny = min(posay, posby)
    maxx = max(posax, posbx)
    maxy = max(posay, posby)
    ydist = posay - posby
    xdist = posax - posbx

    if xdist != 0:
        gradient = ydist / xdist
    else:
        gradient = float("inf")

    elevation = posay - posax * gradient
    for loc in locs:
        if loc == posa or loc == posb:
            continue
        x, y, asteroids = loc

        if not (minx <= x <= maxx and miny <= y <= maxy):
            continue

        if gradient == float("inf"):
            if posax == x:
                return False

        elif gradient != 0:
            x_should = (y - elevation) / gradient
            if x == x_should:
                return False
        else:
            if posay == y:
                return False
    return True


locs = load(file)
print(locs)
for i in range(0, len(locs)):
    for j in range(0, len(locs)):
        if i == j:
            continue
        if pathcheck(locs[i], locs[j], locs):
            locs[i][2] += 1

print("locs: ", locs)

maxct = 0
bestloc = None
for loc in locs:
    if loc[2] > maxct:
        maxct = loc[2]
        bestloc = loc
print("best loc: ", bestloc)
print("maxct: ", maxct)
