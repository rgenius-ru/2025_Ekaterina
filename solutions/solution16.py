# free = ['свежий', 'свежий', 'несвежий', 'свежий', 'свежий']
# for f in free:
#     if f == 'несвежий':
#         print('Остановить разгрузку овощей')
#         break 
#     print(f)

# free = ['свежий', 'свежий', 'несвежий', 'свежий', 'свежий']
# for f in free:
#     if f == 'несвежий':
#         print('Остановить разгрузку овощей')
#         continue 
#     print(f)

# 1. Поиск стоп-слова
# list = [
#     "начало",
#     "продолжение",
#     "пауза",
#     "СТОП",
#     "конец",
#     "игра",
#     "время",
#     "завершение",
#     "перерыв",
#     "сигнал"
# ]
# for i in list:
#     if i == 'СТОП':
#         print("Найдено стоп-слово: СТОП")
#         break 
#     print(i)

# 2. Сумма четных чисел
# salary = [1, 3, 4, 7, 8, 10, 11]
# sum_salary = 0
# for i in salary:
#     if i%2==0:
#         sum_salary += i
#     continue
# print(f"Сумма четных: {sum_salary}")

# 3. Пропуск ошибок НЕ СМОГЛА посчитать слово ошибка
# list = [10, 12, "ошибка", 20, "ошибка", 30, -1, 40]
# sum_list = 0
# sum_2 = 0
# for i in list:
#     if i == "ошибка":
#         # sum_2 += i
#         # a = len('ошибка')
#         continue
#     # print(f"Пропущено {a} ошибки")
#     sum_list += i
# print(f"Общая сумма: {sum_list}")

# list = [10, 12, "ошибка", 20, "ошибка", 30, -1, 40]
# sum_2 = 0
# for i in list:
#     if i == input("ошибка"):
#         continue
#     sum_2 += i
#         # continue
# print(f"пропущено: {sum_2} ошибки")

# 4. Поиск в матрице
# flag = False  НЕ РАЗОБРАЛАСЬ            
# matrix = [
#     [10, 20, 30],
#     [45, 55, 65],
#     [70, 80, 90]
# ]
# for i in matrix[0]:
#     if i >= 50:
#         print(f"Первое число больше 50: {i}")
#         break
#     for i in matrix[1]:
#         if i >= 50:
#             print(f"Первое число больше 50: {i}")
#             break
#         for i in matrix[2]:
#             if i >= 50:
#                 print(f"Первое число больше 50: {i}")
#                 break
