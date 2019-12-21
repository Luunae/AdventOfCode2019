testloc = [0, 0]
locs = [[0, 0, 0], [2, 2, 0], [1, 1, 0]]


def pathcheck(posa, posb, locs):
    posax, posay = posa
    posbx, posby = posb
    minx = min(posax, posbx)
    miny = min(posay, posby)
    maxx = max(posax, posbx)
    maxy = max(posay, posby)

    ydist = posay - posby
    xdist = posax - posbx
    dist = ((ydist**2) + (xdist**2))**0.5
    print("posa: ", posa)
    print("posb: ", posb)
    print("posax: ", posax)
    print("posay: ", posay)
    print("posbx: ", posbx)
    print("posby: ", posby)
    print("ydist: ", ydist)
    print("xdist: ", xdist)
    print("dist: ", dist)

    # y = m*x + b
    gradient = ydist / xdist

    print(gradient)
    elevation = posay - posax * gradient
    print(elevation)
    for loc in locs:
        if loc == posa or loc == posb:
            continue
        x, y = loc
        x_should = (y - elevation) / gradient
        if x == x_should and minx < x < maxx and miny < y < maxy:
            return False
    return True


for i in range(0, len(locs)):
    for j in range(0, len(locs)):
