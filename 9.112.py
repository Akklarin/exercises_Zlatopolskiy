word = str(input('Введите предложение: '))
m = int(input('Порядковый номер начального символа: '))
n = int(input('Порядковый номер конечного символа: '))

print(word.replace(word[m-1:n], ''))