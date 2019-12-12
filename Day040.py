xvalue = 137683
yvalue = 596253
current = xvalue
totalnum = 0


def buddycompare(a):
    for b in range(5):
        if a[b] == a[b+1]:
            return 1


while current < yvalue:
    a = str(current)
    if "".join(sorted(a)) == a:
        if buddycompare(a) == 1:
            totalnum += 1
    current += 1
print("Total:")
print(totalnum)
