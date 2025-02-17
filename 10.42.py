def stepen(a, n):
    if a * n == 0:
        return 1
    return a * stepen(a, n-1)


a = int(input('Основание равно '))
n = int(input('Степень равна '))

print(stepen(a, n))
