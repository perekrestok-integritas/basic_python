s1 = "string"
print(34, s1)
print(34, 157, "qwerty", s1)
print(2 - 10 * 9)

a = 1
b = 2
c = 3
print(a, b, c, sep=" & ", end=" ; ")
print(a, b, c, sep=" & ", end="\n")
print(a, b, c, sep=" & ")
print(a, b, c, sep=" & ")

print("Результат умножения", b, "на", c, ":", "равно", b * c)
print(f"Результат умножения {b} на {c} равен {b * c}")

# {} - вставляет переменные и что угодно внутрь одной строки
# f (f-string) - меняет формат строки
# sep="" - добавляет любой символ меду переменным
# end="" - указывает print, что надо сделать в конце строки

# s2 = input()
# print(s2)
# v = int(input())
# print(type(v))
# print(v)

# По умолчанию input всегда является строкой.
# Меняем тип сами при необходимости.

s3 = float(input("Длина: "))
s4 = float(input("Ширина: "))
print(f"Периметр: {2 * (s3 + s4)} cm")