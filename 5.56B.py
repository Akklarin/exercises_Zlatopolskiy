num = int(input('Сколько будет слагаемых?'))
vvod = str(input('Введите числа через пробел, в конце нажмите Enter: '))
spis = vvod.split(' ')
vyvod = ''

for i in range(1, num):
    vyvod = vyvod + str(int(spis[i-1]) + int(spis[i])) + ', '

print(vyvod[:-2] + '.')