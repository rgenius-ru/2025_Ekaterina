# Списки. Продолжение.
## Создание
## Изменение
## Операции со списками
## Двумерные и многомерные списки
## Длина списков
## Обработка ошибок выхода за границы

# Создание
l1 = []
print(l1)

l2 = list()
print(l2)

l3 = [1, 2, 3]
l4 = list([2, 2, 2])
print(l3, l4)

l5 = l4 = list('222')
print(l5)

print(list('hello how are you?'))


# Изменение
l3[2] = 333
print(l3)

print(l3[1:])
l3[1:] = [222, 555]
print(l3)

print(l3[1:])
l3[1:] = [10, 20, 30]
print(l3)


# Операции со списками
print([1, 1, 1] + [2, 2, 2])
print([2, 3] * 5)


# Двумерные и многомерные списки
l6 = [1, [10, 20], 3]
l7 = [1, [10, 20, ['привет', 'пока']], 3]

print(l6[1][1])
print(l7[1][2][0])


# Длина списков
print(len(l6))
print(len(l7))


# Обработка ошибок выхода за границы
l8 = [1, 2, 50, 60]
# print(l8[4])  # ERROR IndexError: list index out of range
