# Даны два целых числа. Выведите значение наименьшего из них.

# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите первое число: "))
# if number1<number2:
#     print(number1)
# if number2<number1:
#     print(number2)

# Условие
# Заданы две клетки шахматной доски. Если они покрашены в один цвет, 
# то выведите слово YES, а если в разные цвета — то NO. Программа получает
# на вход четыре числа от 1 до 8 каждое, задающие 
# номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# number4 = int(input())
# if (number1 + number2 + number3 + number4) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# Условие
# Даны три целых числа. Выведите значение наименьшего из них.

# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# if number1<=number2 and number1<=number3:
#     print(number1)
# elif number2<=number1 and number2<=number3:
#     print(number2)
# else:
#     print(number3)

# Даны три целых числа. Определите, сколько среди них совпадающих. Программа
# должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0
# (если все числа различны).

number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1==number2==number3:
    print("3")
elif number1 != number2 and number1 != number3 and number2 != number3:
    print("0")
else:
    print('2')


