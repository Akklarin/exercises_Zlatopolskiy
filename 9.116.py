word = str(input('Что проверять будем?'))

neword = word.replace(' ', '')

reword = neword[::-1]

if neword != reword:
    print('Шеф, усё пропало!!!')
else:
    print('Клёв будет такой, что ты забудешь всё на свете')