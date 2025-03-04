# int, float, str

a = 10      # int
b = 5.5     # float
c = "текст" # str


# Преобразование типов
# int(), float(), str()

# int(5.9) -> 5
# float('3.14') -> 3.14
# str(100) -> '100'

# Простые мат операции
# + - * /
# / (всегда возвращает float)
# // Целочисленное деление 10 // 3 = 3 (всегда возвращает int)
# % Остаток от деления 10 % 3 = 1
# ** Возведение в степень 2 ** 3 = 8


# Приоритет мат. операций
# () -> ** -> * / // % -> + -

# print(2 + 3 * 4)    # 14
# print((2 + 3) * 4)  # 20
# print(10 // 3)      # 3
# print(10 % 3)       # 1


# Строк
# '', "", '''многострочный текст''', """многострочный текст"""

# сложение строк
# умножение (повторение) строк
# перенос строки и табуляция
# print('Привет, \n\nВован!') # \n перенос на новую строку

# print('Мой возраст: \t15 лет')
# print('Мой вес: \t30 кг') # \t табуляция

# экранирование строк
# print('y = a\\n')

# print('ООО "Ромашка"')
# print("ООО 'Ромашка'")

# Срезы
# строка[start:stop:step]
text = "Python"
print(text[0:1])      # 'P'
print(text[2:5])    # 'tho' (символы с индексом 2, 3, 4)
print(text[::-1])   # 'nohtyP' (обратная строка).

# Ввод данных
# input('необязательный текст') - всегда возвращает str!


# gitHub.ru