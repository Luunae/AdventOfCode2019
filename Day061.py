import csv
file = "input_06.txt"
with open(file, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=")")
    uom = list(reader)
llist = []
rlist = []
for i in range(0, len(uom)):
    llist.append(uom[i][0])
    rlist.append(uom[i][1])
sanorb = ["YOU"]
selforb = ["SAN"]
left = llist[rlist.index("YOU")]
while left != "COM":
    selforb.append(left)
    left = llist[rlist.index(left)]
left = llist[rlist.index("SAN")]
while left != "COM":
    sanorb.append(left)
    left = llist[rlist.index(left)]
selforb.reverse()
sanorb.reverse()
# print("self orbit: ")
# print(selforb)
# print("santa orbit: ")
# print(sanorb)
while selforb[1] == sanorb[1]:
    selforb.pop(0)
    sanorb.pop(0)
selforb.pop(len(selforb) - 1)
sanorb.pop(len(sanorb) - 1)
# print("number of hops: ", len(selforb) + len(sanorb))
# print("selforb:")
# print(len(selforb))
# print(selforb)
# print("sanorb:")
# print(len(sanorb))
# print(sanorb)
print("ans should hopefully be: ", (len(selforb) + len(sanorb)) - 2)
