# print("====")
# print("Русский язык")

# print("Текст 1", 'Текст 2')
# print()
# print("Текст 1", 'Текст 2')

# age = 20 + 1
# print(age)

# print(20 + 10)

# price = 300
# discount = 0.20
# percent = 1 - discount

# price_rub = 88.25
# course = 88.25
# print (price_rub / course)
# price = 10000
# prize = 0.13
# print (prize * price + price)
price = int(input('Цена: ')) # Цена
discount = int(input('Скидка: ')) # Скидка
percent = 1 - discount

print('Ваша скидка:', discount)
print('Сумма:', price * percent)