mas = []

for i in range(10):
    mas.append([])
    for j in range(12):
        mas[i].append(0)

for i in range(10):
    for j in range(12):
        if i % 2 == 0:
            mas[i][j] = i * 12 + j +1
        else:
            mas[i][j] = (i + 1) * 12 - j

for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end = '\t')
    print()
