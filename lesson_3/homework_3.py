# Часть 1
from encodings import shift_jisx0213

from lesson_2.lesson_2_2 import s13

s1 = "Привет, мир!"
print(s1)
s2 = 5
s3 = 10
s4 = 15
print(f"{s2} {s3} {s4}")
s5 = 10 + 25
print(s5)
s6 = 1
s7 = 2
s8 = 3
print(s6, s7, s8, sep=" & ")
print("Python", end=" ")
print("лучший язык")
x = 3.14
y = -8
print(f"Координаты точки: x = {x} ; y = {y}")

# Часть 2

# s9 = input("Введите имя: ")
# print("Привет, ", s9)
# s10 = input("Введите возраст: ")
# print(f"Имя: {s9}, Возраст: {s10}")

# s11 = int(input("Число 1: "))
# s12 = int(input("Число 2: "))
# print(f"Сумма: {s11 + s12}")
# print(f"Квадрат числа: {s11 ** 2}")
# print(f"Периметр: {2 * (float(s11) + float(s12))}")

# Часть 3

print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)

res = (8 > 12)
print(res, type(res))

z = 15
print(z % 2 == 0)
print(z % 5 == 0)
print(z % 3 == 0 and z % 5 == 0)
print(z % 3 == 0 or z % 5 == 1)

u = 4.5
print(1 <= u <= 10)
print(0 <= u <= 5 or 10 <= u <= 15)
print(not(u < 5))

print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))

# Часть 4

s13 = "Программирование"
print(s13[0])
print(s13[-1])
print(s13[2])
print(s13[-2])
print(s13[:6])
print(s13[-5:])
print(s13[2:7])
print(s13[::2])
print(s13[::-1])
print(len(s13))
print(s13[1:15])

# Часть 5

# s14[0] = "п"

s14 = "" + s13[1:15] + ""
print(s14)