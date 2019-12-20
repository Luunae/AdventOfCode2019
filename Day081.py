from enum import IntEnum
# This is a shit image format. If I ever catch anyone using this for anything serious, I will murder them.

class Colour(IntEnum):
    BLACK = 0
    WHITE = 1
    TRANS = 2


def fill(compare):
    global row
    global pixfilled
    if int(compare) == Colour.BLACK:
        row += "▮"
        pixfilled = True
    elif int(compare) == Colour.WHITE:
        row += "▯"
        pixfilled = True
    return


file = "input_08.txt"
width = 25  # x
height = 6  # y
final = []
pixfilled = False

with open(file, "r") as f:
    raw = f.read()
img = str(raw)

layers = []
while len(img) > 0:
    layer = []
    for y in range(0, height):
        row = []

        for x in range(0, width):
            row.append(img[y * width + x])

        layer.append(row)
    layers.append(layer)
    img = img[height * width:]

for y in range(0, height):
    row = ""
    for x in range(0, width):
        pixfilled = False
        while not pixfilled:
            for k in range(len(layers)):
                fill(layers[k][y][x])
                if pixfilled:
                    break
                if k == len(layers) - 1:
                    row += "△"
                    pixfilled = True
    final.append(row)

for y in range(0, height):
    print(final[y])
