"""Даны натуральное число n и числа a1, a2, ..., an.
Определить a1 + a2, a2 + a3, ..., an-1 + an"""

num = int(input('Сколько будет слагаемых?'))
vvod = str(input('Введите числа через пробел, в конце нажмите Enter: '))
spis = vvod.split(' ')
vyvod = ''

for i in range(1, num):
    vyvod = vyvod + str(int(spis[i-1]) + int(spis[i])) + ', '

print(vyvod[:-2] + '.')
