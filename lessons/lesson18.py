# for number in range(10):
#     print(1)
#     # continue
#     break
#     print(2)

# print("The End")


# Цикл while

# Синтаксис

# Цикл работает только если условное выражение == True
# while <условие работы цикла>: 
#     <команда 1>
#     <команда 2>
#     ...

# x = 1000

# while x > 0:
#     print("Тратим деньги!!")
#     x -= 100
#     print(x)

# print("The end")


text = "Hello world"
len_text = len(text)
i = 0

while i < len_text:
    print(text[i])
    i += 1

print("The end")