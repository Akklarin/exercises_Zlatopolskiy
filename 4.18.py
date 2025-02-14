a1x = float(input("A1(x) = "))              # A - нижняя левая точка. C - верхняя правая точка
a1y = float(input("A1(y) = "))
c1x = float(input("C1(x) = "))
c1y = float(input("C1(y) = "))

a2x = float(input("A2(x) = "))
a2y = float(input("A2(y) = "))
c2x = float(input("C2(x) = "))
c2y = float(input("C2(y) = "))

listx = [a1x, a2x, c1x, c2x]
listy = [a1y, a2y, c1y, c2y]

print('Левый нижний угол:', min(listx), ';', min(listy))
print('Правый верхний угол:', max(listx), ';', max(listy))
