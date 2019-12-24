from math import atan2
file = "input_10.txt"

class Asteroid:
    def __init__(self, position, gradient):
        self.position = position
        self.gradient = gradient

    def __str__(self) -> str:
        return f"{self.position} {self.gradient}"


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

# This part checks every asteroid in the list to make sure it's not inbetween the two asteroids.
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


# def asteroiddestroy():

asteroidlist = load(file)
print(asteroidlist)
for i in range(0, len(asteroidlist)):
    for j in range(0, len(asteroidlist)):
        if i == j:
            continue
        if noncollinearitycheck(asteroidlist[i], asteroidlist[j], asteroidlist):
            asteroidlist[i][2] += 1

print("locs: ", asteroidlist)

maxct = 0
bestloc = None
baseloc = None
for loc in asteroidlist:
    if loc[2] > maxct:
        maxct = loc[2]
        bestloc = loc
        baseloc = asteroidlist.index(bestloc)
print("best loc: ", bestloc)
print("maxct: ", maxct)
print("index of asteroid: ", asteroidlist.index(bestloc))

asteroids = []
for asteroid in asteroidlist:
    if asteroid == asteroidlist[baseloc]:
        continue
    if noncollinearitycheck(asteroidlist[baseloc], asteroid, asteroidlist):
        ydist = asteroidlist[baseloc][1] - asteroid[1]
        xdist = asteroidlist[baseloc][0] - asteroid[0]
        if xdist != 0:
            gradient = ydist / xdist
        elif ydist < 0:
            gradient = float("inf")
        elif ydist > 0:
            gradient = float("-inf")
        else:
            print("fuck")
            break
        asteroids.append(Asteroid(asteroid, gradient))


xoffset = asteroidlist[248][0]
yoffset = asteroidlist[248][1]
asteroids.sort(key=lambda x: atan2(x.position[0] - xoffset, x.position[1] - yoffset))
print(asteroids)
print("done")
