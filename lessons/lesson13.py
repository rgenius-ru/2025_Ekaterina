# Функцию range() 
# range - диапазон

print(range(15))

# range(start, stop, step)

print(list(range(20)))
print(list(range(5, 20)))
print(list(range(5, 20, 3)))

print(list(range(10, 0, -1)))


for i in range(50):
    print('Привет')

for i in range(50):
    print(f'Привет уже в {i} раз')