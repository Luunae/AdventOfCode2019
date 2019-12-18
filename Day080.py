from typing import List

file = "input_08.txt"
width = 25  # x
height = 6  # y
maxz = float("inf")
new_line = True
newlayer = True
leastz = None
zeroes = 0
ones = 0
twos = 0

f = open(file, "r")
if f.mode == "r":
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

print(layers[0])

for i in range(0, len(layers)):  # Check each layer
    zeroes = 0
    for j in range(0, len(layers[i])):  # Check each row
        zeroes += layers[i][j].count("0")
    if zeroes < maxz:
        maxz = zeroes
        leastz = layers[i]
for i in range(0, len(leastz)):
    ones += leastz[i].count("1")
    twos += leastz[i].count("2")
ans = ones * twos
print(ans)