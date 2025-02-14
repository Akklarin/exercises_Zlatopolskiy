mas = []

for i in range(7):
    mas.append([])
    for j in range(7):
        mas[i].append(0)

for i in range(7):
    j = i
    mas[i][j] = 1
    mas[i][j * (-1) - 1] = 1


for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end = '\t')
    print()