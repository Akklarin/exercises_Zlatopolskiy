"""Для условий предыдущей задачи в случае наличия вещественных корней найти их,
в противном случае — вывести на экран соответствующее сообщение.
Вариант равенства корней отдельно не рассматривать. """

import math as m

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a == 0:
    print('недопустимое значение a')
else:
    if b ** 2 - 4 * a * c <= 0:
        print('нет корней')
    else:
        print((-b + m.sqrt(b ** 2 - 4 * a * c))/(2*a))
        print((-b - m.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
