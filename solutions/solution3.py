# Задание 1: Извлечение подстроки
text = "Привет, мир!"
print(text[0:6])

# Задание 2: Реверс строки
text = "Python"
reversed_string = (text[::-1]) 
print(reversed_string)

# Задание 3: Удаление символов по индексам
text = "Привет, Мир!"
text1 = text[1:]
text2 = text[:5:]
text3 = text[7:]
modified_string = text1+text2+text3
print(modified_string)