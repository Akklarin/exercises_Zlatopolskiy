"""Вычислить сумму
x + (x^3)/3 + (x^5)/5 + ... + (x^11)/11
при x = 2"""

x = 2
summ = 0

for i in range(1, 12, 2):
    summ += (x ** i) / i

print(summ)
