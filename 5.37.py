"""Вычислить сумму
1 - 2/3 * x + 3/4 * x^2 - 4/5 * x^3 + ... + 11/12 * x^10
при x = 2"""

x = 2
summ = 1

for i in range(1, 11):
    modul = (i + 1) * (x ** i) / (i + 2)
    slogaemoe = ((-1) ** i) * modul
    summ += slogaemoe
    print(summ)
