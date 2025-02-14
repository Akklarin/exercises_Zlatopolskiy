summ = 0

for i in range(1, 11):
    string = 'Введите ' + str(i) + 'е число:'
    n = float(input(string))
    summ = summ + n

print(summ)
