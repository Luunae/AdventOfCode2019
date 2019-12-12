filepath = 'input_01.txt'
fuel = 0
with open(filepath) as file:
    for count, line in enumerate(file):
        fuel += (int(line) // 3) - 2
    print(fuel)