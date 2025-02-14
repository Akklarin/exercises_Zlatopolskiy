n = int(input('Введите n: '))
summ = 0
chislitel = 1

for i in range(1, n+1):
    a = chislitel / i
    chislitel *= -1
    summ += a

print(summ)
