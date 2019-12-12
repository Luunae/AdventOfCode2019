xvalue = 137683
yvalue = 596253
current = xvalue
totalnum = 0


def buddycompare(a):
    for b in range(5):
        if a.count(a[b]) == 2:
            return True


while current < yvalue:
    a = str(current)
    if "".join(sorted(a)) == a:
        if buddycompare(a):
            totalnum += 1
    current += 1
print("Total:")
print(totalnum)
