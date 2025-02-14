s1 = float(input('s1 (км) = '))
s2 = float(input('s2 (ф) = '))

s1ft = s1*1000/0.305

if s1ft > s2:
    print(s2, 'ф  меньше', sep='')
elif s1ft == s2:
    print('расстояния равны')
else:
    print(s1, 'км меньше', sep='')
