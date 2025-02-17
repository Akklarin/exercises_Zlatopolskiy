def rokirovka(p, q, r, s):
    m = p
    p = q
    q = m
    n = r
    r = s
    s = n
    return p, q, r, s


a = input('a = ')
b = input('b = ')
c = input('c = ')
d = input('d = ')

a, b, c, d = rokirovka(a, b, c, d)

print('a = ', a, ', b = ', b, ', c = ', c, ', d = ', d, sep='')
