def summa(x):
    if x == 0:
        return 0
    ost = x % 10
    return ost + summa(x // 10)


number = int(input('Введите число: '))

print(summa(number))