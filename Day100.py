file = "input_10.txt"

def load(file):
    asteroidlocations = []
    with open(file, 'r') as inputfile:
        y = 0
        for line in inputfile:
            x = 0
            for char in line.strip():
                if char == '#':
                    asteroidlocations.append([x, y, 0])
                x += 1
            y += 1
    return asteroidlocations


def noncollinearitycheck(firstasteroid, secondasteroid, asteroidlist):
    firstasteroidx, firstasteroidy, _numasteroids = firstasteroid
    secondasteroidx, secondasteroidy, _numasteroids = secondasteroid
    minx = min(firstasteroidx, secondasteroidx)  # range setup
    miny = min(firstasteroidy, secondasteroidy)
    maxx = max(firstasteroidx, secondasteroidx)
    maxy = max(firstasteroidy, secondasteroidy)
    ydist = firstasteroidy - secondasteroidy
    xdist = firstasteroidx - secondasteroidx

# if xdist (the distance between firstasteroidx and secondasteroidx is zero, the line is vertical.
# TODO: Better way to do that?
    if xdist != 0:
        gradient = ydist / xdist
    else:
        gradient = float("inf")

# This part checks every asteroid in the list to make sure it's not inbetween posa, posb.
# SUPER FUCKING INEFFICIENT.
# TODO: work on algorithm to minimize overhead.
    for compare in asteroidlist:
        if compare == firstasteroid or compare == secondasteroid:  # If current asteroid checking is either asteroids...
            continue                       # Skip. Should only happen twice per loop?
        comparex, comparey, _numasteroids = compare      # Split out info for use. EZ enough.

        # Range checking. Make sure asteroid isn't behind posa or posb. Should remove false LOS break positives.
        if not (minx <= comparex <= maxx and miny <= comparey <= maxy):
            continue

        firstthirdydist = firstasteroidy - comparey
        firstthirdxdist = firstasteroidx - comparex
        if firstthirdxdist != 0:
            firstthirdgradient = firstthirdydist / firstthirdxdist
        else:
            firstthirdgradient = float("inf")

        if firstthirdgradient == gradient:
            return False
    return True


locs = load(file)
print(locs)
for i in range(0, len(locs)):
    for j in range(0, len(locs)):
        if i == j:
            continue
        if noncollinearitycheck(locs[i], locs[j], locs):
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
