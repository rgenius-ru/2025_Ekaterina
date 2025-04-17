# Операторы управления потоком break и continue

# Оператор break
# Оператор continue

# for <переменная> in <последовательность>:
#     <команда 1>
#     <команда 2>
#     <команда 3>


# students = ['Иван', 'Петр', 'Сидор', 'Алексей', 'Дмитрий', 'Алексей', 'Семен', 'Алексей', 'Александр']

# for student in students:
#     if student == 'Алексей':
#         print(student)
#         break
    
# print('Конец цикла')


# salary = [100, 200, 300, -400, 500]

# sum_salary = 0
# for s in salary:
#     if s < 0:
#         print("Зарплата не может быть отрицательной")
#         break
#     sum_salary += s

# print(f'Общая зарплата: {sum_salary}')
# print('Конец цикла')



# salary = [100, 200, 300, -400, 500]

# sum_salary = 0
# for s in salary:
#     if s < 0:
#         print("Зарплата не может быть отрицательной")
#         continue
#     sum_salary += s

# print(f'Общая зарплата: {sum_salary}')
# print('Конец цикла')

# Вариант с тем же результатом что и в предыдущем без continue
salary = [100, 200, 300, -400, 500]

sum_salary = 0
for s in salary:
    if s < 0:
        print("Зарплата не может быть отрицательной")
    else:
        sum_salary += s

print(f'Общая зарплата: {sum_salary}')
print('Конец цикла')