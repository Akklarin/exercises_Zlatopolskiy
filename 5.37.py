x = 2
summ = 1

for i in range(1, 11):
    modul = (i + 1) * (x ** i) / (i + 2)
    slogaemoe = ((-1) ** i) * modul
    summ += slogaemoe
    print(summ)
