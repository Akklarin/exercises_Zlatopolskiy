word = ' ' + str(input('Введите слово: '))

for i in range(1, len(word)):
    if word[i:] == '':
        continue
    else:
        factory = word.lower()[i:]
        factory_cap = factory.capitalize()
        word = word[:i] + factory_cap.replace(factory[0], '')

print(word.lower()[1:])
