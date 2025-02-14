delta_r = 0
s = 0

for i in range(1, 101):
    delta_r = delta_r + ((-1) ** (i+1)) * 1 / i
    s = s + 1 / i

print('Итоговое расстояние от дома = ', delta_r, 'км')
print('Пройденый путь = ', s, 'км')