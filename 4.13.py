a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a == 0:
    print('недопустимое значение a')
else:
    if b ** 2 - 4 * a * c >= 0:
        print('имеет')
    else:
        print('не имеет')
