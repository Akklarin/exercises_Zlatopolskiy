"""Дано слово. Если его длина нечетная, то удалить среднюю букву,
в противном случае — две средних буквы. """

word = str(input('Введите слово: '))

l = len(word)
nomer = len(word)//2

if l % 2 == 0:
    print(word.replace(word[nomer-1:nomer+1], ''))
else:
    print(word.replace(word[nomer], ''))
