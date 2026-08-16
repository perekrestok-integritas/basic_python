name = "Sandra"
age = 39
height = 1.63
print("Name:", name)
print("Age:", age)
print("Height:", height)

x = 10
print(x, type(x))
x = 25.5
print(x, type(x))
x = "Python"
print(x, type(x))

a = 7
b = a
print(a, b)
a = 10
print(a, b)
# b не изменилось, так как в момент создания b получает ссылку на число 7, также, как a.
# Но после изменения переменной a, a получает другую ссылку, а b остается со своей.

x = y = z = 100
print(x, id(x), y, id(y), z, id(z))
x, y, z = 101, 102, 103
print(x, id(x), y, id(y), z, id(z))

a = 5
b = 10
a, b = b, a
print(a)
print(b)

import keyword
print(keyword.kwlist)

