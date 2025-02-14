mas = []

for i in range(12):
    mas.append([])
    for j in range(10):
        mas[i].append(0)

for i in range(12):
    for j in range(10):
        mas[i][j] = 12 * j + i +1

for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end = '\t')
    print()