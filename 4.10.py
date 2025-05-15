"""Даны радиус круга и сторона квадрата. У какой фигуры площадь больше?"""

import math as m
r = float(input('r = '))
a = float(input('a = '))

skr = m.pi*r**2
skv = a**2

if skr > skv:
    print('s круга больше')
else:
    print('s квадрата больше')
