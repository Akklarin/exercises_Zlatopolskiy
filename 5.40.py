"""Даны натуральное число n и вещественные числа a1, a2, ..., an. Определить
сумму всех вещественных чисел."""

summ = 0
num = int(input('Сколько будет слагаемых?'))

for i in range(1, num+1):
    string = 'Введите ' + str(i) + 'е число:'
    n = float(input(string))
    summ = summ + n

print(summ)