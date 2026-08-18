# Задание 1
from itertools import count

a = 10
b = 3
x = 2.5
print(type(a), type(x))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(b ** 2)

# Задание 2
first_name = "Иван"
last_name = "Петров"
age = 25
full_name = first_name + " " + last_name
print(full_name)
print("Возраст: ", age)
print(len(full_name))
print("Иван" in full_name)
print(ord("A"))
print("Ха " * 3)
empty = ""
print(len(empty))

# Задание 3
count = 10
count += 5
count -= 3
count *= 2
count /= 4
print(count)

number_text = "2312"
print(type(int(number_text)))
print(type(number_text))