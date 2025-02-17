text = str(input('Введите текст: '))
char = str(input('Укажите искомый символ: '))

text = text.lower()
char = char.lower()
count = 0

for i in text:
    if i == char:
        count += 1

print(count)