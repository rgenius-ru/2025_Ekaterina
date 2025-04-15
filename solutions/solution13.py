# print(list(range(1,6)))
# for i in range(1,6):
    # print(i)

# summa=0
# for i in range(1,11):
#     summa=summa+i
#     print(summa)

# summa=5
# for i in range(1,101):
#     summa=summa+i
#     print(summa)

# [3, 7, 2, 9, 5]
# for i in [3, 8, 2, 9, 5]:
#     if i%2!=0:  
#         print(i)

# [10, 3, 8, 1, 15, 6]
# Подсчет элементов
# Дан список: [10, 3, 8, 1, 15, 6]. Посчитайте, сколько в нем чисел, которые больше 5. 
# Выведите ответ.

# Пример вывода:
# Количество чисел больше 5: 4
# count=0
# for i in [10, 3, 3, 1, 15, 6]:
#     if i>5:
#         count+=1
# print(count)
        

# Даны два целых числа A и B (при этом A ≤ B). 
# Выведите все числа от A до B включительно.

# a = int(input())
# b = int(input())
# for i in range(a,b+1): 
#     print(i)

# Даны два целых числа A и В. Выведите все числа от A до B включительно, в
# порядке возрастания, если A < B, или в порядке убывания в противном случае.
# a = int(input())
# b = int(input())
# if a<b:
#     for i in range(a,b+1): 
#         print(i)
# else:
#     for i in range(a,b-1,-1): 
#         print(i)

# Даны два целых числа A и В, A>B. 
# Выведите все нечётные числа от A до B включительно, в порядке убывания. 
# В этой задаче можно обойтись без инструкции if.

#вар1
# a = int(input())
# b = int(input())
# for i in range(a,b-1,-1): #start, stop, step
#     if i%2!=0:
#         print(i)

#вар2
# a = int(input())
# b = int(input())
# for i in range (a - (a + 1) % 2, b - b % 2, -2):
#     print (i)

# Дано 10 целых чисел.
# Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
#вар1 неверный
# summa=0
# for i in range(10):
#    number = int(input())
#     summa+=number
# print(summa) 

#вар2
# a = int(input())
# summa = 0
# for i in range(a):
#     summa += int(input())
# print(summa)

# Дано несколько чисел. Вычислите их сумму. 
# Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
# Какое наименьшее число переменных нужно для решения этой задачи?

# a = int(input())
# summa = 0
# for i in range(a):
#     summa += int(input())
# print(summa)

# Условие
# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. 
# Подсчитайте количество нулей среди введенных чисел и выведите это количество. 
# Вам нужно подсчитать количество чисел, равных нулю,а не количество цифр.

# N = int(input())
# count=0 
# for i in range(N):
#     m = int(input())
#     if m==0:
#         count+=1
# print(count)

# Условие
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, 
# i-я ступенька состоит из чисел от 1 до i без пробелов.

n = int(input())
n<=9
for i in range(1, n+1):
    for m in range(1, n-i):
        print(m)
    print(i)