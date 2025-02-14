
cells_all = [1, 3, 4, 5, 7, 11, 13, 15, 16, 16, 16, 16, 15, 18, 19, 20, 21, 22, 24, 28]

for i in range(len(cells_all) - 1):
    if cells_all[i] == cells_all[i + 1]:
        n = i + 1
        break

counter = 2

while n < len(cells_all) - 1:
    if cells_all[n] == cells_all[n + 1]:
        counter += 1
        n += 1
    else:
        break

print(counter)