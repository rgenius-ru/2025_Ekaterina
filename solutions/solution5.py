# #Задание1
# name =input("Имя: ")
# age = int(input('Возраст: '))
# hobby = input('Любимое занятие: ')
# #print(name,'говорит:', "Обожаю", hobby+"!\nЭто моё самое большое увлечение!")

# message=f"""
# ==={name}===
# Возраст {age}
# Хобби: {hobby}

# {name}, говорит: Обожаю {hobby}!
# 'Это моё самое большое увлечение!'"""

# print(message)

#Задание 2
name =(input("Имя персонажа "))
text =(input("Текст сообщения ")) 
line = "─"*(len(text)+4)
message=f"""
     ┌{line}┐  
     │  {text}  │  
     └{line}┘  
      \\  
       \\  
        😀☁️  
    
Говорит: {name}"""

print(message)

