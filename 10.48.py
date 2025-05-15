"""Написать рекурсивную функцию для вычисления индекса максимального
элемента массива из n элементов. """


def maximum(lst, a=0, i=0):
    if i >= len(lst):
        return a
    if a < lst[i]:
        a = lst[i]
    i += 1
    return maximum(lst, a, i)


ls = [2, 5, 8, 12, 45, 10, 11, 33, 3]

print(maximum(ls))
