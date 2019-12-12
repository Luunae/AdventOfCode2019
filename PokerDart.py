# quick program to calculate when to reset cost of Poker Dart to 0
# assumes only one reset is available
for i in range(100):
    cost = 0
    mana = 100
    casts = 0
    if i == 0:
        mostcasts = 0
        clear = 1
        clearpoint = 1
        manareset = 0
    cleared = False
    while mana > 0 and cost < mana:
        mana -= cost
        casts += 1
        cost += 1
        if not cleared:
            if cost == clear:
                manareset = cost
                cost = 0
                cleared = True
    if casts > mostcasts:
        mostcasts = casts
        clearpoint = clear
        manaresetforrealthistime = manareset
    clear += 1
print("The most casts you can get with the given mana is:")
print(mostcasts)
print("The amount of casts you should reset at is:")
print(clearpoint)
print("the mana cost at this time is:")
print(manaresetforrealthistime)