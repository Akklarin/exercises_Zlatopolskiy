"""Дано слово, состоящее из четного числа букв. Вывести на экран его первую
половину, не используя оператор цикла. """

word = str(input('Введите слово: '))

l = len(word)//2

print(word[:l])
