mas = []

for i in range(5):
    mas.append([])
    for j in range(5):
        mas[i].append(0)

dabl_len = 10
x = -1
y = 0
number = 0

while dabl_len // 2 > 0:
    for i in range(dabl_len // 2):
        x += 1 * (-1) ** ((dabl_len + 1) // 2 + 1)
        number += 1
        mas[y][x] = number

    dabl_len -= 1

    for j in range(dabl_len // 2):
        y += 1 * (-1) ** ((dabl_len + 1) // 2 + 1)
        number += 1
        mas[y][x] = number

    dabl_len -= 1

for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end = '\t')
    print()

