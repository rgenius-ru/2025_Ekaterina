# str int float 

pi = 3.14
pi_integer = int(pi)  # integer 
print(pi_integer)

number = 19
number_float = float(number)
print(number_float)

print(str(pi))
print('Привет')

print(type(pi)) # Тип данных
print(type(number))
print(type('Привет'))

# =====================

print("Онлайн-магазин")
#price = int(input('Наименование товара: '))
price = int(input('Цена: ')) # Цена
discount = int(input('Скидка: ')) # Скидка
percent = discount

print('Ваша скидка:', discount)
print('Сумма к оплате:', price - percent)
# =====================

number1 = int(input('Число 1:'))
number2 = int(input('Число 2:'))

print(number1 + number2)

# =====================

# 'text'
# "text"
# print('text' + "text")

# s = 'Наименование товара'
# print(s[1]) # доступ (к букве) по индексу
# print(s[-2])

# ===
s = input('Ваш текст: ')
index = int(input('Номер позиции буквы: '))
print(s[index - 1])