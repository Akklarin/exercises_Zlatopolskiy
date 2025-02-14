word = str(input('Введите предложение: '))
length = len(word)
outpt = ''

for i in range(length):
    if (word[i] == 'o' or word[i] == 'о') and i % 2 == 0:
        continue
    else:
        outpt += word[i]

print(outpt)