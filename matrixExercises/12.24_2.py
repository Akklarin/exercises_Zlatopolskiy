mas = []

for i in range(6):
    mas.append([])
    for j in range(6):
        mas[i].append(0)

spis = list(range(1, 7))
n = -1

for i in range(6):
    n += 1
    m = n
    for j in range(6):
        mas[i][j] = spis[m % 6]
        m += 1

for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end = '\t')
    print()